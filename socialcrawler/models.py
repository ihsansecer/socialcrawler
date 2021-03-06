import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    BigInteger,
    Text,
    DateTime,
    Boolean,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class TwitterUser(Base):
    __tablename__ = "twitter_user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=False)
    screen_name = Column(String(50), nullable=False)
    match_ratio = Column(Integer)
    match_name = Column(String(150))
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    lang = Column(String(5), nullable=False)


class TwitterConnection(Base):
    __tablename__ = "twitter_connection"

    id = Column(Integer, primary_key=True)
    from_user_id = Column(ForeignKey("twitter_user.id"))
    from_user = relationship("TwitterUser", foreign_keys=[from_user_id])
    to_user_id = Column(ForeignKey("twitter_user.id"))
    to_user = relationship("TwitterUser", foreign_keys=[to_user_id])
    formation = Column(JSONB)


class TwitterConnectionChange(Base):
    __tablename__ = "twitter_connection_change"

    id = Column(Integer, primary_key=True)
    is_added = Column(Boolean, nullable=False)
    connection_id = Column(ForeignKey("twitter_connection.id"), nullable=False)
    connection = relationship(
        "TwitterConnection", foreign_keys=[connection_id]
    )
    created_at = Column(
        DateTime, default=datetime.datetime.utcnow, nullable=False
    )


class TwitterEntry(Base):
    __tablename__ = "twitter_entry"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("twitter_user.id"))
    user = relationship("TwitterUser", foreign_keys=[user_id])
    text = Column(String(280))
