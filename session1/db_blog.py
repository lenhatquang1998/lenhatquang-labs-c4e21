#1. connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://nhatquang98:Lenhatquang1@ds131340.mlab.com:31340/c4e21"

client = MongoClient(uri)
db = client.get_default_database()
#2. select collection
posts = db["posts"]

#3. create document
post = {
    "title": " hôm nay nhiều mưa",
    "content": "tôi vân đi học"
}
#4. insert document
posts.insert_one(post)
# print("done")

post_list = posts.find()
# for post in post_list:                    # post_list ~ collection ~ list
    # print(post['title'])                  # post ~ docoment ~ dictiona

cond = {
    # "title": " hôm nay nhiều mưa",
    # "_id": ObjectId("5b855f3785359d43bc9ca8da")
    "title": {
        "$regex": " hôm nay nhiều",
        "$options": "i",                     # k phân biệt hoa thường
    }
}
post = posts.find_one(cond)                 # tim 1 cai
print(post)