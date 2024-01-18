from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    c1 = request.form['campo1']
    c2 = request.form['campo2']
    c3 = request.form['campo3']
    c4 = request.form['campo4']
    c1 = float(c1)
    c3 = float(c3)
    c5 = c1+c3

    print(c5)

    return f'Dados Recebidos: Campo 1={c1}, Campo 2={c2}, Campo 3={c3}, Campo 4={c4}   soma dos dois: {c5}'

if __name__ == '__main__':
    app.run(debug=True)
