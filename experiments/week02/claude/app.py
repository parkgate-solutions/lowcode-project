import os
import re
import secrets

from flask import Flask, abort, render_template, request, session

app = Flask(__name__)
# Set FLASK_SECRET_KEY in production; the random fallback resets sessions on restart.
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)

# Pragmatic check: one "@", no spaces, and a dot in the domain part.
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MAX_LENGTHS = {"name": 100, "email": 254, "message": 5000}


@app.route("/")
def index():
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hello</title>
</head>
<body>
  <h1>Hello from Claude</h1>
</body>
</html>"""


def csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_urlsafe(32)
    return session["csrf_token"]


app.jinja_env.globals["csrf_token"] = csrf_token


def validate_contact(form):
    data = {field: form.get(field, "").strip() for field in MAX_LENGTHS}
    errors = {}
    for field, value in data.items():
        if not value:
            errors[field] = f"{field.capitalize()} is required."
        elif len(value) > MAX_LENGTHS[field]:
            errors[field] = f"{field.capitalize()} must be at most {MAX_LENGTHS[field]} characters."
    if "email" not in errors and not EMAIL_RE.match(data["email"]):
        errors["email"] = "Enter a valid email address."
    return data, errors


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", data={}, errors={})

    token = request.form.get("csrf_token", "")
    expected = session.get("csrf_token", "")
    if not expected or not secrets.compare_digest(token.encode(), expected.encode()):
        abort(400, description="Invalid or missing form token. Reload the page and try again.")

    data, errors = validate_contact(request.form)
    if errors:
        return render_template("contact.html", data=data, errors=errors), 400

    # Submissions are deliberately not stored, logged or forwarded.
    return render_template("contact.html", sent=True, data=data)


if __name__ == "__main__":
    app.run(debug=True)
