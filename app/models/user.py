from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # 사용자의 이름
    email = Column(String, unique=True, index=True, nullable=False)  # 사용자의 이메일
    password = Column(String, nullable=False)  # 사용자의 비밀번호

    played_the_games = relationship("GameLog", back_populates="user")
