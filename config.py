import os
from dotenv import load_dotenv

load_dotenv()

    

class Config:
    SECRET_KEY = os.environ.get('7370f5da0a450b0e92c424b9458826e4c710cb327e00985261e81284c24e4c0e')
    SQLALCHEMY_DATABASE_URI = os.getenv('sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('2a8d7c8ad4eb6f6b6719fe88f6ef901238778c8678bc3ea87452c856b0f0ca04b026f209c84a28f78d21a13d1069a0c78137d77fb6ef2ccdc0cf03797007bfcf')
