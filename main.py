from fastapi import FastAPI, Form, Request, status, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

import pandas as pd
import model


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    print('Request for index page received')
    return templates.TemplateResponse('index.html', {"request": request})

@app.get('/favicon.ico')
async def favicon():
    file_name = 'favicon.ico'
    file_path = './static/' + file_name
    return FileResponse(path=file_path, headers={'mimetype': 'image/vnd.microsoft.icon'})


@app.post('/upload')
async def upload(request: Request, file: UploadFile = File(...)):
    f = file.file
    df = pd.read_csv(f)
    f.close()
    df_predict = df.drop(labels=["From", "To"], axis=1)
    y = model.predict(df_predict.values)
    df.insert(len(df.columns), "Fraud", y)
    context = {'request': request, 'table': df.loc[df.Fraud == 1., :].to_html()}
    return templates.TemplateResponse('results.html', context)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

