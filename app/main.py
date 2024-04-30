from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .routers import post, user, auth, vote
from .config import settings


# models.Base.metadata.create_all(bind=engine)

# creating an instance
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# in-memory database
my_posts = [{"id": 1, "title": "GaussAI", "content": "AI For Spreadsheets", "rating": 5}, 
            {"id": 2,"title": "PredictAI", "content": "AI For Engineering", "rating": 5},
            {"id": 3,"title": "SemalWiseAI", "content": "AI For Medicine", "rating": 5}]


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

    
@app.get("/")
def root():
    return {"message": "Welcome to my API"}


