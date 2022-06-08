# Complete project details at https://RandomNerdTutorials.com
import ssd1306
from time import sleep, time
from umqttsimple import MQTTClient
import ubinascii
from machine import Pin, SoftI2C, unique_id, reset
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()


led = Pin(2, Pin.OUT)
ssid = ''
password = ''
mqtt_server = 'research.upb.edu'
client_id = ubinascii.hexlify(unique_id())
topic_sub = 'control'
topic_pub = 'control'
msg1 = ""

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

# initialize oled
oled_width = 128
oled_height = 64
i2c_rst = Pin(16, Pin.OUT)
i2c_rst.value(0)
sleep(2)
i2c_rst.value(1) 
i2c_scl = Pin(15, Pin.OUT, Pin.PULL_UP)
i2c_sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
