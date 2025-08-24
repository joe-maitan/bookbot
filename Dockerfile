FROM python:3.12-slim

RUN apt update && apt install -y curl && \
    mkdir -p /books && \
    curl -o /books/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt && \
    useradd -m appuser && \
    chown -R appuser:appuser /books

USER appuser
WORKDIR /bookbot
COPY . .

CMD ["python3", "main.py", "/books/frankenstein.txt"]
