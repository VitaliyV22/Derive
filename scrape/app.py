from flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen


@app.route('/')

def sound():
 
 
 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://encyclotronic.com/synthesizers/korg/prototype-one-r72/', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')

 summary = soup.find('div', class_='ipsGrid_span6')

 print(summary.text)





 return render_template ("index.html", summary =summary)