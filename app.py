
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@aplicación.route("/robots.txt")
def robots():
    contenido = "User-agent: *\nAllow: /\n"
    return Respuesta(contenido, mimetype="text/plain")
if __name__ == "__main__":
    app.run(debug=True)
  
