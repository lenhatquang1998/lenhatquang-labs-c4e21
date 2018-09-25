import mlab
from post import Post

#1. connect
mlab.connect()
# #2. create data
# p = Post(title="c4e21", author="quang", content="sap den project roi", likes = 15)
# print(p.title)
# print(p.content)
# print(p.likes)
# print(p.author)
# #3. write data
# p.save()

def test_load_data():
    #2. load all documents
    all_posts = Post.objects()                #lazy loading
    # 3. print all documents
    for post in all_posts:
        
        print(post.title)
        print(post.content)
        print(post.author)
        print("-----------")

def test_load_data(post_id):
    post = Post.objects().with_id(post_id)  # none
    if post == None:
        print("not found")
    else:
        print(post.title)
        print(post.content)
        print(post.author)
# test_load_data("5b9cd15885359d1eaca051ab")
def delete_one_data(post_id):
    #1. retrive document
    post = Post.objects().with_id(post_id)
    #2. delete document
    if post is None:
        print("post not found")
    else:
        post.delete()
delete_one_data("5b9cd15885359d1eaca051ab")

def update_one(post_id):
    #1. retrive document
    post = Post.objects().with_id(post_id)
    #2.update
    #Slug
    post.update(set__title="new title, ahihihi")

update_one("5b9cd30185359d2ac8906d24", "riven quan quan")