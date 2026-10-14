FROM python:3.12.12-slim-bookworm

WORKDIR /docs

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
