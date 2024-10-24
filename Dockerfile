# ใช้ Python base image
FROM python:3.12

# ตั้ง working directory
WORKDIR /app

# ติดตั้ง CMake และ build-essential
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install face_recognition_models
#RUN pip3 install face_recognition_models

# คัดลอกไฟล์ requirements.txt
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip install setuptools

# คัดลอกโค้ดโปรเจกต์
COPY API ./API

# เปิดพอร์ตที่ FastAPI จะฟัง
EXPOSE 8000

# คำสั่งในการรันแอป
CMD ["fastapi", "run", "API/FaceRecognitionApi.py", "--port", "8000"]