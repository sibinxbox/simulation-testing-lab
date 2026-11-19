# Simulation Testing Lab

Company-style DevOps practice platform.

## Architecture

Browser -> Nginx -> Flask/Gunicorn -> PostgreSQL

## Start

```bash
cp .env.example .env
make up
```

Open http://localhost:8080

## Validate

```bash
make health
curl http://localhost:8080/ready
curl http://localhost:8080/version
curl http://localhost:8080/metrics
```

## Test

```bash
make test
make lint
```

## Stop

```bash
make down
```

Future phases add registry publishing, CI/CD deployment, rollback, monitoring and cloud infrastructure.
