# Azure IoT to ADLS :: Generate Telemetry data and create files in ADLS
![image](https://github.com/user-attachments/assets/4c33bbee-e61d-4ca9-b16f-82acbfacbff2)


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


![image](https://github.com/user-attachments/assets/d4ea0101-d410-4e22-94bb-30794526d766)

![image](https://github.com/user-attachments/assets/033dd61c-0be7-4052-ae7b-063ff80db563)


Creating a stream analytics job to push data to adls


![image](https://github.com/user-attachments/assets/20f2c80b-638b-4057-b743-8d61feb319cf)


![image](https://github.com/user-attachments/assets/8dd2a250-5f82-4f63-99c6-5223b0b8da5c)

![image](https://github.com/user-attachments/assets/a3dadcb2-3cb8-4069-b7e7-13cdb03ce063)


![image](https://github.com/user-attachments/assets/04a1433e-200e-4a1c-8bac-d44bda7b1400)

I started stream job and simulator python applicaiton

![image](https://github.com/user-attachments/assets/0af41771-63e9-4604-b538-79cff05c9c4d)

You can see data is loading in adls storage container

![image](https://github.com/user-attachments/assets/160e42b2-d0fd-4c68-bbe5-284f236ececb)


Json data is for your reference


![image](https://github.com/user-attachments/assets/d0e39a13-8ed2-4647-b878-875cadc1207e)

You can see streaming job is still running and loading data in adls

![image](https://github.com/user-attachments/assets/7897ae00-1ed9-4052-a3e9-8037b1377178)

![image](https://github.com/user-attachments/assets/f43707b0-185e-418d-a77e-4cfc7e205b86)

![image](https://github.com/user-attachments/assets/053b08f1-8d44-4c68-88f4-7593a61f7999)




