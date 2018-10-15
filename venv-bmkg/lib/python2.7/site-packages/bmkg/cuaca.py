from bmkg.req import simple_get
from bmkg.url import CUACA_URL_FORMAT
from bs4 import BeautifulSoup as bs

class PrakiraanCuaca(object):
    area_id = None
    prov = None
    results = list()
    URL = None

    def __init__(self, area_id, prov):
        self.area_id = area_id
        self.prov = prov
        self.URL = CUACA_URL_FORMAT.format(areaid=self.area_id, prov=self.prov)

    def get(self):
        raw_html = simple_get(self.URL)
        html = bs(raw_html, 'html.parser')
        kab = html.find('div', {'class': 'prakicu-kabkota'})
        
        nav_tab = []

        for li in kab.ul.findAll('li'):
            by_id = kab.find('div', {'id': li.a['href'].replace('#', '')})
            for kota in by_id.findAll('div', {'class': 'prakicu-kota'}):
            
                waktu = kota.h2.text

                kiri = kota.find('div', {'class': 'kiri'})
                icon = kiri.img['src']
                cuaca = kiri.p.text
                kanan = kota.find('div', {'class': 'kanan'})
                suhu = kanan.h2.text
                p_all = []
                p = kanan.findAll('p')
                p_atas = p[0] if len(p) >= 2 else None

                for i in p_atas.findAll('i'):
                    i.replaceWith(" ")

                p_atas = str(u''.join(p_atas.text).encode('utf-8').strip()).split(' ')
                suhu_min = str(p_atas[0]) if len(p_atas) >= 3 else None
                suhu_max = p_atas[1] if len(p_atas) >= 3 else None
                lembab = p_atas[2] if len(p_atas) >= 3 else None


                p_bawah = p[1] if len(p) >= 2 else None
                p_bawah.br.replaceWith("-")
                for i in p_bawah.findAll('i'):
                    i.replaceWith(" ")

                p_bawah = str(u''.join(p_bawah.text).encode('utf-8').strip()).split('-')
                angin = p_bawah[0] if len(p_bawah) >= 2 else None
                arah_angin = p_bawah[1] if len(p_bawah) >= 2 else None

                self.results.append({
                    "hari":li.a.text,
                    "area_id": self.area_id,
                    "prov": self.prov,
                    "waktu": waktu,
                    "icon": icon,
                    "cuaca": cuaca,
                    "suhu": suhu,
                    "suhu_min": suhu_min,
                    "suhu_max": suhu_max,
                    "lembab": lembab,
                    "angin": angin,
                    "arah_angin": arah_angin
                })

        return self.results  
        



    
    


    

