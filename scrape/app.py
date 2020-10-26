from flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
import re

@app.route('/')

def index():

 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://en.wikipedia.org/wiki/Epidemiology_of_depression', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')
 a = soup.find_all('li')
 print (a)


 return render_template ("index.html")