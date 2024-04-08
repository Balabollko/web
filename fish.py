from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# Отримання ключа доступу та URL з вашого ресурсу Azure Face API
KEY = '3054f84afb90427a9a2cc62c0b4640f9'
ENDPOINT = 'https://uuk.cognitiveservices.azure.com/'

# Створення клієнта Azure Face API
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Використання функцій Azure Face API, наприклад, розпізнавання облич
detected_faces = face_client.face.detect_with_url(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSapwwrcLJJGrMlQ6eC5q85MRVWSypV9Xs3RQ&usqp=CAU')