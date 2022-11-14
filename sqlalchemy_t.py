from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+aiomysql://skf:123456@localhost:3306/spiders", echo=True)
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

class book(Base):
    __tablename__ = "spa5"
    name = Column(String(20), primary_key=True, nullable=False, comment="书名")
    introduction = Column(String(20), default=None,  comment="书籍简介")

    def __repr__(self):
        name = self.name
        introduction = self.introdution
        return f"Book: name: {name}, introduction: {Phone}"
   

Base.metadata.create_all(engine)
NewBook = book(name="python", introduction="ss")
session.add(NewBook)
session.commit()	# 需要调用commit()方法提交事务。
