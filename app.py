from typing import Union
from routes.singer_routes import singer as SingerRoute
from fastapi import FastAPI
from config.db import Session, engine, Base
from models.singer_model import Singer as SingerModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

def get_application():
    # crea la base de datos
    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title="API Music_Store",
        version="1.0.0",
        docs_url="/"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(SingerRoute)
    return app

app = get_application()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5555
    )