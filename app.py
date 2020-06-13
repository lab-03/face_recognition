from flask import Flask
from api.compare_faces import compare 
from api.detect_faces import detect_faces_in_image


app = Flask(__name__)


@app.route('/verify', methods=['POST'])
def compare_images():
    return compare()


@app.route('/index', methods=['GET'])
def compare_page(): 
    return app.send_static_file('example.html')

@app.route('/detect_faces', methods=['post'])
def detect_faces():
    return detect_faces_in_image()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
