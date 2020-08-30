import p5
import math
# görüntüleme için p5 ve trigonometrik işlemler
# için math kütüphaneleri içe aktarıldı

# Pencere boyutu için değişkenler atandı (global)
w, h = 500, 500

# Bir yarıçap belirlendi (global)
r = 225


# Başlangıç fonksiyonu.
# p5 bu fonksiyonu 1 defa başlangıta çalıştırır
def setup():
    # Pencereyi tanımlanan boyutta oluştur
    p5.size(w, h)


# Ekrana çizim fonksiyonu.
# Bu fonksiyon frame her yenilendiğinde çalıştırılır
# 60 FPS için saniyede 60 defa çalıştırılacaktır
def draw():
    # Arka alanı siyah yap
    p5.background(0)
    # Orijini (Yani (0, 0) noktasını) pencerenin ortasına taşı
    p5.translate(w / 2, h / 2)

    # Analog saatte, saat değerlerinin olduğu konumlara
    # kırmızı noktalar koymak için döngü
    # [0, 360) aralığında 30'ar derece açılarla değer oluştur:
    # Böylece 0, 30, 60, ..., 270, 300, 330 değerleri elde edilecek
    for i in range(0, 360, 30):
        # Her bir açı için x ve y konumlarını hesapla
        x = r * math.cos(math.radians(i))
        y = r * math.sin(math.radians(i))

        # Çizilecek nesnenin içini kırmızı renk ile doldur
        p5.fill(255, 0, 0)
        # Çizilecek nesne için çevre çizgisi çizme
        p5.no_stroke()
        # x ve y konumuna 15 piksel çapında bir daire çiz.
        p5.circle((x, y), 15)

    # Analog saatte, dakika değerlerinin olduğu konumlara
    # beyaz noktalar koymak için döngü
    # [0, 360) aralığında 6'şar derece açılarla değer oluştur:
    # Böylece 0, 6, 12, ..., 342, 348, 354 değerleri elde edilecek
    for u in range(0, 360, 6):
        # Eğer u açısı 30'a tm bölünebiliyorsa işlemi YAPMA
        if u % 30:
            # Her bir açı için x ve y konumlarını hesapla
            x = r * math.cos(math.radians(u))
            y = r * math.sin(math.radians(u))

            # Çizilecek nesnenin içini beyaz renk ile doldur
            p5.fill(255)
            # Çizilecek nesne için çevre çizgisi çizme
            p5.no_stroke()
            # x ve y konumuna 10 piksel çapında bir daire çiz.
            p5.circle((x, y), 10)


# Bu betik çalıştırıldığında aşağıdaki işlemleri yap
# Böylece import edildiğinde aşağıdaki işlemler yapılmaz
if __name__ == "__main__":
    # p5'i varsayılan değerler ile çalıştır
    p5.run()
