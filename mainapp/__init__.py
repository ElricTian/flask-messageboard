import settings

from flask import Flask
from models import db, Message
from flask_session import Session


from flask import request, render_template, redirect, url_for, session
from models.UserDB import UserDB
from models.MessageDB import MessageDB


app = Flask(__name__)
app.config.from_object(settings.Dev())

# 创建Session对象
sessions = Session()
sessions.init_app(app)

# 初始化数据库
db.init_app(app)

# 创建表对象
user_db = UserDB()
message_db = MessageDB()


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    # 用户注册
    if request.method == 'POST':
        name = request.form.get('Name')
        password = request.form.get('Password')
        confirm_password = request.form.get('Confirm Password')
        print(name, password)
        if all((name, password, confirm_password)):

            if password != confirm_password:
                tips = '请输入相同的密码'
            else:
                # 查找是否有此用户
                re_result = user_db.rechecking(name)
                if not re_result:
                    reg_result = user_db.reg_user(name, password)
                    if reg_result == 1:
                        # 注册成功自动跳转
                        return redirect(url_for('login'))
                elif re_result == 1:
                    message = '该用户已存在'

        else:
            tips = '请输入注册完整的信息'

    return render_template('register.html', **locals())


@app.route('/login', methods=['GET', 'POST'])
def login():
    register = url_for('user_register')
    if request.method == 'POST':
        # 读取登录用户信息
        name = request.form.get('name')
        password = request.form.get('password')
        user = user_db.search_user(name, password)

        if all((name, password)):
            if not user:
                tips = "请检查用户名或密码是否正确,或前往注册"
            else:
                # 将用户信息加入session
                session['login_user'] = user
                # 返回主页
                return redirect(url_for('index'))
        else:
            tips = '请勿留空白'
    return render_template('login.html', **locals())


@app.route('/logout')
def logout():
    del session['login_user']
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    # 判断是否登录
    if not session.get('login_user'):
            return """请先登录,正在跳转...<meta http-equiv="refresh" content="2;url= %s"/> 
        """ % url_for('login')

    # 当前用户
    user = session.get('login_user')

    if request.method == 'POST':
        content = request.form.get('Content')
        if len(content) == 0:
            tips = '请勿输入空的留言'
        else:
            result = message_db.save_message(name=user, content=content)
            if result == 1:
                tips = '留言成功'

    message_list = Message.query.all()

    return render_template('index.html', **locals())


@app.route('/user')
def user_index():
    user = session.get('login_user')

    result = user_db.show_info(user)
    hobby = result[0].hobby
    age = result[0].age
    img_path = result[0].img
    message_list = result
    return render_template('user.html', **locals())


@app.route('/upload_head', methods=['GET', 'POST'])
def upload_file():
    # 上传头像到本地
    if request.method == 'POST':
        # 上传图片到静态资源里
        file = request.files['file']
        path = r'mainapp/static/photos/user_'
        user = session.get('login_user')
        filename = user + '.jpg'
        file.save(path + filename)

        # 存入路径到数据中

        img_path = 'user_' + filename
        result = user_db.save_img(user, img_path)

        return """上传成功,正在跳转...<meta http-equiv="refresh" content="2;url= %s"/> """ % url_for('user_index')
    return render_template('upload_head.html', **locals())
