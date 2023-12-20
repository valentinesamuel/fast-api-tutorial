from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "Title 1", "content": "Post 1", "published": True, "rating": 5},
    {"title": "Title 2", "content": "Post 2", "published": True, "rating": 4},
    {"title": "Title 3", "content": "Post 3", "published": False, "rating": 3},
    {"title": "Title 4", "content": "Post 4", "published": True, "rating": 2},
    {"title": "Title 5", "content": "Post 5", "published": False, "rating": 1},
]


@app.get("/")
async def root():
    return {"message": "Hello World!!"}

@app.post('/posts')
def createPost(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 100)
    my_posts.append(post_dict)
    return post_dict

@app.get("/posts")
async def getPosts():
    return {"posts": my_posts}


@app.get("/posts/{id}")
async def getPost(id: int):
    post = findPost(id)
    return {'post_detail': post}
