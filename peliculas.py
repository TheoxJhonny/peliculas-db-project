from flask import Flask, render_template, request, redirect
from bd import agregar_pelicula, obtener_peliculas, eliminar_pelicula, modificar_pelicula, buscar_pelicula_api


app = Flask(__name__)

@app.route("/")
def index():
    peliculas = obtener_peliculas()
    return render_template("index.html", peliculas=peliculas)

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form["titulo"]

    data = buscar_pelicula_api(titulo)

    if data:
        agregar_pelicula(data["titulo"], int(data["año"]), data["genero"])
    else:
        # Si no existe en la API, agregar manual desde el formulario
        año = int(request.form["año"])
        genero = request.form["genero"]
        agregar_pelicula(titulo, año, genero)

    return redirect("/")

@app.route("/eliminar/<titulo>")
def eliminar(titulo):
    eliminar_pelicula(titulo)
    return redirect("/")

# ====== NUEVO: MOSTRAR FORMULARIO PARA EDITAR ======
@app.route("/editar/<titulo>")
def editar(titulo):
    peliculas = obtener_peliculas()
    pelicula = None
    for p in peliculas:
        if p["titulo"] == titulo:
            pelicula = p
    return render_template("editar.html", pelicula=pelicula)

# ====== NUEVO: GUARDAR CAMBIOS ======
@app.route("/actualizar", methods=["POST"])
def actualizar():
    titulo_original = request.form["titulo_original"]
    nuevo_titulo = request.form["titulo"]
    nuevo_año = int(request.form["año"])
    nuevo_genero = request.form["genero"]

    modificar_pelicula(titulo_original, nuevo_titulo, nuevo_año, nuevo_genero)
    return redirect("/")

if __name__ == "__main__":
   app.run(debug=True)
