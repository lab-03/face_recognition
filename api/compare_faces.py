from flask import jsonify, request, redirect
from face_recgonition.face_recognition_api import compare_faces
from helpers.image_validations import allowed_file
from helpers.image_downloader import url_to_image

def compare():
    accuracy = 0
    if check_if_image_missing(): 
       return same_person_resp(False, 0)
    original_face_image =  get_face_image(image_url('original_face'))
    captured_face_image =  get_face_image(image_url('captured_face'))
    same_person, accuracy = compare_faces(original_face_image, captured_face_image)
    return same_person_resp(same_person, accuracy)



def check_if_image_missing():
    if 'original_face' not in request.json or 'captured_face' not in request.json:
        return True
   
def get_face_image(file_url):
    return url_to_image(file_url)

def same_person_resp(status, accuracy):
    return jsonify({"same_person": status, "same_person_accuracy": accuracy})

def image_url(key):
    return request.json[key]