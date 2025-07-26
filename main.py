from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import redis 
import os
from pydantic import BaseModel

app = FastAPI();

redis_client =redis.Redis(host=os.getenv('REDIS_HOST','redis'),port=6379)

class StringRequest(BaseModel):
    text:str

@app.get("/")
def home():
  return FileResponse('index.html')



@app.post("/add_string")
def add_value(request:StringRequest):
   data = redis_client.get("concat_data")
   if data:
       data = data.decode()
       data = data + request.text
       redis_client.set("concat_data",data)
       return {
            "message":f"string{request.text} was succesfully concatenated",
            "result": data
            }   
   else:
       redis_client.set("concat_data",request.text)
       return {
           "message":f"string{request.text} was succesfully created",
           "result": request.text
         
       }
   



@app.get("/get_status")
def get_status():
    data:bytes = redis_client.get("concat_data")
    return {
        "data": data.decode()
        
    }








