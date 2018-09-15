#1. create a flask app
from flask import Flask, render_template

app = Flask(__name__)
ps = [
        "trong dam gi dep bang sen",
        "la xanh bong trang lai chen nhi vang",
        "nhi vang bong trang la xanh"
    ]

#2. create router
@app.route("/")
def homepage():
    
    return render_template("homepage.html", 
    title = "SU THAT",
    posts = ps)

@app.route("/post/<int:x>")
def post(x):
    post = ps[x]
    return render_template("post_detail.html",post = post)

@app.route("/posts")
def posts():
    cut_ps = []
    for post in ps:
        cut_ps.append(post[0:10])
    return render_template("homepage.html", posts = cut_ps)

@app.route("/quang")
def new():
    return "toi la quang "

@app.route("/hello/<name>")
def hello(name):
    return "hello" + name

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    sum = x + y
    return str(sum)

@app.route("/h1tag")
def h1tag():
    return "<h1>heading 1 - biggg</h1><p>hom nay quang buon</p>"
#3. run app
print("running app")
if __name__ == "__main__":
    app.run(debug=True)                          # chay vinh vien den khi dung lai
