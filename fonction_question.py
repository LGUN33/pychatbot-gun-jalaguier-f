import os
from fonctions_texte import *

def token_question(phrase):# retourne un tableau clean

    # retire les majuscules :
    phrase_min=""
    for lettre in phrase :
        if 65<=ord(lettre)<=90 :
            phrase_min+=chr(ord(lettre)+32)
        else :
            phrase_min+=lettre

    # retire la ponctuation
    phrase_ponctu=""
    for lettre in phrase_min :
        mot=""
        if 97<=ord(lettre)<=122 :
            mot+=lettre
        else :
            mot+=" "
        phrase_ponctu+=mot

    #chaque mot est ajouté dans un tableau
    tab_mot=phrase_ponctu.split()
    return(tab_mot)

#print(token_question("salut C'est moi, fred."))



def recherche_mot_corpus (repertoire,phrase) : # retourne la liste des mots de la question qui sont dans le corpus de txt
    list_nom = {}
    tab_final=[]
    directory = "./" + repertoire
    files_names = list_of_files(directory, "txt")
    tab_corpus=[]
    for i in range(len(files_names)): # parcours des differents docs
        chemin = os.path.join(directory, files_names[i])
        with open(chemin, "r") as doc:
            contenu = doc.read()
            contenu = contenu.split()
            for mot in contenu :
                tab_corpus.append(mot) # rassemble tous les textes dans une seule liste
    phr=phrase.split()
    for mot in phr :
        if mot in tab_corpus: # compare la question à tous les textes
            tab_final.append(mot)
    return(tab_final)

#print(recherche_mot_corpus("cleaned",'je suis un chien homme nation ll france quoicoubeh'))

def TF_IDF_question () :
    pass


print(TF('je suis un chien homme nation ll france quoicoubeh'))



