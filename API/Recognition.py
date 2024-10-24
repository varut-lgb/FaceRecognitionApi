import os
from google.cloud import storage
import face_recognition

class FaceRecognition:
    def __init__(self):

        # เตรียม google storage
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "API/logisboy-2d68bc776d5b.json"
        self.client = storage.Client()
        self.bucket_name = 'nhealth-storage-dev' 

        # เตรียมรูปและชื่อ
        self.known_face_encodings = []
        self.known_face_names = []

        # เรียกใช้ load_images_blob 
        self.load_images_blob()

    def download_blob(self, source_blob_name):
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(source_blob_name)
        file_name = os.path.basename(source_blob_name)

        # สร้างไฟล์ชั่วคราว
        temp_file = f'{file_name}'
        blob.download_to_filename(temp_file)
        print(f"Downloaded {source_blob_name} to {temp_file}.")
        return temp_file

    # เอารูปจาก google มาเก็บเข้าเตรียมเอาไปอ่าน
    def load_images_blob(self):
        bucket = self.client.bucket(self.bucket_name)
        blobs = bucket.list_blobs(prefix='Master/Upload_File/Tansporter/Profile_Image/')
        # เก็บชื่อไฟล์ที่เป็น jpg
        self.image_files = [blob.name for blob in blobs if blob.name.endswith('.jpg')]

        # loop เพื่อเก็บข้อมูลลงใน known_face_encodings และ known_face_names
        for file_name in self.image_files:
            temp_file = self.download_blob(file_name)
            image = face_recognition.load_image_file(temp_file)
            encoding = face_recognition.face_encodings(image)

            if encoding:
                self.known_face_encodings.append(encoding[0])
                self.known_face_names.append(os.path.splitext(temp_file)[0])
            # ลบไฟล์ชั่วคราวหลังจากโหลด
            os.remove(temp_file)


    # โมดูลสำหรับเปรียบเทียบใบหน้า
    def recognize_face(self, image):
        unknown_encoding = face_recognition.face_encodings(image)

        if unknown_encoding:
            results = face_recognition.compare_faces(self.known_face_encodings, unknown_encoding[0], 0.4)
            distances = face_recognition.face_distance(self.known_face_encodings, unknown_encoding[0])
            matches = []
            for i, match in enumerate(results):
                if match:
                    matches.append({'name':self.known_face_names[i], 'distance':distances[i]})
            return matches
        return []

if __name__ == "__main__":
    face_recog = FaceRecognition()

    # ตรวจสอบใบหน้า
    test_image = face_recognition.load_image_file("../TestPics/GVTpoyaaYAA9pcS.jpg")
    recognized_names = face_recog.recognize_face(test_image)
    print(f"Recognized names: {recognized_names}")