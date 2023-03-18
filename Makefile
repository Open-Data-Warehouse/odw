up:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml up -d
up-init:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml up -d minio
up-build:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml up -d --build
down:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml down
logs:
	docker-compose -f docker-compose.yml -f docker-compose.superset.yml logs -f
