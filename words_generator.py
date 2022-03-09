import urllib.request

def addToText(url):
    global huge_text
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    huge_text += mybytes.decode("utf8")
    fp.close()

links = ["https://he.wikipedia.org/wiki/%D7%9B%D7%93%D7%95%D7%A8_%D7%94%D7%90%D7%A8%D7%A5",
         "https://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%9C%D7%99_%D7%97%D7%99%D7%99%D7%9D",
         "https://he.wikipedia.org/wiki/%D7%90%D7%93%D7%9D",
         "https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A7%D7%99%D7%A4%D7%93%D7%99%D7%94_%D7%94%D7%A2%D7%91%D7%A8%D7%99%D7%AA",
         "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%A0%D7%98%D7%A8%D7%A0%D7%98",
         "https://he.wikipedia.org/wiki/%D7%93%D7%99%D7%90%D7%9C%D7%95%D7%92",
         "https://he.wikipedia.org/wiki/%D7%A1%D7%9C%D7%99%D7%97%D7%94",
         "https://he.wikipedia.org/wiki/%D7%A8%D7%92%D7%A9",
         "https://he.wikipedia.org/wiki/%D7%A1%D7%9C%D7%A0%D7%92",
         "https://www.adamtsair.co.il/%D7%A1%D7%99%D7%A4%D7%95%D7%A8%D7%99%D7%9D-%D7%9C%D7%99%D7%9C%D7%93%D7%99%D7%9D/",
         "https://www.adamtsair.co.il/%d7%9e%d6%b4%d7%99%d7%95%d6%b9%d7%9e%d6%b8%d7%a0%d7%95%d6%b9-%d7%a9%d7%81%d6%b6%d7%9c-%d7%97%d6%b2%d7%aa%d7%95%d6%bc%d7%9c-%d7%96%d6%b6%d7%91%d6%b6%d7%9c/",
         "https://www.adamtsair.co.il/%d7%90%d6%b7%d7%a8%d6%b0%d7%9e%d7%95%d6%b9%d7%9f-%d7%94%d6%b7%d7%98%d6%b7%d7%91%d6%bc%d6%b7%d7%a2%d6%b7%d7%aa/",
         "https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C"
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
    step = int(len(text) / 10)
    c = 0
    for let in text:
        if ((c + 1) % step) == 0:
            print(str((c+1)/step) + ' %')
        if (let in heb_letters) == False:
            copy = copy.replace(let, '')
        c+=1
    print('Replaced All')

    words_text = copy.split(' ')
    step = int(len(words_text) / 10)
    c = 0
    for w in words_text:
        if ((c + 1) % step) == 0:
            print(str((c+1)/step) + ' %')
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

    

    
