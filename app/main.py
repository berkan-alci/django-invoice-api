import uvicorn
from fastapi import FastAPI
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)


@app.get('/')
def root_redirect():
    return RedirectResponse("/api/v1")


@app.get('/api/v1')
def root():
    return {"message": "use www.examplehost.com/docs for documentation regarding the API."}
