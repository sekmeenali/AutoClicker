import pyautogui
import time

# İlk noktanın koordinatları
x1, y1 = 920, 806

# İkinci noktanın koordinatları
x2, y2 = 637, 900

# Başlangıç zamanı
start_time = time.time()

while True:
    # İlk noktaya tıkla
    pyautogui.click(x1, y1)

    # 0.3 saniye bekle
    time.sleep(0.3)

    # İkinci noktaya tıkla
    pyautogui.click(x2, y2)

    # 0.3 saniye bekle
    time.sleep(0.3)

    # Geçen süreyi hesapla
    elapsed_time = time.time() - start_time

    # 30 saniye geçtikten sonra döngüyü sonlandır
    if elapsed_time > 30:
        break

