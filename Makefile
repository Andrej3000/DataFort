up:
	docker compose down && docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f
