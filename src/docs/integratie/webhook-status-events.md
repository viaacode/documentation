---
title: Webhook Status Events
nav_order: 5
---

# Introduction

This document describes the use of webhooks to receive update events about submitted [meemoo SIP v2.x](../diginstroom/sip/index.md) files.

After submission, an event is sent out when:
- the SIP package is fully and correctly archived in the meemoo archive system
- there is an error somewhere in the processing pipeline, including the meemoo archive system. These events contain a description of the error.

No interim _in progress_ events are sent out. Only when the status changes.

# Pre-process

## Submitting the SIP to S3

On the [SIP Submission page](../diginstroom/aanlevering-van-sips.md) you will find the procedure to request an S3 token so that the package can be uploaded. After a successful transfer, you will find a correlation ID in the custom key `X-Correlation-ID` in the headers of the response object of the S3 transfer:

``` json
{
    "Server": "nginx/1.26.2",
    "Date": "Fri,11 Jul 2025 15:56:30 GMT",
    "Transfer-Encoding": "chunked",
    "Connection": "keep-alive",
    "x-amz-request-id": "981F27F72E5E7EBF-843e9ba457593d0edf69a24baa0babf3",
    "Via": "1.1 s3-qas.do.viaa.be (Cloud Gateway S3/8.2.0)",
    "Gateway-Protocol": "s3",
    "ETag": "294a6020d4588dfd92b936a1a620fcd2",
    "X-Correlation-ID": "843e9ba457593d0edf69a24baa0babf3"
}
```

If you are using the Python library `boto3`, the response object is in the form of a Python dictionary, with the following structure:

``` json
{
    <SNIP>
    "ResponseMetadata": {
        "HTTPStatusCode": 200,
        "RetryAttempts": 0,
        "HostId": "",
        "RequestId": "5916962FB12A52B7-a5f7312a0b9555b747361c4c407924eb",
        "HTTPHeaders": {
            "via": "1.1 s3.viaa.be (Cloud Gateway S3/7.5.0)",
            "transfer-encoding": "chunked",
            "x-correlation-id": "a5f7312a0b9555b747361c4c407924eb",
            "server": "nginx/1.21.3",
            "connection": "keep-alive",
            "x-amz-request-id": "5916962FB12A52B7-a5f7312a0b9555b747361c4c407924eb",
            "date": "Wed, 05 Apr 2023 13:11:34 GMT",
            "gateway-protocol": "s3",
            "content-type": "application/zip"
        }
    }
}
```
The correlation ID is available via `response['ResponseMetadata']['HTTPHeaders']['x-correlation-id']`.

This correlation ID is used throughout the process to identify the lifecycle of that SIP. It is unique to one submission of one SIP. If the same SIP is submitted multiple times, different correlation IDs will result.

# Webhook

