from flask import Flask, render_template

app = Flask(__name__)
#criar a 1 pagina do site
#route -> kelvinho.com/ é oque vem depois do barra
#template
@app.route("/")
#função -> oque você quer exibir naquela página
def homepage():
    return render_template("index.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # Servidor do heroku

