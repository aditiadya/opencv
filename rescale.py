import cv2 as cv

#used for images, videos and live videos(webcam, external camera)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

#used for live videos only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)