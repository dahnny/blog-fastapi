from .. import schemas, models, utils
from fastapi import  status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router= APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash_password(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Failed to create user")
    return new_user

@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id {user_id} not found")
    return user