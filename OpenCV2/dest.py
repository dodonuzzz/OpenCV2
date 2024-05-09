import cv2

ataturk = cv2.imread("Ataturk.jpg")
sinem = cv2.imread("Sinem_Baskan.jpg")

if ataturk.shape != sinem.shape:
    # Eğer boyutlar farklıysa, 'sinem' görüntüsünü 'ataturk' görüntüsünün boyutlarına getir
    sinem = cv2.resize(sinem, (ataturk.shape[1], ataturk.shape[0]))

dest_not1 = cv2.bitwise_not(ataturk, mask=None)
dest_not2 = cv2.bitwise_not(sinem, mask=None)

cv2.imshow("Not İşlemi 1", dest_not1)
cv2.imshow("Not İşlemi 2", dest_not2)

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()

cv2.imwrite("not_islemi1.jpg", dest_not1)
cv2.imwrite("not_islemi2.jpg", dest_not2)