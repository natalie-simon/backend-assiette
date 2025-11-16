import bcrypt
from sqlalchemy.orm import Session
from database import DBUser, DBRole
from users.models import UserCreate
from typing import Optional

def create_user(db: Session, user: UserCreate) -> DBUser:
    """Création d'un nouvel utilisateur dans la base de données. Et création du hash du mot de passe."""
    hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'),
        bcrypt.gensalt()
        ).decode('utf-8')
    db_user = DBUser(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )

    user_role = db.query(DBRole).filter(DBRole.name == "user").first()
    if user_role:
        db_user.roles.append(user_role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_by_email(db: Session, email: str) -> Optional[DBUser]:
    """Récupération d'un utilisateur par son email."""
    return db.query(DBUser).filter(DBUser.email == email).first()