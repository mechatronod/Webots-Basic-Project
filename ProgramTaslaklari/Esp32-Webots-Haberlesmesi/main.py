import socket
import time
import random

# UDP ayarlari
# ESP32 Access Point modunda PC IP adresi
UDP_IP = "192.168.4.2" 
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

virtual_ticks = 0

print("--- Sanal Enkoder Yayini Basladi ---")

while True:
    # real bir motoru simule edelim: 
    # Her 100ms'de bir 5 ile 15 arasi tik
    virtual_ticks += random.randint(5, 15)
    
    # Veriyi paketle ve gonder
    msg = str(virtual_ticks)
    try:
        sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
        print("Gonderilen Ticks:", virtual_ticks)
    except:
        print("PC bekleniyor...")
    
    time.sleep(0.1) # 10Hz hizinda gonder