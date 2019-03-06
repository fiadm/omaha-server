.PHONY: build-base-alpine
build-base-alpine:
	docker build -t crystalnix/omaha-server-base:alpine -f Dockerfile-base-alpine .

.PHONY: build-dev
build-dev:
	docker build -t crystalnix/omaha-server:dev -f Dockerfile-dev .

.PHONY: lock
lock:
	pipenv lock

.PHONY: test
test:
	pipenv run paver run_test_in_docker

.PHONY: up
up:
	pipenv run paver up_local_dev_server

.PHONY: exec
exec:
	docker-compose -f docker-compose.dev.yml -p dev exec web sh

.PHONY: ps
ps:
	docker-compose -f docker-compose.dev.yml -p dev ps

.PHONY: logs
logs:
	docker-compose -f docker-compose.dev.yml -p dev logs -f web

.PHONY: stop
stop:
	docker-compose -f docker-compose.dev.yml -p dev stop

.PHONY: rm
rm:
	docker-compose -f docker-compose.dev.yml -p dev rm -f
