# FaceRecognitionApi
เป็น API สำหรับตรวจสอบใบหน้าว่าตรงหรือไม่

# library จำเป็นสำหรับ project
cmake
dlib
face_recognition
fastapi
google-cloud-storage

# คำสั่งรัน docker
# build image
docker build -t face-recognition-api .
# run container
docker run -d --name face-recognition-api-container -p 8000:8000 face-recognition-api
