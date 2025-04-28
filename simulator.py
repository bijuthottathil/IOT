import os
import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Set your device connection string
CONNECTION_STRING = "HostName=iotstreamdata-bj.azure-devices.net;DeviceId=iotDevice;SharedAccessKey=+re3WM+7aybVA/BJTMWF64oCWea+cZ/5kYTvGDt9ZO8="

# Define the telemetry data format
TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

def run_telemetry_sample(client):
    print("Sending messages to IoT Hub...")
    while True:
        # Simulate telemetry data
        temperature = TEMPERATURE + (random.random() * 15)
        humidity = HUMIDITY + (random.random() * 20)
        msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
        message = Message(msg_txt_formatted)

        # Add a custom application property
        if temperature > 30:
            message.custom_properties["temperatureAlert"] = "true"
        else:
            message.custom_properties["temperatureAlert"] = "false"

        # Send the message
        print(f"Sending message: {message}")
        client.send_message(message)
        print("Message successfully sent")
        time.sleep(10)

def main():
    print("IoT Hub Quickstart - Simulated device")
    print("Press Ctrl-C to exit")
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    try:
        run_telemetry_sample(client)
    except KeyboardInterrupt:
        print("Simulation stopped by user")
    finally:
        client.shutdown()

if __name__ == '__main__':
    main()
