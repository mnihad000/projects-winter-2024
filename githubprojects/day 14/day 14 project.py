import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#create data base
path = 'employees'
my_images = []
employees_names= []
employees_list = os.listdir(path)


for name in employees_list:
    this_image = cv2.imread(f'{path}\\{name}')
    my_images.append((this_image))
    employees_names.append(os.path.splitext(name)[0])

print(employees_names)

def encode(images):
    encoded_list = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #encoded
        encoded = fr.face_encodings(image)[0]
        encoded_list.append(encoded)
    return encoded_list

#record attendance
def record_attendance(person):
    f= open('register.csv', 'r+')
    data_list = f.readlines()
    register_names = []

    for line in data_list:
        newcomer = line.split(',')
        register_names.append(newcomer[0])
    if person not in register_names:
        right_now = datetime.now()
        string_right_now = right_now.strftime('%Y-%m-%d %H:%M:%S')
        f.writelines(f'\n{person}, {string_right_now}')



encoded_employee_list = encode(my_images)

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

success, image = capture.read()

if not success:
    print('capture failed')
else:
    captured_face = fr.face_locations(image)
    encoded_captured_face = fr.face_encodings(image, captured_face)
    for face, location_face in zip(encoded_captured_face, captured_face):
        matches = fr.compare_faces(encoded_employee_list, face)
        distance = fr.face_distance(encoded_employee_list, face)
        print(distance)

        match_index = numpy.argmin(distance)

        if distance[match_index] > 0.6:
            print('does not match any of our employee')
        else:
            employee_name = employees_names[match_index]

            y1,x2,y2,x1 = location_face
            cv2.rectangle(image,
                          (x1, y1),
                          (x2, y2),
                          (0,255,0),
                          2)
            cv2.rectangle(image,
                          (x1, y2 - 35),
                          (x2, y2),
                          (0,255,0),
                          cv2.FILLED)
            cv2.putText(image,
                        employee_name,
                        (x1 + 6, y2-6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255,255,255),
                        2)
            record_attendance(employee_name)
            cv2.imshow('web image', image)

            cv2.waitKey(0)

