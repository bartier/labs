docker-build:
	docker build -t app:latest .

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs

logs-app:
	docker-compose logs app

logs-db:
	docker-compose logs db

ps:
	docker-compose ps

restart:
	docker-compose restart

clean:
	docker-compose down -v
	docker system prune -af --volumes
