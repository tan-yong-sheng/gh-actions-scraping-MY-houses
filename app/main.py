from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()
templates = Jinja2Templates(directory="./app/templates")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/", response_class=HTMLResponse)
async def hello(request: Request):
   return templates.TemplateResponse("hello.html", {"request": request})

if __name__=='__main__':
    uvicorn.run('app.main:app', reload=True)