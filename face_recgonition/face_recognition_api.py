import face_recognition


def compare_faces(original_face, captured_face):
    
    same_person = False
    
    original_face_encoding = get_image_encoding(original_face)
    captured_face_encoding = get_image_encoding(captured_face)

    if len(captured_face_encoding) > 0 and len(original_face_encoding) > 0:
        same_face = face_recognition.compare_faces([original_face_encoding[0]], captured_face_encoding[0])
        if same_face[0]:
            same_person = True
    return same_person

def get_image_encoding(image_file):
    image = face_recognition.load_image_file(image_file)
    return face_recognition.face_encodings(image)    