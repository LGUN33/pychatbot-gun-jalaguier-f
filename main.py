from fonctions import *
import os

os.system("cls")

print("\033[1;31m\nBienvenue sur 'My First Chat Bot' l'intelligence artificielle à la pointe de la technologie (équivalent de ChatGPT® 6) développée par Louis Gun et Frédéric Jalaguier")
print("\033[1;34m\nVoici la liste des différentes actions que vous pouvez faire : \n")
print("\033[1;34mTappez 1 pour : "+"\033[1;35mAfficher la liste des mots les moins importants dans tous les documents")
print("\033[1;34mTappez 2 pour : "+"\033[1;35mAfficher le(s) mot(s) ayant le score TD-IDF le plus élevé")
print("\033[1;34mTappez 3 pour : "+"\033[1;35mAfficher le(s) mot(s) le(s) plus répété(s) par le président Chirac")
print("\033[1;34mTappez 4 pour : "+"\033[1;35mAfficher le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
print("\033[1;34mTappez 5 pour : "+"\033[1;35mAfficher le premier président à parler du climat et/ou de l’écologie")
print("\033[1;34mTappez 6 pour : "+"\033[1;35mAfficher le(s) mot(s) que tous les présidents ont évoqués")


réponse = input("\033[1;31mSaisir votre choix : ")

while réponse != '1' and réponse != '2' and réponse != '3' and réponse != '4' and réponse != '5' and réponse != '6' :
    print("Merci de saisir un chiffre entre 1 et 6")
    réponse = input("\033[1;31mSaisir votre choix : ")

réponse=int(réponse)
print("\033[1;31m")

if réponse == 1 :
    print ("\033[1;37mVoici la liste des mots les moins importants dans tous les documents : ")
    print(mot_non_important("cleaned"))

elif réponse == 2 :
    print("\033[1;37mVoici le(s) mot(s) ayant le score TD-IDF le plus élevé : ")
    print(plusgrand_TF_IDF("cleaned"))

elif réponse == 3:

    print("\033[1;37mVoici le(s) mot(s) le(s) plus répété(s) par le président Chirac : ")
    print(mot_chirac())

elif réponse == 4:
    print("\033[1;37mVoici le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois : ")
    print(nation("cleaned"))

elif réponse == 5:
    print("\033[1;37mVoici le premier président à parler du climat et/ou de l’écologie : ")
    print("Fonctionnalité à venir...")

elif réponse == 6:
    print("\033[1;37mVoici le(s) mot(s) que tous les présidents ont évoqués : ")
    print("Fonctionnalité à venir...")
    print(mot_dit("cleaned"))









