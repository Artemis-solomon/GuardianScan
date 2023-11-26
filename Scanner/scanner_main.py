# scanner_main.py

import logging
from flask import Flask, render_template, request
from sql_injection_detector import detect_sql_injection

# Configure logging
logging.basicConfig(filename='vulnerability_scanner.log', level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    try:
        input_data = request.form.get('input_data')
        result = detect_sql_injection(input_data)

        if result:
            logging.warning(f'Potential SQL injection detected: {input_data}')
            return render_template('result.html', result='Potential SQL injection detected!')
        else:
            return render_template('result.html', result='No SQL injection detected.')

    except Exception as e:
        logging.error(f'Error during scanning: {str(e)}')
        return render_template('result.html', result='Error during scanning. Please check the logs.')

if __name__ == '__main__':
    logging.info('GuardianScan started.')
    app.run(debug=True)
    logging.info('GuardianScan stopped.')
