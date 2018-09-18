from flask import Flask, render_template, request
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

ps = [
    {
        "title": "C4E21",
        "content": "module web, sap hackathon",
        "author": "quan",
        "date": "2018/09/02",
    },
    {
        "title": "c4e21-hachathon",
        "content": "5 gio code,hoan thien san pham",
        "author": "huy",
        "date": "2018/09/04",
    },
    {
        "title": "c4e21-demo",
        "content": "2 p trinh bay,15p hoi dap, san pham san sang",
        "author": "manh",
        "date": "2018/09/04",
    }
]

@app.route("/post")
def post():
    return render_template("dict.html",post=p )

@app.route("/posts")
def posts():
    return render_template("dicts.html", posts=ps)

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
        return "ok"

if __name__=="__main__":
    app.run(debug=True)