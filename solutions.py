# from fastapi import APIRouter, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse

# router = APIRouter()

# # Set up templates directory.
# templates = Jinja2Templates(directory="templates")

# @router.get("/")
# def solutions_home():
#     return {"message": "welcome to the solutions endpoint"}

# @router.get("/mordern")
# def get_modern(request: Request):
#     return templates.TemplateResponse('mordern.html', {'request': request})
