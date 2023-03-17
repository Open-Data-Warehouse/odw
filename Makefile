up:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml up -d --build
up-init:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml up -d minio
down:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml down
logs:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml logs -f
