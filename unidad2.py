from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
	#return render_template()
	return '<h1>Bienvenido a mi Sistema</h1>'

@app.route('/autor', methods=['GET'])
def autor():
	#return render_template()
	return '<h2>Hola, soy Alvaro</h2>'

@app.route('/alcohol', methods=['GET', 'POST'])
def alcohol():
	if request.method == 'POST':
		alcohol = request.form.get('alcohol')
		if alcohol == 'cheve' or alcohol == 'cerveza':
			alcohol = 'cerveza'

		if alcohol == 'tequila':
			alcohol = 'que perro asco'

		return '''

			<hr>
			<h2>Elegiste {} !</h2>x
			<hr>

		'''.format(alcohol)
	else:
		return '''
			<form method="POST">
				<hr>
				<h3>Elige un alcohol:</h3>
				<input type="text" name="alcohol"> <br><br>
				<input type="submit" value="A tomar!">
				<hr>
			</form>'''


app.run()
