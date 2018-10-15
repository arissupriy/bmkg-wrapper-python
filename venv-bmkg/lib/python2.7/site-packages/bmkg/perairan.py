from bmkg.req import simple_get
from bmkg.url import CUACA_BANDARA_AKTUAL_URL, CUACA_BANDARA_AKTUAL_URL_FORMAT, CUACA_BANDARA_PRAKIRAAN_URL
from bs4 import BeautifulSoup as bs
import urlparse
import os
import json