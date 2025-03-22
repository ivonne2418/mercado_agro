from flask import Flask, render_template, url_for
import os

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/")
def index():
    diagrams_path = os.path.join(app.static_folder, "diagrams")

    if not os.path.exists(diagrams_path):
        return "La carpeta 'diagrams' no existe en la ruta esperada.", 404

    files = os.listdir(diagrams_path)
    images = [url_for('static', filename=f"diagrams/{file}") for file in files]

    return render_template("mercado_agro.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)