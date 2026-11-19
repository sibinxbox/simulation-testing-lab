# Troubleshooting

Check containers:

```bash
docker compose ps
```

Check logs:

```bash
docker compose logs --tail=100 app
docker compose logs --tail=100 db
docker compose logs --tail=100 nginx
```

Rebuild:

```bash
docker compose down
docker compose up -d --build
```
