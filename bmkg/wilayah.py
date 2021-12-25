from bmkg.req import simple_get
from bmkg.url import CUACA_URL
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import os
import json

class Wilayah(object):
    provinsi = list()
    kabupaten = list()
    URL = CUACA_URL

    def __init__(self):
        pass
    
    def get_provinsi(self):
        raw_html = simple_get(self.URL)
        html = bs(raw_html, 'html.parser')

        for div in html.findAll('div', {'class': 'list-cuaca-provinsi'}):
            for a in div.findAll('a'):
                text = a.text
                link = a['href']
                query = urlparse.urlparse(link).query
                url = os.path.join(os.path.split(CUACA_URL)[0], link)
                
                self.provinsi.append({
                    "name": text,
                    "link": link,
                    "url": url,
                    "code": urlparse.parse_qs(query)['Prov'][0]
                })

        return self.provinsi
    
    def get_kabupaten(self):
        for prov in self.provinsi:
            raw_kab = simple_get(prov['url'])
            html = bs(raw_kab, 'html.parser')
            
            div = html.find('div', {'id': 'TabPaneCuaca1'})

            table = div.find('table', {'class': 'table-prakicu-provinsi'})

            for a in table.findAll('a'):
                text = a.text
                link = a['href']
                query = urlparse.urlparse(link).query
                url = os.path.join(os.path.split(CUACA_URL)[0], link)

                self.kabupaten.append({
                    "prov": prov['code'],
                    "name": text,
                    "link": link,
                    "url": url,
                    "code": urlparse.parse_qs(query)['AreaID'][0]
                })
        
        return self.kabupaten
