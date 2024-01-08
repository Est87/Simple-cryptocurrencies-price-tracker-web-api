JSON REST API service using Python FASTAPI of a simple cryptocurrencies price tracker web app.

Backend only, no frontend implemented.

Steps to run the program:
1. Download all the files and place them inside 1 same folder.
2. Before running the program, please install all the required packages listed in the requirements.txt by running 'pip install {package name}' in the terminal/command prompt or simply create a virtual environment if you are using Visual Studio code.
3. Now run the command: 'python -m uvicorn main:app --reload' in the terminal/command prompt inside the folder path to start the service.
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/8c3c24a2-dd3b-4c0d-a371-607ccda8e217)
4. The server should now be started and you can now access the program in http://localhost:8000/
5. Currently available endpoints:
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/38b5d357-2ace-424f-8040-edc1e146d801)
6. Example (in postman):
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/ec9d128e-1b52-40ce-b241-253c94bb71ab)
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/ef4d4eab-a3d0-4846-a703-2036391dc15c)
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/d88c7c9a-f75e-40d7-bf2d-d5d34e6c385c)
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/eef8de98-32f5-454b-bb0d-dc919d439e85)
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/b7db5826-0825-4b26-bc9d-62f07b7ab331)
   ![image](https://github.com/Est87/Simple-cryptocurrencies-price-tracker-web-api/assets/78466216/55dd9c8a-cb6e-49b5-97fb-4a80ad907074)

Note: coin list changes will be reflected in the coin.json file. Currently, this program only will store user data locally while the service is running, meaning if the service is stopped/restarted, all user data (sign-up and sign-in info) will be gone. However, the coin changes will be preserved in the coin.json file.
