import urllib
import urllib.request
url = 'https://www.google.com.br'
try:
    print(f'\n\tO site {url} esta ', end='')
    site = urllib.request.urlopen(url)
except urllib.error.URLError:
    print('\033[31mINDISPONIVEL\033[m')
else:
    print('\033[32mACESSIVEL\033[m')
    print(site.read())

''' OUTRA SOLUÇÂO
import requests
url = 'https://www.google.com.br'
try:
    print(f'\n\tO site {url} esta ', end='')
    if requests.get(url).status_code == 200:
        pass
except Exception:
    print('\033[31mINDISPONIVEL\033[m')
else:
    print('\033[32mACESSIVEL\033[m')
'''