#realtime face tracking and people count 
import cv2
#loading haar cascade xml file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro: could not open video stream")
    exit()
while True:
    ret,frame = cap.read()
    if not ret:
        print("error Fialed to capture frame")
        break


    #convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #etect faces in the frame
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    #draw rectangles around detected faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #display the number of faces detected on the frame
        cv2.putText(frame,f'Faces: {len(faces)}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Detection',frame)

        #exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
