# The challenge: There is a list of 460k English words on Github that we would like you to first fetch, then use this list to crawl over the first 200 words to determine which are valid URI’s (aka github.com/*WORD*) and write the valid words and paths to file. Once implemented what optimizations can you make to determine valid paths?  

# Word list: https://raw.githubusercontent.com/dwyl/english-words/master/words.txt  

# At the end of the interview the candidate submits their code and results to interviews@allyrobotics.com  

from urllib import response
import requests

result = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')

resultList = result.text.split('\n')

url = 'https://github.com/'
correctList = []

for word in resultList[:200]:
    response = requests.get(url+word)
    print(response.status_code, word)
    if response.status_code == 200:
        correctList.append(word)

with open('correct_uris.txt', 'w') as f:
    for word in correctList:
        f.write(f"{word}, {url+word}, \n")
