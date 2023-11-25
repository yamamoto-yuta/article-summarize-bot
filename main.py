# main.py
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/echo")
def echo():
    return JSONResponse(content={
        "text": "echo"
    })
