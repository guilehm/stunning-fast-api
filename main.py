from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates

import models
from database import engine

templates = Jinja2Templates(directory='templates')

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
    })


@app.post('/stock')
def create_stock():
    return {
        'code': 'success',
        'message': 'stock created',
    }
