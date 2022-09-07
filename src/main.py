from fastapi import FastAPI
from routers import users, cities, picnics

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(cities.router)
app.include_router(picnics.router)


@app.get("/")
def root():
    return {"message": "Picnic WebApp"}
