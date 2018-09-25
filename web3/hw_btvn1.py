from flask import Flask, render_template, request
from New_post import Post
import mlab
app = Flask(__name__)
mlab.connect()
ps = [
    {

    },
]
@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("hw_btvn.html")
    elif request.method == "POST":
        #1. get form & extract data
        form = request.form
        name = form["name"]
        email = form["email"]
        log_in = form["log_in"]
        password = form["password"]
        print(name, email, log_in, password)
        #2. add new post
        new_post = {
            "name": name,
            "email": email,
            "log_in": log_in,
            "password": password
        }
        ps.append(new_post)
        new_post = Post(name=name, email=email, log_in=log_in, password=password)
        new_post.save()
        return "ok"

if __name__=="__main__":
    app.run(debug=True)