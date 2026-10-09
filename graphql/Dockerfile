FROM node:22.15.0-alpine

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts

WORKDIR /workspace
ENTRYPOINT ["/app/node_modules/.bin/gqlmd"]
CMD ["graphql-to-doc", "--force"]
