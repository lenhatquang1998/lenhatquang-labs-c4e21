import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds013559.mlab.com:13559/c421-blog

host = "ds013559.mlab.com"
port = 13559
db_name = "c421-blog"
user_name = "nhatquang98"
password = "quang1234"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())