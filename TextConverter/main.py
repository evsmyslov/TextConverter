from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert_text(text: str = Form(...), mode: str = Form(...)):
    if mode == "upper":
        return JSONResponse({"result": text.upper()})
    elif mode == "lower":
        return JSONResponse({"result": text.lower()})
    return JSONResponse({"result": text})
