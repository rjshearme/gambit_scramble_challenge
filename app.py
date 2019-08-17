import re

from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import requests

import IPython

from solver import Solver

app = Flask(__name__)
PROBLEM_URL = "https://www.gambitresearch.com/quiz/"



@app.route('/')
def index():
    problem_content = requests.get(PROBLEM_URL).content
    problem_soup = BeautifulSoup(problem_content)
    problem_body = problem_soup.find('body')
    ascii_codes = [int(digits) for digits in re.findall(r'\d+', problem_body.text)]
    ascii_chars = Solver.codes_to_chars(ascii_codes)
    # stub_codes = [20, 10, 17, 56, 20, 209, 236, 232, 20, 58, 12, 23, 45, 25, 26, 56, 6, 25, 53, 20, 19, 63, 197, 11, 59, 23, 197, 63, 20, 17, 66, 14, 19, 51, 197, 25, 52, 10, 197, 19, 6, 18, 46, 14, 25, 236, 8, 13, 45, 17, 17, 49, 19, 12, 49, 211, 197, 28, 17, 10, 45, 24, 10, 236, 24, 10, 58, 9, 197, 69, 20, 26, 62, 197, 24, 59, 17, 26, 64, 14, 20, 58, 197, 6, 58, 9, 197, 15, 251, 197, 64, 20, 197, 53, 8, 6, 58, 8, 20, 48, 10, 229, 51, 6, 18, 46, 14, 25, 62, 10, 24, 49, 6, 23, 47, 13, 211, 47, 20, 18, 236, 22, 26, 59, 25, 14, 58, 12, 197, 62, 10, 11, 49, 23, 10, 58, 8, 10, 6, 197, 219, 255, 8, 10, 253, 222, 217, 3, 215, 6, 250]
    # stub_chars = Solver.codes_to_chars(stub_codes)
    context = {
        'ascii_chars': ascii_chars,
        'ascii_codes': ascii_codes,
    }

    return render_template('index.html', **context)


@app.route('/unscramble', methods=["POST"])
def unscramble():
    codes = request.json.get('codes')
    args = request.json.get('args')
    unscrambled_codes = Solver.unscramble(codes, *args)
    return {
        "codes": unscrambled_codes,
        "text": Solver.codes_to_chars(unscrambled_codes)
    }



if __name__ == '__main__':
    app.run(port=8000, debug=True)