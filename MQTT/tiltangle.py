import paho.mqtt.client as mqtt
import time
import random
import json

mqttBroker ="test.mosquitto.org"
client = mqtt.Client (client_id="YourClientID", clean_session=True)
client.connect(mqttBroker, port=1883)
i = 1
while i < 10:
    i = i+1
    sensorTemp = random.randint(1, 30)
    sensorHum = random.randint(1, 100)



    value = {"Temperature":sensorTemp, "Humidity":sensorHum}
    values = json.dumps(value)
    type(values)


    client.publish("YourClientTopic", values)
    print("Published " + str(sensorTemp) + " to topic Temperature" + " and " + str(sensorHum) + " to topic Humidity" )

    time.sleep(5)
client.disconnect()