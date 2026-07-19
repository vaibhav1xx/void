#Importing FastAPI
from fastapi import FastAPI
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
