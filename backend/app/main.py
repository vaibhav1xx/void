#Importing FastAPI
from fastapi import FastAPI
#Importing the function 
from app.startup import startup
#Importing Version Information
from app.version import (
    APP_NAME,
    FULL_NAME,
    VERSION,
    CODENAME,
    STATUS,
)
#Creating the Application
app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description=FULL_NAME,
)
#Creating First Route
@app.get("/") #decorator
def root(): #/ is called the root endpoint
    return {
        "project": APP_NAME,
        "version": VERSION,
        "codename": CODENAME,
        "status": STATUS, 
        "message": "System Online. Awaiting Instructions."
     }
#Startup execute 
@app.on_event("startup")
def on_startup():
    startup()
#Health Showcase
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": APP_NAME,
        "version": VERSION,
    }
#connecting route/chat file 
from app.routes.chat import router as chat_router

app.include_router(chat_router)