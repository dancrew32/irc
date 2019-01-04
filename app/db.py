import os
from pony import orm

db = orm.Database()
db.bind(
    provider='postgres',
    user=os.environ['IRC_DB_USER'],
    password=os.environ['IRC_DB_PASSWORD'],
    host='db',
    database=os.environ['IRC_DB_NAME'])


class Message(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    who = orm.Required(str, index=True)
    command = orm.Required(str)
    channel = orm.Required(str, index=True)
    text = orm.Required(str)


@orm.db_session
def add_message(message):
    print(message)
    Message(
        who=message.who,
        command=message.command,
        channel=message.channel,
        text=message.text)


db.generate_mapping(create_tables=True)
