up:
	 docker-compose -f docker-compose.yml -f docker-compose.supserset.yml up -d --build
logs:
	docker-compose -f docker-compose.yml -f docker-compose.supserset.yml logs -f