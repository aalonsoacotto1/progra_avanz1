import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True





























datos = [
    {'id': 0,
     'nombre': 'Juan Perez',
     'edad': '50'
    },
    {'id': 1,
     'nombre': 'Alejandro Fernandez',
     'edad': '45'
    },
    {'id': 2,
     'nombre': 'Alvaro Moreno',
     'edad': '24'
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hola Mundo</h1><p>Retornando HTML desde el servidor de flask!</p>"

@app.route('/about', methods=['GET'])
def about():
	return "<h1>ABOUT PAGE</h1><p>Retornando HTML desde el servidor de flask!</p>"

@app.route('/datos/all', methods=['GET'])
def api_all():
	return jsonify(datos)

@app.route('/datos/', methods=['GET'])
def api_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id field provided. Please specify an id."

	results = []

	for dato in datos:
		if dato['id'] == id:
			results.append(dato)

	return jsonify(results)


app.run()