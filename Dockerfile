FROM python:3.12-slim

ARG APP_VERSION
ARG GIT_COMMIT
ARG REPOSITORY
ARG BUILD_DATE

LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${GIT_COMMIT}" \
      org.opencontainers.image.source="${REPOSITORY}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY VERSION .

EXPOSE 5000

CMD ["python", "app.py"]