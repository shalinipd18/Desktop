import cv2
import numpy as np
def apply_filter(image,ftype):
    '''Apply one filter to the image based on filter's type'''
    img = image.copy()
    if ftype =='red_tint':
        img[:,:,1] = img[:,:,0]=0
    elif ftype == 'green_tint':
        img[:,:,0] = img[:,:,2]=0
    elif ftype == 'blue_tint':
        img[:,:,1] = img[:,:,2]=0
    elif ftype == 'sobel':
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
        sy = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
        sob = cv2.bitwise_or(sx.astype('uint8'),sy.astype('uint8'))
        img = cv2.cvtColor(sob,cv2.COLOR_GRAY2BGR)
    elif ftype == 'cannny':
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray,100,200)
        img = cv2.cvtColor(canny,cv2.COLOR_GRAY2BGR)
    elif ftype == 'cartoon':
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,5)
        edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color = cv2.bilateralFilter(image,9,250,250)
        img = cv2.bitwise_and(color,color,mask=edges)
    return img



def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: could not open video stream")
        return
    filter_type = 'original'  
    print("Keys: r=red, g = green, b=blue, s=sobel, c=canny, t=cartoon, o=original, q=quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        if filter_type != 'original':
            frame = apply_filter(frame, filter_type)

        cv2.imshow('Filtered Video', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('s'):
            filter_type = 'sobel'
        elif key == ord('c'):
            filter_type = 'cannny'
        elif key == ord('t'):
            filter_type = 'cartoon'
        elif key == ord('o'):
            filter_type = 'original'
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()