The implementation of the webhooks is inspired by the [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) guidelines. There is also a [formal specification](../../assets/webhooks/openapi.yml) available in the form of an [OpenAPI specification v3.1.x](https://spec.openapis.org/oas/v3.1.1.html). This describes both the HTTP request and the structure of the sent event.

Here, we will discuss some elements of the specification, as well as certain aspects that fall outside the scope of the formal specification.

## Registration

If you are interested in receiving status updates via webhooks, you should contact [meemoo support](mailto:support@meemoo.be). It is currently not possible to register or manage webhooks automatically, such as through a web interface or REST API.

There are some administrative items to share, particularly the `endpoint` and the `shared secret` (See: [Headers](#headers)). This is done in collaboration with meemoo.

One webhook registration pertains to one S3 bucket. This means that events will be sent to the webhook endpoint for all SIP files uploaded to that bucket.

## Payload

The webhook is an HTTP POST request. The actual event is contained in the HTTP body in the form of JSON.

The structure of the payload:
- `type`: The type of the event, in dot-notated form. Currently, it is always `meemoo.sip.archived`.
- `timestamp`: The timestamp when the event occurred. This is not necessarily when the event is sent. This timestamp is in ISO 8601 format.
- `data`: The actual event data associated with the event.
    - `correlation_id`: This is the correlation ID as described above.
    - `outcome`: The outcome of the event: "success" or "failure".
    - `message`: Additional information about the event, in the case of a failed event. [Optional]
    - `pid`: The meemoo PID of the ingested SIP, if present. [Optional]

Example:
``` json
{
  "type": "meemoo.sip.archived",
  "timestamp": "2025-09-03T20:26:10.344522Z",
  "data": {
    "correlation_id": "843e9ba457593d0edf69a24baa0babf3",
    "outcome": "success",
    "pid": "kdleipkyuj"
  }
}
```

A SIP is successfully archived if the event, with its associated `correlation_id`, has the `type` as `meemoo.sip.archived` and the `outcome` as `success`. If the `outcome` is `failure`, regardless of the `type`, the SIP has failed during ingestion. Note: non-fatal (recoverable) errors may result in a "success" being sent for a SIP that previously had a "failure".

The formal specification in the form of a JSON schema can be found in the [OpenAPI specification](https://github.com/viaacode/sipin-status-webhook-documentation/blob/main/openapi.yml)

## Headers

The payload of the webhook is sent as the body of an HTTP POST request. The additional data about the webhook resides in the HTTP headers:

- `webhook-id`: the unique identification of the event from the webhook. This is associated with the event and remains the same if the event is sent multiple times.
- `webhook-timestamp`: an integer UNIX timestamp (seconds since the epoch). This timestamp describes the moment the webhook was sent. If the same event is sent multiple times, this timestamp will have a different value.
- `webhook-signature`: one or more (space-separated) signatures of this webhook, at least one of which is valid.

A signature in `webhook-signature` consists of the following content: `{msg_id}.{timestamp}.{payload}` (concatenation of these three fields, separated by a dot), with the following properties:

|                         | Symmetric signature                                             |
| ----------------------- | --------------------------------------------------------------------- |
| Signature scheme        | `HMAC-SHA256`                                                         |
| Signing secret          | Shared secret. Random, at least 24 bytes (192 bits)                  |
| Serialization secret    | Base64 encoded, with prefix `whsec_` for easy identification.        |
| Signature identifier    | `v1`                                                                  |

The "serialization secret" describes how the secret is serialized. For example, if the actual secret is `alongwebhookmeemoosecret`, the serialization is `whsec_YWxvbmd3ZWJob29rbWVlbW9vc2VjcmV0` (whsec_{base64encode(b"alongwebhookmeemoosecret")}).

The "signature identifier" is added as a version prefix to the signature when serialized and sent in the webhook. The signature itself is encoded as base64. For example: `v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=` (v1,{base64encode(signature_in_bytes)}).

### Example
Let's put everything together. Suppose a webhook with the following `id` and `timestamp`:

```
webhook-id: msg_333a3NGSYKk1vyFtMgj9Qy8gm3y
webhook-timestamp: 1758548009
```

With the payload (the exact body of the HTTP request):
``` json
{"type": "meemoo.sip.archived", "timestamp": "2025-09-03T20:26:10.344522Z", "data": {"correlation_id": "843e9ba457593d0edf69a24baa0babf3", "outcome": "success", "pid": "kdleipkyuj"}}
```

This results in the following to be signed:
```
msg_333a3NGSYKk1vyFtMgj9Qy8gm3y.1758548009.{"type": "meemoo.sip.archived", "timestamp": "2025-09-03T20:26:10.344522Z", "data": {"correlation_id": "843e9ba457593d0edf69a24baa0babf3", "outcome": "success", "pid": "kdleipkyuj"}}
```
Using the secret `whsec_YWxvbmd3ZWJob29rbWVlbW9vc2VjcmV0` (whsec_{base64encode(b"alongwebhookmeemoosecret")}), the signature becomes:
```
webhook-signature: v1,cVueLJYV5JY6qXHw3+MIHbZCPHHnX7N7jjaebaI2+5o=
```

You can find libraries for several common languages, such as Python, Golang, Java, etc., in the [standard-webhooks repository](https://github.com/standard-webhooks/standard-webhooks/tree/main/libraries). These libraries facilitate signing and validating webhooks. We recommend using these implementations where possible, or at least incorporating them in a way that makes sense. Many of these libraries are also published in their respective repositories.

## Security
In the context of webhooks, we can identify these security aspects:
- **Authenticity**: Is the sender indeed the sender they claim to be?
- **Integrity**: Has the webhook been intercepted and modified along the way?
- **Replayability**: Can we determine if a webhook has been sent and processed before?

| Authenticity   | Integrity  | Replayability                                          |
| --------------- | ----------- | ------------------------------------------------------ |
| Signature      | Signature  | Combination of webhook identifier and webhook timestamp |

The server implementation has some freedom in how it verifies what it needs.

There is an additional layer of security in the form of TLS. The endpoint **must** be a HTTPS endpoint. This encrypts the payload.

## Deliverability and Reliability
The submission of a webhook is considered successful if it receives a `2xx` status code. All other scenarios are marked as failed. If the submission is failed, we will retry sending the event up to the point of success or until all attempts are exhausted. This is based on an incremental backoff schedule:

| Delay      | Time since start  |
| ----------- | ----------------- |
| Immediate   | 00:00:00          |
| 5 seconds   | 00:00:05          |
| 5 minutes   | 00:05:05          |
| 30 minutes  | 00:35:05          |
| 2 hours     | 02:35:05          |
| 5 hours     | 07:35:05          |
| 10 hours    | 17:35:05          |
| 10 hours    | 27:35:05          |

If no successful webhooks can be sent to the agreed endpoint after a period of 72 hours, the system will stop sending events to the designated endpoint. Contact [meemoo support](mailto:support@meemoo.be) in such cases.

Note that we implement a timeout of 15 seconds. If no response is received after 15 seconds, the webhook is interpreted as failed and will be resent according to the above principles.

Keep in mind that we do not guarantee that each event is sent exactly once. Be aware that (in exceptional cases) an event may be sent multiple times ("at least once semantics").
