import urllib.request

def addToText(url):
    global huge_text
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    huge_text += mybytes.decode("utf8")
    fp.close()
    print("#", end='')

links = ["https://he.wikipedia.org/wiki/%D7%9B%D7%93%D7%95%D7%A8_%D7%94%D7%90%D7%A8%D7%A5",
         "https://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%9C%D7%99_%D7%97%D7%99%D7%99%D7%9D",
         "https://he.wikipedia.org/wiki/%D7%90%D7%93%D7%9D",
         "https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A7%D7%99%D7%A4%D7%93%D7%99%D7%94_%D7%94%D7%A2%D7%91%D7%A8%D7%99%D7%AA",
         "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%A0%D7%98%D7%A8%D7%A0%D7%98",
         "https://he.wikipedia.org/wiki/%D7%93%D7%99%D7%90%D7%9C%D7%95%D7%92",
         "https://he.wikipedia.org/wiki/%D7%A1%D7%9C%D7%99%D7%97%D7%94",
         "https://he.wikipedia.org/wiki/%D7%A8%D7%92%D7%A9",
         "https://he.wikipedia.org/wiki/%D7%A1%D7%9C%D7%A0%D7%92"
         ]

huge_text = ""
for i in range(len(links)):
    link = links[i]
    addToText(link)
    print(str(i+1) + ' of ' + str(len(links)) + ' done')

heb_letters = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת', 'ן', 'ך', 'ף', 'ץ']
heb_letters.append(' ')
words = []

def getWords(text):
    copy = text
    for let in text:
        if (let in heb_letters) == False:
            copy = copy.replace(let, '')
    print('Replaced All')

    words_text = copy.split(' ')
    step = len(words_text) / 10
    c = 0
    for w in words_text:
        if (c + 1) % step:
            print('10 %')
        if (len(w) == 5) and ((w in words) == False):
            words.append(w)
        c+=1

getWords(huge_text)

import codecs

path = './words.txt'

file = codecs.open(path, "w", "utf-8")
file.write(u'\ufeff')
file.close()

with open(path, "w", encoding='utf-8') as f:
  f.write(str(words))
  print('Done')

    

    
