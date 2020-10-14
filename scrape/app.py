
app = Flask(__name__)
from flask import Flask
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen

@app.route('/')

def index():
    

    headers = {'user-agent' : 'Mozilla/5.0'}
    page = requests.get("https://www.efficientdrinker.com/beer/", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    a =soup.find_all('td', class_="column-1")[7]
    b =soup.find_all('td', class_="column-3")[0]
    textb= b.text
    texta= a.text
    print (texta)
    print (textb)

    return render_template("index.html", text = print)





