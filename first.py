import cv2

cap=cv2.VideoCapture("test.mp4")

while True:
    success, img = cap.read()
    img=cv2.resize(img,(1280,720),interpolation=cv2.INTER_AREA)
    #edges = cv2.Canny(img, 100, 200)
    cv2.imshow("vid",img)
    if(cv2.waitKey(1) & 0xFF==ord('w')):
        break
#cv2.waitKey(0)
#cv2.destroyAllWindows()