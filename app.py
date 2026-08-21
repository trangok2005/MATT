from flask import Flask, render_template, request, redirect, url_for
from dao import login

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    error = None

    if request.method == "POST":
        email = request.form.get("email")
        pswd = request.form.get("pswd")

        if login(email, pswd):
            return redirect(url_for("index"))

        error = "Tên đăng nhập hoặc mật khẩu sai!"

    return render_template("login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)