from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('/', response_model=List[schemas.PostBase])
def get_posts(db: Session = Depends(get_db)):
    post_query = db.query(models.Post).all()

    return post_query

@router.get('/{id}', response_model=schemas.PostBase)
def get_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id).first()

    if not post_query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )
    
    return post_query

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostBase)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    
    if (post.title is None) or (post.content is None):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Title and content are required"
        )
    if (not post.title.strip()) or (not post.content.strip()):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Title and content cannot be empty"
        )
        
    created_post = models.Post(**post.model_dump())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)

    return created_post


@router.put('/{id}', response_model=schemas.PostBase)
def update_post(id: int, post: schemas.CreatePost, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    if not post_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )
    
    post_query.update(post.model_dump(exclude={'id', 'created_at'}), synchronize_session=False)
    db.commit()
    return post_query.first()

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return None