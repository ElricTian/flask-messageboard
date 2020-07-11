from redis import Redis
from datetime import timedelta

class Dev(object):
    # 如果不更改ENV(开发环境) 默认是production产品模式

    # 生产模式
    ENV = 'developement'
    # session密钥
    SECRET_KEY = 'ElricTian'
    # 静态文件缓存时间
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    # 配置session
    """Redis默认的配置会生成db0~db15共16个db，切分出16个db的一个作用是方便不同项目使用不同的db，防止的数据混淆，也为了方便数据查看"""
    CONFIG = {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 15
    }
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(**CONFIG)

    # 配置sqlalchemy
    # 连接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/message_board'
    # 可扩展
    SQLALCHEMY_TRACK_MODIFICATION = True
    # 回收资源时自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 显示调试SQL
    SQLALCHEMY_ECHO = True
