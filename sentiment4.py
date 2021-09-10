#Sentiment Analysis Tool
import collections
import matplotlib.pyplot as plt
import string
from stop_words import get_stop_words
import operator
import re
import os

a='junio2020.txt'

def read_file(file=a):
    file=open(file,'r',encoding="utf8")
    text=file.read().lower()
    file.close()
    return text

stop_words = get_stop_words('english')
positive=read_file('positive-words.txt').split('\n')
negative=read_file('negative-words.txt').split('\n')
p=0
pintxt=[]
n=0
nintxt=[]
e=0  #neutral
eintxt=[]

b= read_file()

def file_to_sentences(text=b):
    text=text.replace(","," ")
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    return sentences
sentences=file_to_sentences()

def file_to_text(file=b):
    file=file.translate(str.maketrans('','',string.punctuation)).lower()
    file=file.split()
    return file
text=file_to_text()

for i in text:
    if i in positive:
        p+=1
        pintxt.append(i)
    elif i in negative:
        n+=1
        nintxt.append(i)
    else:
        e+=1
        eintxt.append(i)

def procent(object,text):
    m=object/len(text)*100
    m=format(float(m),'.2f')
    return m+'%'

def print_percentage():
    print('Sentiment distribution for',a)
    print('Positive:',(p),'Negative:',(n),'Neutral:',(e),'Total:',(p+n+e),'%Positive:', procent(p, text), '%Negative:', procent(n, text), '%Neutral:' + procent(e, text))

def pie_chart():
    dane=[p,n,e]
    labels=['Positive','Negative','Neutral']
    plt.pie(dane,labels=labels,autopct='%1.2f%%',colors=['g','r','gold'])
    k='Sentiment Analysis for: '+a
    plt.title(k)
    plt.show()
counterp = collections.Counter(pintxt)
countern = collections.Counter(nintxt)
pmc=counterp.most_common()#positivo
nmc=countern.most_common()#negativo

# ordenar listas descendentes
pmc.sort(key=operator.itemgetter(1),reverse=True)
nmc.sort(key=operator.itemgetter(1),reverse=True)

#function imprime el número dado de palabras positivas más populares en el texto.
#por defecto enumera todas las palabras positivas en el texto
def pos_words_list(n=len(pmc)):
    słowo = [x[0] for x in pmc]
    ilość = [x[1] for x in pmc]
    for i in range(n):
        print("{:-<15} {}".format(słowo[i], ilość[i]))

#function imprime el número dado de palabras negativas más comunes en el texto.
#por defecto enumera todas las palabras negativas en el texto
def neg_words_list(n=len(nmc)):
    słowo = [x[0] for x in nmc]
    ilość = [x[1] for x in nmc]
    for i in range(n):
        print("{:-<15} {}".format(słowo[i], ilość[i]))


def top_5_words(list):
    x_val = [x[0] for x in list]
    if len(list)>5:
        top_5_words=[]
        for i in range(5):
            top_5_words.append(x_val[i])
        return top_5_words
    else:
        return x_val

def top_5_numbers(list):
    y_val = [x[1] for x in list]
    if len(list)>5:
        top_5_numbers=[]
        for i in range(5):
            top_5_numbers.append(y_val[i])
        return top_5_numbers
    else:
        return y_val

def pos_chart():
    plt.bar(top_5_words(pmc),top_5_numbers(pmc),color='g')
    plt.show()

def neg_chart():
    plt.bar(top_5_words(nmc),top_5_numbers(nmc),color='r')
    plt.show()

text1=file_to_text(b)
def stopped_text(text1=text1):
    for i in text1:
        if i in stop_words:
            text1.remove(i)
    return text1

stop = stopped_text()
ps=0
ns=0
es=0
for i in stop:
    if i in positive:
        ps+=1
    elif i in negative:
        ns+=1
    else:
        es+=1

def print_stop_percentage():
    print('Sentiment distribution for',a,'without stop words')
    print('Positive:', procent(ps, stop), 'Negative:', procent(ns, stop), 'Neutral:' + procent(es, stop))

def pie_stop_chart():
    dane=[ps,ns,es]
    labels=['Positive','Negative','Neutral']
    plt.pie(dane,labels=labels,autopct='%1.2f%%',colors=['g','r','gold'])
    k=('Sentiment Analysis without stop words for: '+a)
    print(k)
    plt.title(k)
    plt.show()

def sent_key(key):
    key_list=[]
    for sentence in sentences:
        c=sentence.split()
        if key in c:
            key_list.append(sentence)
    str=''.join(key_list)
    key_list=str.split()
    return key_list

q=True
while q:
    print("""MENU DE OPCIONES:
1 - MOSTRAR LA DISTRIBUCIÓN DEL SENTIMIENTO EN UN TEXTO
2 - MOSTRAR UN GRÁFICO CIRCULAR DE DISTRIBUCIÓN DE SENTIMIENTOS
3 - MOSTRAR UNA LISTA DE TODAS LAS PALABRAS POSITIVAS
4 - MOSTRAR UNA LISTA DE TODAS LAS PALABRAS NEGATIVAS
5 - MOSTRAR UN GRÁFICO CON LAS PRINCIPALES PALABRAS POSITIVAS
6 - MOSTRAR UN GRÁFICO CON LAS PRINCIPALES PALABRAS NEGATIVAS
7 - MOSTRAR LA DISTRIBUCIÓN DE SENTIMIENTOS PARA EL TEXTO SIN PALABRAS REDUNDANTES
8 - MOSTRAR UN GRÁFICO CIRCULAR DE DISTRIBUCIÓN DE OPINIONES PARA TEXTO SIN PALABRAS REDUNDANTES
9 - MOSTRAR LA DISTRIBUCIÓN DEL SENTIMIENTO PARA LAS ORACIONES CON LA PALABRA CLAVE PROPORCIONADA
10 - SALIR""")
    q=int(input("""SELECCIONA LA OPCION DESEADA:"""))
    if q==1:
       print_percentage()
    elif q == 2:
        pie_chart()
    elif q == 3:
        pos_words_list()
    elif q == 4:
        neg_words_list()
    elif q == 5:
        pos_chart()
    elif q == 6:
        neg_chart()
    elif q == 7:
        print_stop_percentage()
    elif q == 8:
        pie_stop_chart()
    elif q == 9:
        key = input("Provide a keyword:").lower()
        pk = 0
        nk = 0
        ek = 0
        key_list=sent_key(key)
        if len(key_list)>0:
            for i in key_list:
                if i in positive:
                    pk += 1
                elif i in negative:
                    nk += 1
                else:
                    ek += 1
            print('Sentiment distribution for',a,'for sentences with key word')
            print('Positive:', procent(pk, key_list), 'Negative:', procent(nk, key_list), 'Neutral:' + procent(ek, key_list))
        else:
            print("The word does not occur")
    elif q == 10:
        print("Adiós!")
        q=None
    else:
        print("Sorry, I don't understand.Provide a number from 1 to 10")
