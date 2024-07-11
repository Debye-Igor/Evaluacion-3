from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int((request.form['asistencia']))

        promedio = round((nota1+nota2+nota3) / 3,2)

        if promedio >= 40 and asistencia >=75:
            estado = "APROBADO"
        elif promedio < 40 and asistencia >= 75:
            estado = "REPROBADO, no cumple nota mínima 40"
        elif promedio >= 40 and asistencia < 75:
            estado = "REPROBADO, no cumple con mínimo de asitencia 75%"
        else:
            estado ="REPROBADO"

        return render_template('ejercicio1.html', prom=promedio,est=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            resultado = f"El nombre con la mayor cantidad de caracteres es: {nombre1}."
            cantidad = f"El nombre tiene: {len(nombre1)} caracteres."
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            resultado = f"El nombre con la mayor cantidad de caracteres es: {nombre2}."
            cantidad = f"El nombre tiene: {len(nombre2)} caracteres."
        else:
            resultado = f"El nombre con la mayor cantidad de caracteres es: {nombre3}."
            cantidad = f"El nombre tiene: {len(nombre3)} caracteres."

        return render_template('/ejercicio2.html', resultado=resultado, cantidad=cantidad)
    return render_template('/ejercicio2.html')

if __name__ == '__main__':
    app.run()
