import cv2

cap = cv2.VideoCapture('video-files/IMG_2921.MOV')

count = 0
success = True
while success:
    success, image = cap.read()
    if count % 50 == 0:
        print('frame' + str(count) + '.jpg')
        cv2.imwrite("video-files/2921-%d.jpg" % count, image)
        if cv2.waitKey(10) == 27:
            break
    count += 1
