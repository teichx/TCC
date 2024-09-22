CONTAINER_NAME=tcc

.PHONY: build
build:
	@docker-compose build --pull

.PHONY: down
down:
	@docker-compose down ${CONTAINER_NAME}
