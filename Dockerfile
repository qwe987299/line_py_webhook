# 使用 Python 基礎映像檔
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製程式碼到容器
COPY app.py /app/
COPY requirements.txt /app/

# 安裝所需套件
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 預設的 5000 埠
EXPOSE 5000

# 啟動應用
CMD ["python", "app.py"]
