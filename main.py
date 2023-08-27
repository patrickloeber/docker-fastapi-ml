import io

from model_pipeline import pipeline
from PIL import Image

from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()

 
class ModelOutput(BaseModel):
    answer: str


@app.get("/")
def read_root():
    return {"Hello": "Wooorld11"}


@app.post("/ask", response_model=ModelOutput)
async def ask(file: UploadFile, text: str):    
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    output = pipeline(image, text)
    return {"answer": output}
