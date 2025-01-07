#!/bin/bash

# 停止並移除與 Docker Compose 相關的容器和映像檔
echo "Stopping and removing existing containers..."
docker compose down

# 更新程式碼
echo "Pulling latest code from Git..."
git pull

# 重建映像檔
echo "Building new Docker image..."
docker compose build --no-cache

# 啟動服務
echo "Starting new container..."
docker compose up -d

echo "Update and deployment completed successfully!"
