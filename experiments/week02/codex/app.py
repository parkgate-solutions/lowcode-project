import re

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]+@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}$"
)


def valid_email(value):
    if len(value) > 254 or not EMAIL_PATTERN.fullmatch(value):
        return False
    local = value.rsplit("@", 1)[0]
    return len(local) <= 64 and not local.startswith(".") and not local.endswith(".") and ".." not in local


@app.route("/")
def index():
    return redirect(url_for("contact"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    values = {"name": "", "email": "", "message": ""}
    errors = {}

    if request.method == "POST":
        values = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "message": request.form.get("message", "").strip(),
        }
        if not values["name"]:
            errors["name"] = "Please enter your name."
        if not values["email"]:
            errors["email"] = "Please enter your email address."
        elif not valid_email(values["email"]):
            errors["email"] = "Enter a valid email address, such as you@example.com."
        if not values["message"]:
            errors["message"] = "Please enter a message."

        if not errors:
            # The submission is intentionally not stored.
            return redirect(url_for("success"))

    return render_template("contact.html", values=values, errors=errors), (400 if errors else 200)


@app.route("/contact/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
