import cv2 as cv;

#reading image which is given as input
img = cv.imread('photos/cat_large.jpg')

#showing the image on a new window
cv.imshow('Cat', img)

#reading video which is given as input
capture = cv.VideoCapture('videos/dog.mp4')
#capture = cv.VideoCapture(0) -> when using webcam instead of a video

#reading video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)