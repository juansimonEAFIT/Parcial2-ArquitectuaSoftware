from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/factorial/<int:num>', methods=['GET'])
def calcular_factorial(num):
    # Calcular factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    # Determinar si el número ingresado es par o impar
    if num % 2 == 0:
        etiqueta = "par"
    else:
        etiqueta = "impar"

    # Retornar respuesta JSON
    return jsonify({
        "numero_recibido": num,
        "factorial": factorial,
        "etiqueta": etiqueta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
