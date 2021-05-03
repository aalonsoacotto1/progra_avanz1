# FLASK FRAMEWORK APPS WEB (BACKEND-SERVIDOR) PYTHON
# SERVIDOR
# RESPONDE
# HOGAR/PUNTO DE INICIO -> HOST
# VENTANILLA/PUERTA -> PORT
# SERVIDOR -> DIRECCION = HOST:PORT
# IP -> 10.4.46.139 (HOST)
# LOCALHOST (127.0.0.1)
# PUERTO ESTANDAR (HTTP/HTTPS) :80
# PUERTO DIFERENTE -> 3000, 5000, 6969, 8000, 8001, 8008

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
	return render_template("formulario.html")

@app.route('/tacos', methods=['GET'])
def tacos():
	return "Me gustan mucho los tacos!"

@app.route('/api', methods=['GET', 'POST'])
def api():
	# handle the POST request
	if request.method == 'POST':
		lenguaje = request.form.get('lenguaje')
		pais = request.form.get('pais')
		return '''
			<h1>Tu hablas: {}</h1>
			<h1>Tu pais es: {}</h1>'''.format(lenguaje, pais)

    # otherwise handle the GET request
	return '''
		<form method="POST">
			<hr>
		   <div><label>Lenguaje: <input type="text" name="lenguaje"></label></div><br>
		   <div><label>Pais: <input type="text" name="pais"></label></div><br>
		   <input type="submit" value="Enviar">
		   <hr>
		</form>'''

app.run()