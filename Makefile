BACKEND_DIR := backend/
FRONTEND_DIR := frontend/

BACKEND_IMAGE := backend:v1.0
FRONTEND_IMAGE := frontend:v1.0

BACKEND_CONTAINER := backend
FRONTEND_CONTAINER := frontend

PROJECT_ID := "gke-webapp"


.PHONY: build
build: backend/ frontend/ 
	 sudo docker build -t  $(BACKEND_IMAGE) $(BACKEND_DIR)
	 sudo docker build -t  $(FRONTEND_IMAGE) $(FRONTEND_DIR)

.PHONY: up
up:
	sudo docker-compose up -d

.PHONY: clean
	sudo docker-compose stop
	sudo docker-compose down

.PHONY: stop
stop:
	sudo docker-compose stop

.PHONY: down
down:
	sudo docker-compose down
	
.PHONY: clean
clean:
	 docker stop $(BACKEND_CONTAINER) $(FRONTEND_CONTAINER)
	 docker rm $(BACKEND_CONTAINER) $(FRONTEND_CONTAINER)
	 docker rmi $(BACKEND_IMAGE) $(FRONTEND_IMAGE)

.PHONY: install
install: requirements.txt
	pip intall -r requirements.txt

.PHONY: run
run:
	 sudo docker run -d --name $(BACKEND_CONTAINER) -e PROJECT_ID=$(PROJECT_ID) $(BACKEND_IMAGE)
	 sudo docker run -itd --name $(FRONTEND_CONTAINER) -p 8080:8080 -e PROJECT_ID=$(PROJECT_ID) --link backend:backend $(FRONTEND_IMAGE)

