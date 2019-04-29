import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
  print("ini gak error")
  client.subscribe("group/chats")

def on_message(client, userdata, msg):
  print(msg.topic + " " + str(msg.payload))

client = mqtt.Client("P1")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.103")