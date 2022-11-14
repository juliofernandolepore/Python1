from flask import Flask, jsonify
"""llamo a la libreria de flask y la guardo en mi variable para utilizar"""
app = Flask(__name__)

"""primeras configuracion de metodo y ruta del servidor, uso de json"""


@app.route('/', methods=['GET'])
def indef():
    return jsonify({"mensaje": "bienvenido a python"})


"""este if es para que se ejecute el server"""
if __name__ == "__main__":
    app.run(debug=True)
