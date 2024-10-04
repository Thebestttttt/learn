from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files (CSS, รูปภาพ)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates directory
templates = Jinja2Templates(directory="templates")

# Route สำหรับหน้าเว็บหลัก
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
