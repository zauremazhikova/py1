
import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
const_url = "https://api.quotable.io/random"


def get_info_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()

        return result
    else:
        return {
            'OOPS'
        }


@app.get('/')
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/quote')
def read_root(request: Request):
    smart_word = get_info_from_url(const_url)
    return templates.TemplateResponse("info.html", {"request": request, "author": smart_word["author"], "content": smart_word["content"]})

