from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

def create_app():
    # instantiate the app
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from project.queries import queries_router
    app.include_router(queries_router)

    @app.middleware("http")
    async def add_no_cache_header(request, call_next):
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response

    @app.get("/")
    async def root(request: Request):
        return JSONResponse(content={"data": "Welcome to the API!"}, status_code=200)

    return app
