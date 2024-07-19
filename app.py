from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from routes.rutasAPI import rutas

app = FastAPI()
app.include_router(rutas)