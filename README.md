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

Next step is to test simulator and IOT data transmission

Run simulator program 

![image](https://github.com/user-attachments/assets/4a6cd7f1-05cf-4f65-a4d4-c29ea11d6a35)

I will generage json data and load in IOT Hub

You can see data is adding in device

![image](https://github.com/user-attachments/assets/dc56131d-2795-4d29-acd8-cc8243983610)


You can query data from device

![image](https://github.com/user-attachments/assets/5a97b065-c3cb-4b8f-aaab-6dcc17228978)


Now our intend is to store above messages in ADLS Storage

Created adls storage with a container

![image](https://github.com/user-attachments/assets/dd57e362-2ed1-4020-91e1-633072d0f3ea)


Go To message routing and add custom end point

![image](https://github.com/user-attachments/assets/235687fa-5b5c-418c-b422-a8f169be6369)




