from sqlalchemy import Column, Integer, String, func, desc
from database import Base, engine, SessionLocal

class User(Base):

    __tablename__ = "user"
   # __table_args__ == { "schema" : "public"}
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":

    Base.metadata.create_all(engine)
    session = SessionLocal()

    s = session.query(User.country, User.os, func.count(User.id)).filter(
        User.exp_group == 3).group_by(
        User.country, User.os).order_by(
        desc(func.count(User.id))).having(
        func.count(User.id) > 100).all()
    print(s)


