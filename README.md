# Azure IoT to ADLS :: Generate Telemetry data and create files in ADLS


1. IOT Hub created in Azure

   ![image](https://github.com/user-attachments/assets/7586ae44-a96e-4344-becf-f71fff56896f)

2. Created IOT Device
![image](https://github.com/user-attachments/assets/133d4de6-e295-4a00-9a20-a4059fc2afff)

![image](https://github.com/user-attachments/assets/7fe40105-1e04-41fd-9ba2-c31e5fa72368)


3. Creating a simulator app in python to send weather data to this IOT Device

   Created Virtual Environment in Mac

bijum@MacBook-Pro az-iot-device-simulator % python3 -m venv venv

bijum@MacBook-Pro az-iot-device-simulator % source venv/bin/activate

I have used below python code for event generation. Primary Connection string is copied from Device setting
![image](https://github.com/user-attachments/assets/c2a702b8-632a-44ea-a2bc-2a757ad75bb0)

![image](https://github.com/user-attachments/assets/b4c8305c-c21c-4497-a4ab-c6caf3966349)

