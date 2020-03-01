from flask import Flask
from api.compare_faces import compare

app = Flask(__name__)


@app.route('/', methods=['POST'])
def compare_images():
    return compare()


@app.route('/compare', methods=['GET'])
def compare_page(): 
    return app.send_static_file('example.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
