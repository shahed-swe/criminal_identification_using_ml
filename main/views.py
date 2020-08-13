from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
from django.conf import settings


def home(request):
    return render(request, "home.html", {"title":"Home"})

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(num)
        return True
    except (TypeError, ValueError):
        pass

    return False

def TakeImages(request):
    criminal_id = request.POST['id']
    criminal_name = request.POST['name']
    if(is_number(criminal_id) and criminal_name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = settings.BASE_DIR+"\main\static\cascade\haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        print(harcascadePath)
        print(detector)
        sampleNum = 0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                #incrementing sample number
                sampleNum = sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite(settings.BASE_DIR+"\main\static\TrainingImage\ "+criminal_name + "."+criminal_id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                #display the frame
                cv2.imshow('frame', img)
            #wait for 100 miliseconds
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + criminal_id + " Name : " + criminal_name
        row = [criminal_id, criminal_name]
        with open(settings.BASE_DIR+'\main\static\StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        return HttpResponse("<h1>{}</h1>".format(res))
    else:
        if(is_number(criminal_id)):
            return HttpResponse("<h1>Enter Alphabatic Name</h1>")
        if(criminal_name.isalpha()):
            return HttpResponse("<h1>Enter Numberic Id</h1>")


def TrainImages(request):
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = settings.BASE_DIR+"\main\static\cascade\haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels(settings.BASE_DIR+"\main\static\TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save(settings.BASE_DIR+"\main\static\Model\Training.yml")
    res = "Image Trained"
    return HttpResponse("<h1>{}</h1>".format(res))


def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    #print(imagePaths)

    #create empth face list
    faces = []
    #create empty ID list
    Ids = []
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        #getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def TrackImages(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read(settings.BASE_DIR+"\main\static\Model\Training.yml")
    harcascadePath = settings.BASE_DIR+"\main\static\cascade\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv(settings.BASE_DIR+"\main\static\StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if(conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if(conf > 75):
                noOfFile = len(os.listdir(settings.BASE_DIR+"\main\static\ImagesUnknown"))+1
                cv2.imwrite(settings.BASE_DIR+"\main\static\ImagesUnknown\Image"+str(noOfFile) +
                            ".jpg", im[y:y+h, x:x+w])
            cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = settings.BASE_DIR+"\main\static\Attendance\Attendance_" + \
        date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res = attendance
    return HttpResponse(res)