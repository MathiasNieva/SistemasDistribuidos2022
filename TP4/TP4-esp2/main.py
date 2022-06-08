# Complete project details at https://RandomNerdTutorials.com
from umqttsimple import MQTTClient
import boot
from random import seed
from random import randint
import json

# print(station.status(['rssi']))
s = "localhost"

def sub_cb(topic, msg):
  messageObj = json.loads(msg.decode("utf-8"))
  if topic == b'forward':
    if (messageObj["forward"] == "True" ):
      print((topic, msg))
      publishMsg(messageObj)
      print('Message received from esp1')
      ledState = getLedState(messageObj["control"])
      led.value(ledState)

def getLedState(val):
  if(val == "ON"):
    return True
  else:
    return False

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, 21182)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker: %s Reconnecting...' % (mqtt_server))
  sleep(3)
  reset()

def publishMsg(msgObj): 
  global counter, msg1, client_id
  if(msgObj["forward"] == "True"):
    msg1 = '{ "control" : "%s",  "forward" : "%s", "ip" : "%s", "esp32" : "%s" }' % (msgObj["control"], msgObj["forward"], msgObj["ip"], client_id)
    oled.fill(0)
    oled.text('{ control: %s, ' % (msgObj["control"]), 0, 0)
    oled.text('forward: %s, ' % (msgObj["forward"]), 0, 10)
    oled.text('ip: %s, ' % (msgObj["ip"]), 0, 20)
    oled.text('esp: %s }' % (client_id.decode("utf-8")), 0, 30)
    oled.text('}', 0, 40)
    oled.show()
  else:
    msg1 = '{ "control" : "%s",  "forward" : "%s", "ip" : "%s" }' % (msgObj["control"], msgObj["forward"], msgObj["ip"])
    counter = counter + 1
    oled.fill(0)
    oled.text('{ control: %s, ' % (msgObj["control"]), 0, 0)
    oled.text('forward: %s, ' % (msgObj["forward"]), 0, 10)
    oled.text('ip: %s }' % (msgObj["ip"]), 0, 20)
    oled.show()

def randomVal(value):
  rndVal = randint(0, 20)
  val = ""
  if(value == "control"):
    if(rndVal % 2 == 0):
      val = 'ON'
    else:
      val = 'OFF'
  else:
    if(rndVal % 2 == 0):
      val = 'True'
    else:
      val = 'False'
  return val

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
global oled, ssid, topic_sub, counter, msg1
while True:
  try:
    client.check_msg()
    if (time() - last_message) > message_interval:
      # ctrlVal = randomVal("control")
      # fwdVal = randomVal("forward")
      # publishMsg(ctrlVal, fwdVal)
      # if(fwdVal == "True"):
      #   client.publish('forward', str(msg1))
      #   print("message for esp2")
      #   print()
      # else: 
      #   client.publish('control', str(msg1))
      # client.publish('control', str(msg1))
      last_message = time()
      
  except OSError as e:
    restart_and_reconnect()