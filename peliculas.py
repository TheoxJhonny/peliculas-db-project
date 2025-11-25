from flask import Flask, render_template, request, redirect
from bd import agregar_pelicula, obtener_peliculas, eliminar_pelicula

app = Flask(__name__)

@app.route("/")
def index():
    peliculas = obtener_peliculas()
    return render_template("index.html", peliculas=peliculas)

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form["titulo"]
    año = int(request.form["año"])
    genero = request.form["genero"]

    agregar_pelicula(titulo, año, genero)
    return redirect("/")

@app.route("/eliminar/<titulo>")
def eliminar(titulo):
    eliminar_pelicula(titulo)
    return redirect("/")

if __name__ == "__main__":
   obtener_peliculas.run(debug=True)
