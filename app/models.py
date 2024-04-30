from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

# nullable=False indicates that field can't be left blank.

class Post(Base):
    # the table of our posts.
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=text("now()"))
    
    # oneToMany Relationship
    # a user can create multiple posts
    # while a single post can be associated with only one user
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),
                      nullable=False)
    
    # it figures out the relationship with the User sqlalchemy class.
    # it doesn't store this to the database.
    # monkey-patching
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text("now()"))


class Vote(Base):
    __tablename__ = "votes"

    # manyToOne relationship,
    # a user can vote multiple times
    # while a vote has only one user
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), 
                     primary_key=True)
    
    # a post can have multiple votes
    # while each vote is only associated with one post
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), 
                     primary_key=True)
    
    # two or more sets of ForeignKey in a table creates a composite key.
    