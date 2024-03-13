from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app= FastAPI()
oauth2=OAuth2PasswordBearer(tokenUrl="login")
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,
        "password": "654321"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

##########revicion de diccionarios 
async def current_user(token:str=Depends(oauth2)):
  c
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm=Depends()):
    user_db=users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="usuario no encontrado")
    
    user= search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400,detail="usuario no encontrado")
    
    return {"access_token":user.username, "token_type" : "bearer"}




@app.get("/users/me")
async def me(user : User= Depends(current_user)):
    return user


    
    
    


    

    

