from models import Message, db


class MessageDB(object):

    @staticmethod
    def save_message(name, content):
        message = Message()
        message.name = name
        message.content = content

        db.session.add(message)
        db.session.commit()
        return 1

