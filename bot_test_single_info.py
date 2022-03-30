import requests
url = 'https://kraken.cs.toronto.edu/api/v1/molecule/1'
strhtml = requests.get(url)
file = open('D:/calc/optool/early_test/temp/test.txt','w')
file.write(strhtml.text)
file.close()