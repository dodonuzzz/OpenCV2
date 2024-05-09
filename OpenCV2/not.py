import cv2

ataturk = cv2.imread("Ataturk.jpg")
sinem = cv2.imread("Sinem_Baskan.jpg")

if ataturk.shape != sinem.shape:
    # Eğer boyutlar farklıysa, 'sinem' görüntüsünü 'ataturk' görüntüsünün boyutlarına getir
    sinem = cv2.resize(sinem, (ataturk.shape[1], ataturk.shape[0]))

not_islemi = cv2.bitwise_not(ataturk, sinem, mask=None)

cv2.imshow("Not İşlemi", not_islemi)

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()

cv2.imwrite("not_islemi.jpg", not_islemi)