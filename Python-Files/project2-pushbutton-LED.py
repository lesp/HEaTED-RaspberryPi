from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(22)

button.when_pressed = led.toggle()

pause()
