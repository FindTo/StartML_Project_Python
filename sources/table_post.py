from sqlalchemy import Column, Integer, String, desc
from database import Base, engine, SessionLocal

class Post(Base):

    __tablename__ = "post"
   # __table_args__ == { "schema" : "public"}
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":

    Base.metadata.create_all(engine)
    session = SessionLocal()
    s = session.query(Post).filter(Post.topic == "business").order_by(desc(Post.id)).limit(10).all()
    k = []
    for x in s:
        k.append(x.id)

    print(k)
    session.commit()