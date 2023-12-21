from os import listdir
from fonctions_texte import *
from typing import List
from math import sqrt


def produit_scalaire(liste_gauche: List[float], liste_droite: List[float]) -> float:
    return sum(x * y for x, y in zip(liste_gauche, liste_droite))


def norm(v: List[float]) -> float:
    return sqrt(sum(map(lambda x: pow(x, 2), v)))


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
    tab_corpus=[]
    matrice_tf_idf=TF_IDF(repertoire)
    for mot in matrice_tf_idf.keys() :
        tab_corpus.append(mot) # rassemble tous les textes dans une seule liste
    phr=phrase.split()
    for mot in phr :
        if mot in tab_corpus: # compare la question à tous les textes
            tab_final.append(mot)
    return(tab_final)

#print(recherche_mot_corpus("cleaned",'je suis un bel homme nation efrei ll france quoicoubeh'))


def TF_IDF_question(question):
    # Obtenir le dictionnaire IDF du corpus
    dictionnaire_idf_corpus =IDF("cleaned")
    # Obtenir la liste des mots du corpus
    mots_corpus = list(dictionnaire_idf_corpus.keys())
    # Extraire les mots de la question
    mots_question = token_question(question)
    # Initialiser le vecteur TF-IDF de la question avec des zéros
    vecteur_tf_idf_question = [0.0] * len(mots_corpus)
    # Calculer le score TF pour chaque mot de la question
    for mot in mots_question:
        if mot in mots_corpus:
            tf_mot = mots_question.count(mot)
            idf_mot = dictionnaire_idf_corpus.get(mot, 0.0)
            tf_idf_mot = tf_mot * idf_mot
            indice_mot_corpus = mots_corpus.index(mot)
            vecteur_tf_idf_question[indice_mot_corpus] = tf_idf_mot
    return vecteur_tf_idf_question

#print(TF_IDF_question("quelle sont les valeurs de la france nation ?",))


def similarite(L, R):
    return produit_scalaire(L, R) / (norm(L) * norm(R))


def matrice_corpus_a_partir_question(question, corpus):
    dictionnaire_tf_idf_corpus = TF_IDF(corpus)
    mots_corpus = list(dictionnaire_tf_idf_corpus.keys())
    mots_partages = recherche_mot_corpus(corpus, question)
    nombre_documents = len(dictionnaire_tf_idf_corpus[mots_partages[0]])
    matrice_corpus = [[] for _ in range(nombre_documents)]

    for mot in mots_partages:
        for indice_document, valeur_tf_idf_mot in enumerate(dictionnaire_tf_idf_corpus[mot]):
            matrice_corpus[indice_document].append(valeur_tf_idf_mot)

    return matrice_corpus

#print(matrice_corpus_a_partir_question("me dire comment une nation peut-elle prendre soin du climat", "cleaned"))


def document_pertinent(question_matrix, corpus_matrix, document_names):
    similarity_vector = [
        similarite(question_matrix, document_vector)
        for document_vector in corpus_matrix
        if not all(map(lambda x: x == 0.0, document_vector))
    ]

    return document_names[similarity_vector.index(max(similarity_vector))]


def generateur_fichier_reponse(question, corpus):
    directory = "./cleaned"
    document_names = listdir(directory)
    question_matrix = TF_IDF_question(question)
    corpus_matrix = matrice_corpus_a_partir_question(question, corpus)
    print(document_pertinent(question_matrix, corpus_matrix, document_names))


def generation_reponse(question):
    print("et je songe bien sûr à françois hollande, faisant oeuvre de précurseur avec l'accord de paris sur le climat et protégeant les français dans un monde frappé par le terrorisme.")


def affiner_reponse():
    question_starters = {"Comment": "Après analyse, ","Pourquoi": "Car, ","Peux-tu": "Oui, bien sûr!"}
    pass