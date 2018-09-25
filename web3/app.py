from flask import Flask, render_template, request, redirect, url_for
import mlab
from post import Post
app = Flask(__name__)
mlab.connect()
p = {
    "title": "C4E21",
    "content": "module web, sap hackathon",
    "author": "quan",
    "date": "2018/09/02",
}

@app.route("/post/<post_id>")
def post(post_id):
    post = Post.objects().with_id(post_id)
    return render_template("post.html",post=post )

@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = Post.objects().with_id(post_id)
    if post is None:
        print("post not found")
    else:
        post.delete()
    return redirect("/posts")

@app.route("/update/<post_id>", methods=["GET", "POST"])
def update_post(post_id):
    p = Post.objects().with_id(post_id)
    if request.method == "GET":
        return render_template("update_post.html", post=p)
    elif request.method == "POST":
        form = request.form
        title = form["title"]
        author = form["author"]
        content = form["content"]

        p.update(set__title="title", set__author="author", set__content="content")
    

@app.route("/posts")
def posts():
    all_post = Post.objects()
    return render_template("posts.html", posts=all_post)

@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        #1. get form & extract data
        form = request.form
        title = form["title"]
        author = form["author"]
        content = form["content"]
        print(title,author,content)
        

        #2. add new post
        # new_post = {
        #     "title": title,
        #     "author": author,
        #     "content": content,
        # }
        # ps.append(new_post)
        new_post = Post(title=title, author=author, content=content,likes=0)
        new_post.save()
        
        # return redirect("/posts")      # chuyển về đường dẫn cũ
        return redirect(url_for("posts"))  # chuyển về đường cũ theo def
if __name__=="__main__":
    app.run(debug=True)