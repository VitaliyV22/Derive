from flask import Flask, render_template
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen


@app.route('/index')

def index():
 
 
 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://encyclotronic.com/synthesizers/korg/prototype-one-r72/', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')

 summary = soup.find('div', class_='ipsGrid_span6')

 print(summary.text)





 return render_template ("index.html", summary =summary)



@app.route('/ms20')

def ms20():
 
 
 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://encyclotronic.com/synthesizers/korg/ms-20-r1329/', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')

 summary = soup.find('div', class_='ipsGrid_span6')

 print(summary.text)





 return render_template ("ms20.html", summary =summary)

@app.route('/poly6')

def poly6():
 
 
 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://encyclotronic.com/synthesizers/korg/polysix-r6/', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')

 summary = soup.find('div', class_='ipsGrid_span6')

 print(summary.text)





 return render_template ("poly6.html", summary =summary)

@app.route('/arp')

def arp():
 
 
 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://encyclotronic.com/synthesizers/korg/korg-arp-odyssey-rev-3-duophonic-synthesizer-r175/', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')

 summary = soup.find('div', class_='ipsGrid_span6')

 print(summary.text)





 return render_template ("arp.html", summary =summary) 


@app.route('/op6')

def op6():
 
 
 headers = {'user-agent': 'Mozilla/5.0' }
 page = requests.get('https://encyclotronic.com/synthesizers/korg/korg-opsix-fm-synthesizer-concept-design-r1934/', headers = headers)
 soup = BeautifulSoup(page.content, 'html.parser')

 summary = soup.find('div', class_='ipsGrid_span6')

 print(summary.text)





 return render_template ("op6.html", summary =summary)