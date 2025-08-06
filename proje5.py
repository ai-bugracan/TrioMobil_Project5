import cv2 as cv
import numpy as np
from random import randint

# Havuç resminin okunması
img = cv.imread("carrot.png")
img = cv.resize(img, (20,20), cv.INTER_LINEAR)

# ekran boyutu
width = 700
height = 700

# havucun başlangıç konumu, ilerleyecek piksel sayısı ve çapı
w1 = randint(20,680)
h1 = randint(20,680)
vx = randint(-10,10) 
vy = randint(-10,10)
radius = 10

score = 0

# Mouse ile üstüne geldiğinde scoreu artırıp havucun rastgele bir yerden tekrar başlamasını sağlayacak fonksiyon
def catcher(event, x, y, flags, param):
    global score, w1, h1, vx, vy

    if event == cv.EVENT_MOUSEMOVE:
        if abs(w1-x) <= 20 and abs(h1-y) <= 20: # Mousun konum bilgisi havucun konum bilgisinden çıkarıldığında arasındaki fark 5 den az ise
            score += 1                      # skor değişkenini 1 artırıp havucun konum ve ilerlenecek piksel sayısı bilgisine rastgele değer ataması sağlanır ve
            w1 = randint(20,680)            # bu konum ve piksel bilgileri kullanılarak tekrar çizim fonksiyonu çalıştırılır.
            h1 = randint(20,680)
            vx = randint(-10,10)
            vy = randint(-10,10)
            carrotMove()


# Havucun ekrana çizildikten sonra boş arkaplan üzerine belirtilen piksel kadar ileriye tekrar çizilmesini sağlayan fonksiyon
def carrotMove():
    global w1,h1,radius,width,height,vx,vy

    # arka plan
    blank = np.zeros((width,height,3),dtype="uint8")
    blank[:] = (0,255,0)

    cv.namedWindow("Carrot")
    cv.setMouseCallback("Carrot", catcher)

    while True:
        frame = blank.copy()                                    # Boş arkaplanı kopyalayıp üzerine yeni konumları olan görseli yapıştırır
        frame[h1:h1+img.shape[0], w1:w1+img.shape[1]] = img
        frame = cv.putText(frame,"Skor:" + str(score),(10,30),cv.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2)    # Ekranın sol üst köşesine skoru yazar
        cv.imshow("Carrot",frame)

        if (w1+img.shape[1]+vx) <= 20 or (w1+img.shape[1]+vx) >= width:     # Görselin arkaplan kenarlarına geldiğinde eklenecek piksel sayısını tersine döndürerek
            vx = -vx                                                        # ters yönde konuma yapıştırılmasını sağlar

        if (h1+img.shape[0]+vy) <= 20 or (h1+img.shape[0]+vy) >= height:
            vy = -vy

        w1 += vx    # Çizilen havucun konum değişkenlerini belirtilen piksel kadar artırır
        h1 += vy

        key = cv.waitKey(100)

        if key == ord("q"): # q tuşuna basıldığında döngünün kırılmasını sağlar
            break

carrotMove()

cv.destroyAllWindows() # Program sonlandırıldığında tüm pencerelerin kapanmasını sağlarqqqqqqqqqqq