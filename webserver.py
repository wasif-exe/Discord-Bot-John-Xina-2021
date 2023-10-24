from flask import Flask, render_template
import random
from threading import Thread
no =random.randint(1,100)
app = Flask('')
@app.route('/')
def home():
    return f"John Cena YOU CANT SEE ME. Yes I am hosted in this webserver. Random number {no}"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start() 