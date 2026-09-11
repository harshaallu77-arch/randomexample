# LOGIN PAGE

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("loginpage.html")

@app.route("/login", methods=["POST"])
def login():

    print("WELCOME")

    userName = request.form["username"]
    password = request.form["password"]

    if userName == "258T1a4202" and password == "harsha":
        print("login successful")
        return "LOGIN SUCCESSFUL"

    else:
        print("login failed")
        print("please enter correct user name and password")
        return "LOGIN FAILED"

if __name__ == "__main__":
    app.run(debug=True)