import paho.mqtt.client as mqtt
import time
mqttBroker = "test.mosquitto.org"
client = mqtt.Client(client_id="TassaeriID1234", clean_session=True)
client.connect(mqttBroker, port=1883)
i = 1
sensorLat = 61.500634
sensorLon = 23.763382
sensorTime = time.localtime()
sensorEpoch = int(time.time())
interval = 1


while i < 45:
    i = i+1
    sensorLat = sensorLat + -0.0000058
    sensorLon = sensorLon + -0.0000220
    sensorEpoch = sensorEpoch + interval
    data = "{\"name\":\"Driver2\",\"icon\":\"male\",\"iconColor\":\"darkred\",\"time\":\""+str(time.ctime())+"\",\"epoch\":" +str(sensorEpoch)+",\"lat\":"+str(sensorLat)+",\"lon\":"+str(sensorLon)+"}"
    client.publish("Driving/status/location", data)
    print("Published " + str(time.ctime()) + " epoch " + str(sensorEpoch) + " Lat " + str(sensorLat) + "Lon " + str(sensorLon) + " to topic Walking01/status/location")
    time.sleep(interval)




client.disconnect()
