import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ORIJINAL_YOL =r"C:\Users\hayri\OneDrive\Masaüstü\eriyen saatler.png"
CIKTI_YOL = r"C:\Users\hayri\OneDrive\Masaüstü\ispatli_islem.jpg"

def ispatli_damga_sistemi():                      #Kaynak resmimizin belirtilen
    if not os.path.exists(ORIJINAL_YOL):          #adreste olup olmadığını kontrol eder.
        print("Hata: Kaynak resim bulunamadı.")
        return

    #  -ADIM 1: ORIJINAL PIKSEL DEĞERİNİ OKUMA -
    # Resmin tam ortasındaki bir pikselin rengini kaydettik (İspat için)
    img_orig = Image.open(ORIJINAL_YOL).convert("RGB")
    W, H = img_orig.size
    orta_x, orta_y = int(W/2), int(H/2)
    
    # Resmin damgalanmadan önceki temiz hali
    orijinal_renk = img_orig.getpixel((orta_x, orta_y))
    print(f"[1] BAŞLANGIÇ: Tam ortadaki pikselin rengi: {orijinal_renk}")

    #   -ADIM 2: DAMGA EKLEME- 
    draw = ImageDraw.Draw(img_orig)
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    mesaj = "DAMGA"
    
    
    draw.text((orta_x - 50, orta_y - 40), mesaj, font=font, fill=(255, 255, 255))   # Yazıyı tam ortaya damgalıyor
    img_orig.save(CIKTI_YOL)
    
    # Damga eklendikten sonraki renk (Beyaz : 255, 255, 255)
    damgali_img = Image.open(CIKTI_YOL)
    yeni_renk = damgali_img.getpixel((orta_x, orta_y))
    print(f"[2] DAMGA EKLENDİ: Ortadaki piksel artık: {yeni_renk} (Yazı geldi!)")

    # -ADIM 3: DAMGAYI TEMİZLEME-
    # Yazılı dosyayı siliyoruz ve orijinali referans alıyoruz
    if os.path.exists(CIKTI_YOL):
        os.remove(CIKTI_YOL)
        print("[3] TEMİZLİK: Damgalı dosya silindi.")

    # -ADIM 4: DOĞRULAMA (FINAL)-
    # Tekrar orijinal resmi kontrol ediyoruz
    final_img = Image.open(ORIJINAL_YOL)
    final_renk = final_img.getpixel((orta_x, orta_y))
    
    print(f"[4] SONUÇ: Piksel rengi tekrar: {final_renk}")
    
    if final_renk[:3] == orijinal_renk[:3]:
        print("\n Resim başarıyla tertemiz hale döndü.")
    else:
        print("\n Renkler eşleşmiyor.")

# Çalıştır
ispatli_damga_sistemi()
