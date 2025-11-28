from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def simple_calculator():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculator_operations():
    if request.method == 'POST':

        try:
            opr1 = float(request.form['operand1'])
            opr2 = float(request.form['operand2'])
        except:
            result = "Invalid operand. Please try again!"
            return render_template('index.html', result=result)

        opr = request.form['operator']

        if opr == '+':
            result = f"Addition of {opr1} and {opr2} is {opr1 + opr2}"
        elif opr == '-':
            result = f"Subtraction of {opr1} and {opr2} is {opr1 - opr2}"
        elif opr == '*':
            result = f"Multiplication of {opr1} and {opr2} is {opr1 * opr2}"
        else:
            result = f"Division of {opr1} and {opr2} is {opr1 / opr2}"

        return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
