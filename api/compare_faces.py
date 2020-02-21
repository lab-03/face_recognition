from flask import jsonify, request, redirect
from face_recgonition.face_recognition_api import compare_faces
from helpers.image_validations import allowed_file

def compare():
    check_if_image_missing()
    original_face, captured_face = get_faces_files()
    same_person = compare_faces(request.files['original'], request.files['captured'])
    return jsonify({"same_person": same_person})



def check_if_image_missing():
    if 'original_face' not in request.files:
        return redirect(request.url)
    if 'captured_face' not in request.files:
        return redirect(request.url)
    file_1, file_2 = get_faces_files()
    if file_1.filename == '' or file_2.filename == '':
        return redirect(request.url)
    if not(file_1 and file_2 and allowed_file(file_1.filename) and allowed_file(file_2.filename)):
        return redirect(request.url)

def get_faces_files():
    return request.files['original'], request.files['captured']