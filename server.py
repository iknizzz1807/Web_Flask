from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def empty():
    return redirect(url_for("login"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/rain")
def rain():
    return render_template("rain.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        g = open("data.txt", "r")
        string = g.readlines()[0]
        check = string.split()
        g.close()
        f = open("data.txt", "a")
        yname = request.form.get("yourname", "")
        user = request.form.get("username", "")
        passwd = request.form.get("password", "")
        repasswd = request.form.get("retype_password", "")
        if not yname:
            return render_template("login_cases.html", case  = "Please type your name!", goto = "GoBackSignUp", login_status = "Sign up failed")
        else:
            if not user:
                if not passwd:
                    return render_template("login_cases.html", case  = "Missing username and password!", goto = "GoBackSignUp", login_status = "Sign up failed")
                else:
                    return render_template("login_cases.html", case  = "Missing username!", goto = "GoBackSignUp", login_status = "Sign up failed")
        if not passwd:
            if not user:
                return render_template("login_cases.html", case  = "Missing username and password!", goto = "GoBackSignUp", login_status = "Sign up failed")
            else:
                return render_template("login_cases.html", case  = "Missing password!", goto = "GoBackSignUp", login_status = "Sign up failed")
        if passwd != repasswd:
            return render_template("login_cases.html", case  = "Please type the same password!", goto = "GoBackSignUp", login_status = "Sign up failed")
        else:
            for i in range(0, len(check), 3):
                if user == check[i]:
                    return render_template("login_cases.html", case  = "Username existed!", goto = "GoBackSignUp", login_status = "Sign up failed")
                elif (i == (len(check) - 3)) and (user != check[i]):
                    f.write(user + " ")
                    f.write(passwd + " ")
                    f.write(yname + " ")
                    f.close()
                    return render_template("home.html", nameofuser = yname)
    else:
        return render_template("signup.html")
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "")
        passwd = request.form.get("password", "")
        g = open("data.txt", "r")
        string = g.readlines()[0]
        check = string.split()
        if not user:
            if not passwd:
                return render_template("login_cases.html", case  = "Missing username and password!", goto = "GoBack", login_status = "Login failed")
            else:
                return render_template("login_cases.html", case  = "Missing username!", goto = "GoBack", login_status = "Login failed")
        if not passwd:
            if not user:
                return render_template("login_cases.html", case  = "Missing username and password!", goto = "GoBack", login_status = "Login failed")
            else:
                return render_template("login_cases.html", case  = "Missing password!", goto = "GoBack", login_status = "Login failed")
        for i in range(0, len(check), 3):
            if user == check[i] and passwd == check[i + 1]:
                return render_template("home.html", nameofuser = check[i + 2])
            elif i == (len(check) - 3) and (user != check[i] or passwd != check[i + 1]):
                return render_template("login_cases.html", case  = "Wrong username and(or) password!", goto = "GoBack", login_status = "Login failed")
    else:
        return render_template("login.html")

app.run(debug=True, port=8080)