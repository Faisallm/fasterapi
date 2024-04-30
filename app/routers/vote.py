from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/votes",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), 
         current_user: int =  Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {vote.post_id} does not exist.")
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, 
                                     models.Vote.user_id == current_user.id)
    # check to see if user have voted on post before
    found_vote = vote_query.first()

    if(vote.dir == 1):
        if found_vote:
            # the user has already voted on this post.
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted on post \
                                {vote.post_id}")
        else:
            # create vote
            new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
            db.add(new_vote)
            db.commit()
            return {"message": "successfully added vote"}
       
    else:
        if not found_vote:
            # you are trying to delete a post that does not exist.
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Vote does not exist')
        else:
            vote_query.delete(synchronize_session=False)
            db.commit()
            return {'message': "successfully deleted vote"}
