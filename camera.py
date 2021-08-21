import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    #フレームが取得できなかった場合は、画面を閉じる
    if not ret:
        break

    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    #とあるキーが押されたら閉じるESC
    if key == 29:
        break
    # x = input()
    # if x == 29:

cap.release()
cv2.destroyAllWindows()