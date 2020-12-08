#   FACE RECOGNITION


## A python-django application for face detection and recognition using face_recognition

## Description
 
    This application is developed using face_recognition https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
    Application provides 5 apis. It allows training model on individual images one at a time, also it has a batch processing feature, since training can take upto 20 second (Tested with High quality DSLR image) You can upload pictures temporily in database and finally at some feasible time can run batch training on all temporily stored images.


### How To Run:

1)   Install pipenv
2)   Clone appilcation and go to FACERECOGNITION
3)   run pipenv shell   -> pipenv install
4)   create superuser   -> python manage.py createsuperuser
5)   run server         -> python manage.py runserver



### APIS  (Tested On Insomnia)

#### To Get CSRFMIDDLEWARETOKEN
get: http://127.0.0.1:8000/person/get_csrf

#### To Train On Individual Image
post: http://127.0.0.1:8000/person/add_person/

multipart form data:  

csrfmiddlewaretoken = ""
name = ""
image = ""  //Image File

#### To Store Person Data Temporily for later training
post: http://127.0.0.1:8000/person/add_temp_person/

multipart form data:  

csrfmiddlewaretoken = ""
name = ""
image = ""  //Image File

#### To Train All Temporily Stored Images
get: http://127.0.0.1:8000/person/batch_train/

#### To Get Face Label
post: http://127.0.0.1:8000/person/get_label/

multipart form data:  

csrfmiddlewaretoken = ""
image = ""  //Image File