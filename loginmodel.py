from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class User(BaseModel):
    id: Optional[str] = uuid4().hex
    email: str
    password: str
    password_confirmation: str
    logged_in: Optional[str] = "No"
    access_token: Optional[str] = ""
    
class Login(BaseModel):
	email: str
	password: str
      
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

class Coin(BaseModel):
    id: Optional[str] = ""
    rank: Optional[str] = ""
    symbol: Optional[str] = ""
    name: str
    supply: Optional[str] = ""
    maxSupply: Optional[str] = ""
    marketCapUsd: Optional[str] = ""
    volumeUsd24Hr: Optional[str] = ""
    priceUsd: str
    changePercent24Hr: Optional[str] = ""
    vwap24Hr: Optional[str] = ""

