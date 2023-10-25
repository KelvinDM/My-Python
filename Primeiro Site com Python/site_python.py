from flask import Flask, render_template

app = Flask(__name__)
#criar a 1 pagina do site
#route -> kelvinho.com/ é oque vem depois do barra
#template
@app.route("/")
#função -> oque você quer exibir naquela página
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
        return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>") #passo 1 colocar <>
def usuarios(nome_usuario): #passo 2 passar o nome_usuario dentro da função usuarios
    return render_template("usuarios.html", nome_usuario = nome_usuario) #passo 3 passar ele na variavel


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # Servidor do heroku

