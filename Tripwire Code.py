from gpiozero import LightSensor, Buzzer, LED
from time import sleep

ldr = LightSensor(4)
buzzer = Buzzer(17)
led = LED(18)

while True:
    sleep(0.1)
    if ldr.value < 0.5:   #Adjust the value to change the sensitivity of the system
        buzzer.on()
        led.on()
        print("Intruder Detected!")
        sleep(15)
    else:
        buzzer.off()
        led.off()