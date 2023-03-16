up:
	 docker-compose -f docker-compose.yml -f docker-compose.supserset.yml up -d --build
down:
    docker-compose -f docker-compose.yml -f docker-compose.supserset.yml down
logs:
	docker-compose -f docker-compose.yml -f docker-compose.supserset.yml logs -f