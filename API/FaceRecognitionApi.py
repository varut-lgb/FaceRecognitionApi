from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import face_recognition
from .Recognition import FaceRecognition

app = FastAPI()
face_recog = FaceRecognition()

@app.post("/recognize/")
async def recognize_face(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = face_recognition.load_image_file(file.file)
        recognized = face_recog.recognize_face(image)

        if recognized:
            return JSONResponse(content={"status": "success","recognized": recognized})
        else:
            return JSONResponse(content={"status": "failure","recognized": recognized})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)