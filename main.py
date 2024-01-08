from fastapi import FastAPI
from database import conn
from usermodel import Users
from loginmodel import User, Login, Coin
from sqlalchemy import text
from jwttoken import create_access_token
from currency_converter import CurrencyConverter
from fastapi.encoders import jsonable_encoder

import decimal
import os
import json

app = FastAPI()

coinsFilename = "coin.json"
coinsDatabase = []

if os.path.exists(coinsFilename):
    with open(coinsFilename, "r") as f:
        coinsDatabase = json.load(f)

@app.get("/")
async def home():
    return {"message": "Welcome to Cryptocurrencies price tracker! Please sign in or sign up first."}

@app.get("/users")
async def retrieve_users():
    checkEmail = conn.execute(text('select * from Users Where email = "id1@gmail.com"'))
    for row in checkEmail:
        return row.password

@app.post("/signup")
async def signup(user: User):
    inputtedEmail = {'inputtedEmail': user.email}
    checkEmail = conn.execute(text('select * from Users Where email = :inputtedEmail'), inputtedEmail)

    inputtedPassword = user.password
    inputtedPasswordConfirmation = user.password_confirmation

    checkExistLoggedInUser = conn.execute(text('select * from Users Where logged_in = "Yes"'))

    if (len(checkExistLoggedInUser.fetchall()) > 0):
        return {"message": "Please log out first before creating a new account"}

    if (len(checkEmail.fetchall()) > 0):
        return {"message": "User with this email already exists! Please try again with another email."}
    else:
        if (inputtedPasswordConfirmation != inputtedPassword):
            return {"message": "Password and password confirmation mismatch!"}
        else:
            conn.execute(Users.insert().values(
                id = user.id,
                email = user.email,
                password = user.password,
                password_confirmation = user.password_confirmation
            ))
            return {"message": "Successfully created account!", "email": user.email, "password": user.password, "userid": user.id}
    
@app.post("/signin")
async def signin(user: Login):
    inputtedEmailandPassword = {'inputtedEmail': user.email, 'inputtedPassword': user.password}
    checkEmail = conn.execute(text('select * from Users Where email = :inputtedEmail'), inputtedEmailandPassword)
    savedPassword = conn.execute(text('select * from Users Where email = :inputtedEmail and password = :inputtedPassword'), inputtedEmailandPassword)

    checkExistLoggedInUser = conn.execute(text('select * from Users Where logged_in = "Yes"'))

    userpw = ""
    for row in savedPassword:
        userpw = row.password
    
    if (len(checkExistLoggedInUser.fetchall()) > 0):
        return {"message": "You already logged in! Please log out first."}

    if (len(checkEmail.fetchall()) == 0):
        return {"message": "User with this email is not registered yet!"}
    else:
        if (user.password != userpw):
            return {"message": "Wrong Password!"}
        else:
            access_token = create_access_token(data={"email": user.email, "password": user.password})
            conn.execute(Users.update().values(
                logged_in = "Yes",
                access_token = access_token
            ).where(Users.c.email == user.email))
            return {"message": "Successfully login, Welcome to the Cryptocurrencies price tracker!", 
                    "email": user.email, "password": user.password,
                    "access_token": access_token,"token_type": "bearer"}

@app.get("/signout")
async def signout():
    checkExistLoggedInUser = conn.execute(text('select * from Users Where logged_in = "Yes"'))

    loggedInUserEmail = ""
    for loggedInUser in checkExistLoggedInUser:
        loggedInUserEmail = loggedInUser.email

    conn.execute(Users.update().values(
        logged_in = "No",
    ).where(Users.c.email == loggedInUserEmail))

    return {"message": "You have logged out.", "email": loggedInUserEmail}

@app.get("/show_coin_list")
async def show_coin_list():
    checkExistLoggedInUser = conn.execute(text('select * from Users Where logged_in = "Yes"'))
    if (len(checkExistLoggedInUser.fetchall()) == 0):
        return {"message": "Only logged in user can view the coins list! Please log in first."}

    coinName = ""
    coinPrice = ""
    coinNameAndPriceList = []
    cr = CurrencyConverter()
    for coins in coinsDatabase:
        coinName = coins["name"]
        coinPrice = cr.convert(coins["priceUsd"],'USD','IDR')
        coinNameAndPriceList.append({"name": coinName, "priceIDR": coinPrice})
    return {"coins": coinNameAndPriceList}

@app.post("/add_coin")
async def add_coin(coin: Coin):
    checkExistLoggedInUser = conn.execute(text('select * from Users Where logged_in = "Yes"'))
    if (len(checkExistLoggedInUser.fetchall()) == 0):
        return {"message": "Only logged in user can add coin to tracker! Please log in first."}
    
    coin = jsonable_encoder(coin)
    for obj in coinsDatabase:
        if coin["name"] == obj["name"]:
            return {"message": "Coin with that name already exist in the list! Please insert a different coin"}
    coinsDatabase.append(coin)
    with open(coinsFilename, "w") as f:
        json.dump(coinsDatabase, f, indent=4)
    return {"message": f"Coin '{coin['name']}' was added."}

@app.delete("/delete_coin")
async def delete_coin(name: str):
    checkExistLoggedInUser = conn.execute(text('select * from Users Where logged_in = "Yes"'))
    if (len(checkExistLoggedInUser.fetchall()) == 0):
        return {"message": "Only logged in user can delete coin to tracker! Please log in first."}

    counter = 0
    for coins in coinsDatabase:
        if (coins.get('name') == name):
            coinsDatabase.remove(coins)
            counter += 1
        with open(coinsFilename, "w") as f:
            json.dump(coinsDatabase, f, indent=4)
    if (counter == 0):
        return {"message": f"Coin '{name}' does not exist in the list."}
    return {"message": f"Coin '{name}' has been removed from the list."}