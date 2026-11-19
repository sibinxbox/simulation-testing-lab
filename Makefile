setup:
	cp -n .env.example .env || true

test:
	pytest -q

lint:
	ruff check app tests

security:
	bandit -r app -q
	pip-audit

build:
	docker compose build

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=100

health:
	curl -fsS http://localhost:8080/health

clean:
	docker compose down -v --remove-orphans
