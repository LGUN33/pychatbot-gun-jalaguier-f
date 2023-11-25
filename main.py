import os
import math


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def recup_nom(liste):
    nom=[]
    for elt in liste:
        president=elt[11:-4]
        code_asci = ord(president[-1])
        if code_asci >= 48 and code_asci <= 57:
            nom.append(president[0:-1])
        else:
            nom.append(president)
    nom=set(nom)
    return nom

def ajout_prenom(list):
    nom=recup_nom(list)
    nomprenom={}
    for elt in nom:
        nomprenom[elt]=1
    nomprenom['Chirac']='Jacques'
    nomprenom['Giscard dEstaing']='Valéry'
    nomprenom['Hollande']='François'
    nomprenom['Macron']='Emmanuel'
    nomprenom['Mitterrand']='François'
    nomprenom['Sarkozy']=('Nicolas')
    print(nomprenom)

def TF(ch):
    TF={}
    mot=''
    for elt in ch:
        if ord(elt) != 32 :
            mot+=elt
            if elt==ch[-1]:
                if mot not in TF:
                    TF[mot]= 1
                else:
                    TF[mot]+=1
        elif ord(elt)==32 :
            if mot not in TF:
                TF[mot]=1
            else:
                TF[mot]+=1
            mot=''
    return TF

def IDF(repertoire):
    directory = "./",repertoire
    files_names = list_of_files(directory, "txt")
    taille= len(files_names)
    list_mot=[]
    for elt in files_names:
        with open(elt, "r") as doc:
            contenu = doc.read()
            contenu=contenu.split()
            list_mot+=contenu
    list_mot=set(list_mot)
    IDF={}
    for mot in list_mot:
        occurence=0
        for elt in files_names:
            with open(elt, "r") as doc:
                contenu = doc.read()
                if mot in contenu:
                    occurence+=1
        score=math.log10((taille/occurence)+1)
        IDF[mot]=score
    return IDF




directory = "./speeches"
files_names = list_of_files(directory, "txt")


ajout_prenom(files_names)

with open('doc.txt', "r")as ch:
     c = ch.read()
TF(c)

print("d")