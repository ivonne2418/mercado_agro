from flask import Flask, render_template, url_for
import os

# Ajusta la ubicación de la carpeta 'static' y 'templates'
app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/")
def index():
    diagrams_path = os.path.join(app.static_folder, "diagrams")  # Ruta correcta en Flask

    # Verifica si la carpeta diagrams existe
    if not os.path.exists(diagrams_path):
        return "La carpeta 'diagrams' no existe en la ruta esperada.", 404

    files = os.listdir(diagrams_path)  # Lista los archivos de imágenes
    images = [url_for('static', filename=f"diagrams/{file}") for file in files]  # Genera rutas accesibles en Flask

    return render_template("mercado_agro.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)