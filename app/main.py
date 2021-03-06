from fastapi import FastAPI

from .routers import users, items, auth
from .greeter import greet

app = FastAPI()

app.include_router(auth.router, tags=["auth"])
app.include_router(users.router)
app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
)

print(greet('sam'))







