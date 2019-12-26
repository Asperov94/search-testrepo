from flask import Flask, request
import json
import re


app = Flask(__name__)
novosty = ["деревья на cадовом кольце","добрый автобус", "выставка it-технологий"]
eda = ["рецепт борща", "яблочный пирог", "тайская кухня"]
tovar = ["дети капитана гранта", "зимние шины", "тайская кухня"]
    
#print(tovar[1])

#######set1 >= set2 

def slovo(dfg):
    s=' '
    z=3
    for i in range(3):
        while dfg >= set(novosty[i].split(' ')) and z!=2:
            #print('novosty')
            s=s+' NOVOSTY'
            z=2
            #print('RABOTERTTTWEFSDFSDFSDFKSDSDGK')
        while dfg >= set(eda[i].split(' ')) and z!=1:
            print('eda')
            s=s+' EDA'
            z=1
        if dfg >= set(tovar[i].split(' ')) and z!=0:
            print('tovar')
            s=s+' TOVAR'
            z=0
        else:
            print('=====================')
            #print(dfg)
            #print(novosty[1])
    return(s)
#def novosty(words):
#    lst = words.split(' ') 
#    words=set(lst)
#    result=list(set(Ans) & set(Word))


@app.route('/', methods=['POST'])
def hello_world():
    x = str(request.get_json(force=True))
    d=x.rfind(':')
    s=x[d::]
    reg = re.compile('[^a-zA-Zа-я-А-Я ]')
    a=reg.sub(' ', s)
    a = a.lower()
    a = a.split(' ')
    #print(a)
    a = set(a)
    #print(slovo(a))

    #lst = a.split(' ')
    #wor = set(lst)
    #slovo(a)
    #print(a)
    return(slovo(a))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
