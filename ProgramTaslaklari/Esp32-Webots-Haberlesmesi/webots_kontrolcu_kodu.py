#webots kontrolcu kodu
from controller import Robot
import socket

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Webots'taki motorun adı (Scene Tree'den kontrol edin)
left_motor = robot.getDevice('left wheel motor')
left_motor.setPosition(float('inf')) # Hız kontrolü için sonsuz pozisyon
left_motor.setVelocity(0.0)

# UDP Dinleyici
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5005))
sock.setblocking(False)

while robot.step(timestep) != -1:
    try:
        data, addr = sock.recvfrom(1024)
        ticks = int(data.decode())
        
        # Basit bir test: Her 100 tıkta tekerleği 1 rad/s hızla döndür
        # Normalde burada setPosition ile hassas konum ayarlanır
        print("ESP32'den gelen sanal tık:", ticks)
        left_motor.setVelocity(2.0) # Robotun tekerleği dönmeye başlar
        
    except (BlockingIOError, ValueError):
        pass