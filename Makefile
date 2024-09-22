CONTAINER_NAME=tcc

.PHONY: build
build:
	@docker-compose build --pull

.PHONY: down
down:
	@docker-compose down ${CONTAINER_NAME}

.PHONY: combine-data
combine-data:
	@docker-compose run --rm -e --name ${CONTAINER_NAME} python app/01_combine_data.py
