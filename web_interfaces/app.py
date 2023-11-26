from flask import Flask, render_template, request
from sql_injection_detector import detect_sql_injection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    input_data = request.form.get('input_data')
    result = detect_sql_injection(input_data)
    
    if result:
        return render_template('result.html', result='Potential SQL injection detected!')
    else:
        return render_template('result.html', result='No SQL injection detected.')

if __name__ == '__main__':
    app.run(debug=True)

