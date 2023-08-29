from fastapi import Response, status, HTTPException, Depends, APIRouter
import models, schemas, oauth2
from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix='/betting',
    tags=['Match Betting']
)


# 1A-1
# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.MatchBettingOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[
            str] = ""):  # pass in Session as parameter saved as 'db' when using sqlalchemy and fastapi
    # 1A-2
    # posts = db.query(models.Post).filter(
    #     models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # 1A-13
    posts = db.query(models.MatchBetting, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.MatchBetting.id, isouter=True).group_by(models.MatchBetting.id).filter(
        models.MatchBetting.title.contains(search)).limit(limit).offset(skip).all()
    # posts SQL equivalent w/o filter:
    # select posts.*, count(votes.post_id) as votes from posts
    # left join votes on posts.id = votes.post_id
    # group by posts.id;
    return posts  # If I pass in an array like this, FastAPI serializes 'my_posts' converting it into JSON


# 1A-3, 1A-4
# 1A-5, 1A-6
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.MatchBetting)
def create_posts(post: schemas.MatchBettingCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):  # 1A-7
    # 1A-8
    new_post = models.MatchBetting(owner_id=current_user.id,
                                   **post.dict())  # this line does same thing as next 2 lines of comments
    # new_post = models.Post
    # title=post.title, content=post.content, published=post.published)
    db.add(new_post)  # add to database
    db.commit()  # then commit it
    db.refresh(new_post)  # retrieve the new post that was created and store it back under the variable 'new_post'

    return new_post


# 1A-9
@router.get("/{id}", response_model=schemas.MatchBettingOut)  # get post
def get_post(id: int, db: Session = Depends(get_db),
             current_user: int = Depends(oauth2.get_current_user)):
    # 1A-10
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.MatchBetting, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.MatchBetting.id, isouter=True).group_by(models.MatchBetting.id).filter(
        models.MatchBetting.id == id).first()  # now queries votes too

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post


# DELETE single post with post id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    # 1A-11
    post_query = db.query(models.MatchBetting).filter(models.MatchBetting.id == id)
    post = post_query.first()

    if post == None:  # checks if post exists
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    if post.user_id != current_user.id:  # checks if owner of the post is the user logged in user
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# PUT, updates single post by id
@router.put("/{id}", response_model=schemas.MatchBetting)
def update_post(id: int, updated_post: schemas.MatchBettingCreate, db: Session = Depends(get_db),
                current_user: int = Depends(
                    oauth2.get_current_user)):  # 'post: Post' makes sures the request comes in with the right schema
    # 1A-12
    post_query = db.query(models.MatchBetting).filter(models.MatchBetting.id == id)
    post = post_query.first()

    if post == None:  # if index doesnt exist, this sends an error code to the user stating the reason
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    if post.user_id != current_user.id:  # checks if owner of the post is the user logged in user
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()