# BMKG Wrapper for Python

## Supported Version python 2.7

Versi ini menyediakan API untuk pengambilan data sebagai berikut :
- Data Wilayah (Kabupaten dan Provinsi)
- CUACA per Kabupaten (http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?AreaID={areaid}&Prov={prov})
- Cuaca Aktual Bandara (http://www.bmkg.go.id/cuaca/cuaca-aktual-bandara.bmkg)
- Cuaca Prakiraan Bandara (http://www.bmkg.go.id/cuaca/prakiraan-cuaca-bandara.bmkg?s={})


## Penggunaan

### Install

``` pip install bmkg-wrapper ```

### Ambil Data Provinsi dan Kabupaten

``` 
from bmkg.wilayah import Wilayah

wil = Wilayah()

prov = wil.get_provinsi()

```
return provinsi
```
[{'code': u'01',
  'link': u'prakiraan-cuaca-indonesia.bmkg?Prov=01&NamaProv=Aceh',
  'name': u'Aceh',
  'url': u'http://www.bmkg.go.id/cuaca/prakiraan-cuaca-indonesia.bmkg?Prov=01&NamaProv=Aceh'},
 {'code': u'02',
  'link': u'prakiraan-cuaca-indonesia.bmkg?Prov=02&NamaProv=Bali',
  'name': u'Bali',
  'url': u'http://www.bmkg.go.id/cuaca/prakiraan-cuaca-indonesia.bmkg?Prov=02&NamaProv=Bali'},
 ...
 ...
 ]
```


Data akan selalu di perbarui setiap saat.



terimakasih atas bantuan yang diberikan !!!

terimakasih kepada : bmkg.go.id

