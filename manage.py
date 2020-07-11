from mainapp import app
from flask_script import Manager

manger = Manager()

if __name__ == '__main__':

    # 以脚本的方式启动flask应用服务
    manager = Manager(app)
    manager.run()





