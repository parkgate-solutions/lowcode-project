# Goodfolk contact form (Flask)

This version uses Python and Flask, so Node.js and npm are not needed. It serves the form at `/contact`, validates all fields on the server, and does not save submissions.

## Run in Git Bash on Windows

```bash
cd /c/Users/david/lowcode-project/experiments/week02/gemini
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000/contact](http://127.0.0.1:5000/contact). Leave Git Bash open while the server is running. Press `Ctrl+C` to stop it. If you already have this folder's `.venv` activated, skip the `venv` creation and activation lines.
