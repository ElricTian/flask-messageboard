from models import User, db


class UserDB(object):

    @staticmethod
    def search_user(username, password):
        # 检查用户登录
        results = User.query.filter(User.name == username, User.password == password)
        if results:
            for result in results:
                message = result.name
                return message
        else:
            return None

    @staticmethod
    def rechecking(username):
        # 检查是否注册过
        results = User.query.filter(User.name == username).all()

        if results:
            return 1
        else:
            return None

    @staticmethod
    def reg_user(name, password):
        # 注册
        user = User()
        user.name = name
        user.password = password

        db.session.add(user)
        db.session.commit()
        return 1

    @staticmethod
    def save_img(username, img_path):
        # 存储图片路径
        user = User.query.filter(User.name == username).first()
        user.img = img_path
        db.session.commit()
        return 1

    @staticmethod
    def show_info(username):
        # 关联查询
        sql = "SELECT  user.img, user.hobby, user.age, message.content, message.time " \
              "FROM user " \
              "LEFT JOIN message " \
              "ON user.name=message.name WHERE user.name='%s'" % username

        results = db.session.execute(sql)

        return list(results)
