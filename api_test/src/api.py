from fastapi import FastAPI 
from src.test import Adder
from fastapi.middleware.cors import CORSMiddleware
import faulthandler
import json

app = FastAPI(title="cool project")
faulthandler.enable()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    adder = Adder()
    resources = {
        "Title": "Sam is super awesome generally",
        "Count": adder.count
    }
    return resources 

@app.get("/awesome")
def awesome():
    resources = {
        "Title": "Sam is super awesome all the time"
    }
    return resources 