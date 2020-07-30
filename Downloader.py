import urllib.request
import os

print('Fazendo o download...')

url = 'https://google.com'
urllib.request.urlretrieve(url, 'Google.html')

os.system('cls')
print('Download concluído!')
input()
