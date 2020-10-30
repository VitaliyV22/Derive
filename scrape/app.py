from flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen


@app.route('/')

def sound():
 


 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://en.wikipedia.org/wiki/Sound', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')
 
 
 title = soup.find("title")
 paragraph = soup.find_all("p")
 
 print(title.get_text())
 for p in paragraph: 
    print(p.text())





 return render_template ("index.html", title =title, paragraph = paragraph)