from fastapi import FastAPI
from app import routes
from app.database import Base, engine

async def lifespan_handler(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    pass

app = FastAPI(lifespan=lifespan_handler)
app.include_router(routes.router)



