import face_recognition


def compare_faces(original_face, captured_face):
    
    same_person = False
    
    original_face_encoding = get_image_encoding(original_face)
    captured_face_encoding = get_image_encoding(captured_face)

    if len(captured_face_encoding) > 0 and len(original_face_encoding) > 0:
        same_face = face_recognition.compare_faces([original_face_encoding[0]], captured_face_encoding[0])
        distance = face_recognition.face_distance(original_face_encoding, captured_face_encoding[0])[0]
        accuracy = round((1 - distance) * 100, 2)
        if same_face[0]:
            same_person = True
        print(accuracy);
    return same_person, accuracy

def get_image_encoding(image_file):
    image = face_recognition.load_image_file(image_file)
    return face_recognition.face_encodings(image)    

def detect_number_of_faces(face_image):
    image = face_recognition.load_image_file(face_image)
    return len(face_recognition.face_locations(image))