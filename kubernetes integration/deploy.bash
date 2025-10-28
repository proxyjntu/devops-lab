#!/bin/bash

# Build Docker image
docker build -t myflaskapp:latest .

# Optional: push to Docker Hub
# docker tag myflaskapp:latest <username>/myflaskapp:latest
# docker push <username>/myflaskapp:latest

# Apply Kubernetes deployment and service
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Show current pods and service
kubectl get pods
kubectl get svc
