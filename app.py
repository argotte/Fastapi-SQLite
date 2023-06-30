from routes.singer_routes import singer_route
from routes.album_routes import album_route
from fastapi import FastAPI,responses
from config.db import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
#Returns a FASTAPI app
def get_application() -> FastAPI:
    # Crate the database
    Base.metadata.create_all(bind=engine)
    #Fastapi  version details
    app = FastAPI(
        title="Music_Store API by Diego Argotte",
        description="Feel free to use this FastAPI template for your projects\n\n"
                    "https://github.com/argotte",
        version="0.0.1",
        contact={
            "name": "Diego Argotte",
            "url": "https://www.linkedin.com/in/diego-argotte-2a82441a8/",
        },
        docs_url="/docs"
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
    app.include_router(album_route,prefix="/music-store/api/v1")
    return app

    
app = get_application()

#redirect from / to /docs
@app.get("/", include_in_schema=False)
async def docs_redirect():
    return responses.RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000,
    )