from bmkg.req import simple_get
from bmkg.url import CUACA_BANDARA_AKTUAL_URL, CUACA_BANDARA_AKTUAL_URL_FORMAT, CUACA_BANDARA_PRAKIRAAN_URL
from bs4 import BeautifulSoup as bs
import urlparse
import os
import json
from bmkg.errors import MaxMinPrakiraan


class BandaraCuacaAktual(object):
    results = list()
    URL = None
    raw_html = None
    html = None

    def get(self):
        self.raw_html = simple_get(CUACA_BANDARA_AKTUAL_URL)
        self.html = bs(self.raw_html, 'html.parser')

        tbody = self.html.table.tbody
        for tr in tbody.findAll('tr'):
            td = tr.findAll('td')
            self.results.append({
                "nama": td[1].text,
                "waktu_pengamatan": td[2].text,
                "angin": {
                    "arah_dari": td[3].text,
                    "kecepatan": td[4].text
                },
                "jarak_pandang": td[5].text,
                "cuaca": td[6].text,
                "suhu": td[7].text,
                "titik_embun": td[8].text,
                "tekanan_udara": td[9].text
            })
        
        return self.results

class BandaraCuacaPrakiraan(object):
    results = list()
    URL = None
    raw_html = None
    html = None
 
    def get(self, waktu_prakiraan=1):
        if waktu_prakiraan < 1 or waktu_prakiraan > 12:
            raise MaxMinPrakiraan("Waktu Prakiraan Minium 1 dan Maximum 12")
        
        self.URL = CUACA_BANDARA_PRAKIRAAN_URL.format(waktu_prakiraan)
        self.raw_html = simple_get(self.URL)
        self.html = bs(self.raw_html, 'html.parser')

        tbody = self.html.table.tbody
        for tr in tbody.findAll('tr'):
            td = tr.findAll('td')
            self.results.append({
                "nama": td[1].text,
                "waktu_prakiraan": td[2].text,
                "angin": {
                    "arah_dari": td[3].text,
                    "kecepatan": td[4].text
                },
                "jarak_pandang": td[5].text,
                "cuaca": td[6].text,
                "probabilitas": td[7].text
            })
        
        return self.results




