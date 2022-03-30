import requests
url_main = 'https://kraken.cs.toronto.edu/api/v1/molecule/'
file_main = r'early_test\temp' + '\\'
loop_counter = 1
while loop_counter <= 3:
    url = url_main + str(loop_counter)
    html_get = requests.get(url)
    file = file_main + str(loop_counter) + '.txt'
    file_open = open(file,'w')
    file_open.write(html_get.text)
    file_open.close()
    loop_counter += 1