from routes.singer_routes import singer_route
from fastapi import FastAPI
from config.db import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
#Returns a FASTAPI app
def get_application() -> FastAPI:
    # Crate the database
    Base.metadata.create_all(bind=engine)
    #Fastapi  version details
    app = FastAPI(
        title="API Music_Store",
        version="1.0.0",
        docs_url="/"
    )
    #add a CORS middlewre
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(singer_route,prefix="/music-store/api/v1")
    return app

app = get_application()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5555
    )