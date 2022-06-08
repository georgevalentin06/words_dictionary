from flask import Flask, url_for, render_template, redirect, request
import requests as rq

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        word = request.form['searchbar']
        return redirect(url_for('definition', word=word))
    return render_template('index.html')

@app.route("/<word>")
def definition(word):
    response = rq.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()
    try:
        definitions = [definition['meanings'][0]['definitions'][0]['definition'] for definition in data]
    except:
        definitions = ["No definition for this word"]
    return render_template('index.html', definitions=definitions, word=word)

if __name__ == "__main__":
    app.run(debug=True)