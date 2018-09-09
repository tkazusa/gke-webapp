APP := webapp

BACKEND_DIR := backend/
FRONTEND_DIR := frontend/

BACKEND_IMAGE := backend:v1.0
FRONTEND_IMAGE := frontend:v1.0

BACKEND_CONTAINER := backend
FRONTEND_CONTAINER := frontend

PROJECT_ID := "gke-webapp"

# main commands
.PHONY: build
build: backend/ frontend/ 
	sudo docker build -t  $(BACKEND_IMAGE) $(BACKEND_DIR)
	sudo docker build -t  $(FRONTEND_IMAGE) $(FRONTEND_DIR)

.PHONY: install
install: requirements.txt
	pip intall -r requirements.txt

.PHONY: run
run:
	sudo docker run -d --name $(BACKEND_CONTAINER) -e PROJECT_ID=$(PROJECT_ID) $(BACKEND_IMAGE)
	sudo docker run -itd --name $(FRONTEND_CONTAINER) -p 8080:8080 -e PROJECT_ID=$(PROJECT_ID) --link backend:backend $(FRONTEND_IMAGE)
	

.PHONY: clean
clean:
	sudo docker stop $(BACKEND_CONTAINER)
	sudo docker rm $(BACKEND_CONTAINER)
	sudo docker rmi $(BACKEND_IMAGE)
	
	sudo docker stop $(FRONTEND_CONTAINER)
	sudo docker rm $(FRONTEND_CONTAINER)
	sudo docker rmi $(FRONTEND_IMAGE)

