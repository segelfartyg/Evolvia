from flask import Flask
from flask import render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/start/")
@app.route("/start/<name>")
def Start(name=None):
    return render_template("index.html", name=name)


@app.route("/goals/")
def Goals(name=None):
    return render_template("goals.html")

@app.route("/calendar/")
def Cal(name=None):
    return render_template("calendar.html")








