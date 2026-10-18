# lowcode-project

A minimal Flask 3 web application in a single file, `app.py`.

## What it does

The app defines one route, `/`. A request to it returns a small static HTML page titled "Hello", with a single heading:

> **Hello from Claude**

There are no other routes, templates, static files, database or configuration. Running `python app.py` starts Flask's built-in development server with debug mode on, so it reloads automatically when you edit the code and shows the interactive debugger on errors.

## Requirements

- Windows with [Git Bash](https://git-scm.com/downloads/win)
- Python 3.9 or newer on your `PATH` (Flask 3.1's minimum)

Dependencies are pinned in `requirements.txt`:

| Package | Version |
| --- | --- |
| Flask | 3.1.3 |
| Werkzeug | 3.1.9 |
| Jinja2 | 3.1.6 |
| MarkupSafe | 3.0.4 |
| itsdangerous | 2.2.0 |
| click | 8.5.0 |
| blinker | 1.9.0 |

## Installation

Open Git Bash in the project folder (`C:\Users\david\lowcode-project`) and run:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

The first command creates a virtual environment in `.venv`, the second activates it in the current Git Bash session (your prompt shows `(.venv)`), and the third installs the pinned dependencies into it.

## Running the app

With the virtual environment active, run:

```bash
python app.py
```

Then open <http://127.0.0.1:5000/> in your browser. You should see the heading "Hello from Claude".

Press `Ctrl+C` in Git Bash to stop the server. In a new Git Bash session, run `source .venv/Scripts/activate` again before `python app.py`. To leave the virtual environment, run `deactivate`.

> Debug mode and the built-in server are for local development only. Don't expose this server to a network or use it in production.

## Project layout

```
app.py            # the Flask application
requirements.txt  # pinned dependencies
README.md         # this file
```

## Project Idea 
Talent Lens would help talent acquisition and employer branding teams understand how their organisations appear in AI responses during a candidate’s job search. Inspired by my digital marketing background and conversations with employer branding teams, it would explore how candidates discover employers, research workplaces and compare career opportunities using AI.

Users would create candidate profiles covering skills, experience, location and career goals. The application would generate realistic questions for each profile, send them to an AI platform through its API and store the responses. A dashboard would show which employers are mentioned, how they are described and which sources are cited.

The first version would focus on one candidate profile, one AI platform and a small set of competitors. Users could compare results and identify gaps in their employer content. Later versions could support follow-up questions, additional platforms and recommendations for improving visibility across the entire candidate journey over time.