# FaceRecognitionApi
เป็น API สำหรับตรวจสอบใบหน้าว่าตรงหรือไม่

## library จำเป็นสำหรับ project
```bash
cmake
dlib
face_recognition
fastapi
google-cloud-storage
```

## docker
```bash
## build image
docker build -t face-recognition-api .
## run container
docker run -d --name face-recognition-api-container -p 8000:8000 face-recognition-api
```
