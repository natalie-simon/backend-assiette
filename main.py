from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from users.models import User, UserCreate, UserLogin
from auth import create_access_token
import users.crud as crud


app = FastAPI(title="Backend Service Mon Assiette", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur le service backend Mon Assiette!"}

@app.post("/register", response_model = User)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cette email est déjà utilisée.",
        )

    new_user = crud.create_user(db, user)

    return User(
        username=new_user.username,
        email=new_user.email,
        #full_name=new_user.full_name,
        disabled=not new_user.is_active,
    )

@app.post("/login", response_model=dict)
async def login_user(user_login: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_login.email)
    if not db_user or not crud.check_user_password(db_user, user_login):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect.",
        )

    access_token = create_access_token(data={
        "username": db_user.username,
        "email": db_user.email,
        "disabled": not db_user.is_active
    })
    return access_token 

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)
    return None