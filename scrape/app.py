from flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

@app.route('/')

def index():
 #sound= "sound"
 #music= "music"
 #electronic= "electronic"
 #synthesizers= "synthesizers"
 #Moog= "moog"


 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://en.wikipedia.org/wiki/Sound', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')
 
 title = soup.find("title")
 paragraph = soup.find("p")

 print(title.get_text()) 
 print(paragraph.get_text())




 return render_template ("sound.html", title =title, paragraph = paragraph)