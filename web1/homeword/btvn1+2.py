from flask import Flask, render_template

new_app = Flask(__name__)
users = {
    "huy" :         {
		"name" : "Nguyen Quang Huy",
		"age" : 29
    },
    "tuananh" : {
		"name" : "Huynh Tuan Anh",
		"age" : 22
    },
    "quang" : {
        "name" : "Le Nhat Quang",
        "age" : 20
    },
}


@new_app.route("/")
def new():
    return "hello"
@new_app.route("/bmi/<int:trongluong>/<int:chieucao>")
def BMI(trongluong,chieucao):
    bmi = trongluong/((chieucao/100)**2)
    if bmi < 16:
        return "thieu can nang"
    elif 16 <= bmi <= 18.5 :
        return "thieu can"
    elif 18.5 < bmi < 25:
        return "binh thuong"
    elif 25 <= bmi <= 30:
        return "thua can"
    else :
        return "beo phi"


#bai 2:
@new_app.route("/user/<username>")
def username(username):
    if username in users.keys():
        return str(users[username])  
    else:
        return "k tim thay"


print("running app")
if __name__ == "__main__":
    new_app.run(debug=True)                          
