import mlab
from post import Post

#1. connect
mlab.connect()
#2. create data
p = Post(title="c4e21", author="quang", content="sap den project roi", likes = 15)
print(p.title)
print(p.content)
print(p.likes)
print(p.author)
#3. write data
p.save()
