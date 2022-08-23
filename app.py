import cv2, time

first_frame = None

video_captured=cv2.VideoCapture(0)

while True:
    check, frame = video_captured.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray=cv2.GaussianBlur(gray,(21,21), 0)
    # see if first frame is None if it is true which it is in first iteration then loop witll continue but in second iteration the loop will go to line 15.. becaue firs_frame is not None

    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame=cv2.absdiff(first_frame, gray)
    thesh_frame= cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thesh_frame = cv2.dilate(thesh_frame, None, iterations=2)

    
    cv2.imshow('capture', gray)
    cv2.imshow('delta_frame', delta_frame)
    cv2.imshow('thesh_delta', thesh_frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video_captured.release()
cv2.destroyAllWindows()
