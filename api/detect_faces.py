from flask import jsonify, request, redirect
from face_recgonition.face_recognition_api import detect_number_of_faces
from helpers.image_validations import allowed_file
from helpers.image_downloader import url_to_image


def detect_faces_in_image():
    face_image = request.json['face_image']
    return jsonify({"number_of_faces": detect_number_of_faces(url_to_image(face_image))})
