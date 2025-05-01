from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app =  FastAPI()

@app.get("/")
def hello():
    return {"data":{"name":"Aditya"}}


@app.get("/about")
def about():
    return {"data":"about page"} 

# Dynamic Routing or Dynamic Path Parameter
@app.get("/blog/{id}")
def show(id):  #id here by default is string, to make it int we have to type cast it. ex: def show(id : int):
    #fetch blog with id = id
    return {"data":id}


@app.get("/blogs/unpublished")
def unpublished():
    #fetch blog with id = id
    return {"data":"all unpublished blogs"}


@app.get("/blogs/{id}")
def show_int(id:int):
    #fetch blog with id = id
    return {"data":id}


@app.get("/blog/{id}/comments")
def show_cmts(id):
    #fetch comments of blog with id = id
    return {"data":{'1','2'}}



# Query Parameters
# http://127.0.0.1:8000/blogg?limit=10 >>> like this you can add query parameter

'''
@app.get("/blogg")
def limit(limit):
    return {'data':f'{limit} blogs from db'}
    '''
@app.get("/blogg")
# http://127.0.0.1:8000/blogg?limit=10&published=True >> shall have the query parameter <?limit=10&published=True>
def index(limit,published:bool): #def index(limit=10,published:bool=True):>> This is used to provide the default values to the query parameters.

# if you want to pass some parameter that is optional and you dont have any dafult value then you can set it as Optional.
# for that fiorst you have to : from typing import Optional
#then set it Optional in the function declaration.
# def index(limit=10,published=True,sort=Optional[str]=None):
# here sort is optional of type string and default value is of None type.

    #get only 10 published blogs
    if published:
        return {'data':f"{limit} published blogs from the db"}
    else:
        return {'data':f'{limit} blogs from the db'}
    





# POST METHOD
@app.post("/blog/{id}")
def blog_create(id:int):
    return {'data':f'{id} - blog created.'}


