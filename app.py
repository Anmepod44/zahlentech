from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static files.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory.
templates = Jinja2Templates(directory="templates")


# Level one nesting of the endpoint
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get("/products")
def read_products(request: Request):
    return templates.TemplateResponse('product.html', {'request': request})

@app.get("/about")
def read_about(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get("/mordern")
def get_modern(request: Request):
    return templates.TemplateResponse('mordern.html', {'request': request})


# Level two nesting of the ndpoint    

@app.get("/mordern/kick")
def get_modern(request: Request):
    return {"kick":"hard"}
    # return templates.TemplateResponse('mordern.html', {'request': request})
