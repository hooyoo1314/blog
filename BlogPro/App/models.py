from App.exts import db


# # 分类
# class Person(db.Model):
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     name = db.Column(db.String(20), unique=True)
#     age = db.Column(db.Integer, default=18)



class Catalog(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    category=db.Column(db.String(200))
    catename=db.Column(db.String(200))
    keypassword = db.Column(db.String(20))
    said = db.Column(db.String(200))
    articles = db.relationship('Article',backref='my_catalog',lazy=True)

class Article(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    title=db.Column(db.String(20),unique=True)
    detail=db.Column(db.String(2000))
    catalogid = db.Column(db.Integer,db.ForeignKey(Catalog.id))

class User(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(20))