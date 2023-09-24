from dotenv import load_dotenv
load_dotenv()
import os

url = os.getenv("url")
def create_customers(count):
    for i in range(count):
        print(i,url)