import cv2

ataturk = cv2.imread("Ataturk.jpg")
sinem = cv2.imread("Sinem_Baskan.jpg")

if ataturk.shape != sinem.shape:
    # Eğer boyutlar farklıysa, 'sinem' görüntüsünü 'ataturk' görüntüsünün boyutlarına getir
    sinem = cv2.resize(sinem, (ataturk.shape[1], ataturk.shape[0]))

xor_islemi = cv2.bitwise_xor(ataturk, sinem, mask=None)

cv2.imshow("Xor İşlemi", xor_islemi)

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()

cv2.imwrite("xor_islemi.jpg", xor_islemi)