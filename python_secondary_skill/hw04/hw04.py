from hw03 import chorna_hw3 as foto
from flask import Flask, request,render_template


app = Flask(__name__)


@app.route('/')
def index():
    # print request.method
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    path = request.form['path']
    print("The path is '" + path + "'")
    foto.main(path)
    return render_template('selected.html'), path

if __name__ == '__main__':
    app.run(debug=True)
