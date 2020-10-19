from Flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
import re

@app.route('/')

def index():
    
   headers = {'user-agent' : 'Mozilla/5.0'}
   page = requests.get("https://www.reddit.com/r/MemeEconomy/", headers=headers)
   soup = BeautifulSoup(page.content, 'html.parser')
   imgs = soup.findAll('img', attrs={'alt':'Post image'})

   imglist = []
   for img in imgs :
      link_src = img.get('src')
      imglist.append(link_src)

   picture =imglist[0]

   return render_template("index.html", picture = picture) 