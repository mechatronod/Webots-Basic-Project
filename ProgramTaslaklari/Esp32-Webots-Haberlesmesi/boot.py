import network
import webrepl

# Access Point Ayarları
ap = network.WLAN(network.AP_IF)
ap.active(True)

# authmode=3 -> WPA2-PSK güvenliğini temsil eder
ap.config(essid='erayOkan', password='12345678', authmode=3) 

print('WiFi Ağı Kuruldu. IP Adresi:', ap.ifconfig()[0])

# WebREPL Başlat
webrepl.start()