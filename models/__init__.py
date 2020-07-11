from flask_sqlalchemy import SQLAlchemy

# 创建数据库对象
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    img = db.Column(db.String(255))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    content = db.Column(db.String(255))
    time = db.Column(db.TIMESTAMP,
                     nullable=False,
                     comment='更新时间戳',
                     server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


