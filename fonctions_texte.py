import os
import math


def convertir_minuscule(fichi) :

    # Definir l'accès du fichier d'origine / arrivée
    fichier_origine = 'speeches/'+fichi
    fichier_cleaned = 'cleaned/'+fichi

    f_cl = open(fichier_cleaned, "w")

    with open(fichier_origine, "r") as f_or:
        contenu = f_or.readlines()
    for ligne in contenu:
        for i in range (len(ligne)) :
            if 65 <= ord(ligne[i]) <= 90 :
                f_cl.write(chr(ord(ligne[i]) + 32))
            else:
                f_cl.write(ligne[i])
    f_cl.close()


def supprime_ponctuation(fichi) :
    fichier = 'cleaned/'+fichi

    # Partie 1 : READ le fichier -> Chaque mot filtré va dans une liste
    f = open(fichier, "r")
    txt_filtre=[]
    texte_fichier= f.read()
    ponctu=['.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', "'", '"', '<', '>', '/', '|', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '~', '`', ' ']
    mot=''
    for lettre in texte_fichier :
        if 97<=ord(lettre)<=122 or ord(lettre)>127:
            mot+=lettre
        elif lettre in ponctu :
            mot+=' '
            if mot != ' ' :
                txt_filtre.append(mot)
            mot=''
    f.close()

    # Partie 2: WRITE le fichier : Remplace le contenu du fichier par la liste
    with open (fichier, "w") as f :
        for mot in txt_filtre :
            f.write(mot)


def list_of_files(directory, extension):
    files_names = []
    # Parcours des fichiers dans le répertoire
    for filename in os.listdir(directory):
        # Vérification de l'extension du fichier
        if filename.endswith(extension):
            # Ajout du nom du fichier à la liste
            files_names.append(filename)
    return files_names


def recup_nom(repertoire):
    directory = "./" + repertoire
    liste = list_of_files(directory, "txt")
    nom = []
    # Extraction du nom des présidents à partir des noms de fichiers
    for elt in liste:
        president = elt[11:-4]
        code_asci = ord(president[-1])
        # Vérification du code ASCII du dernier caractère
        if code_asci >= 48 and code_asci <= 57:
            nom.append(president[0:-1])
        else:
            nom.append(president)
    nom = set(nom)
    return nom


def ajout_prenom(repertoire):
    nom = recup_nom(repertoire)
    nomprenom = {}
    # Initialisation du dictionnaire avec des valeurs par défaut
    for elt in nom:
        nomprenom[elt] = 1
    # Ajout de prénoms spécifiques pour certains noms de président
    nomprenom['Chirac'] = 'Jacques'
    nomprenom['Giscard dEstaing'] = 'Valéry'
    nomprenom['Hollande'] = 'François'
    nomprenom['Macron'] = 'Emmanuel'
    nomprenom['Mitterrand'] = 'François'
    nomprenom['Sarkozy'] = 'Nicolas'
    return nomprenom





def TF(ch):
    TF={}
    ch=ch.split()
    for elt in ch:
        if elt not in TF:
            TF[elt]=1
        else:
            TF[elt]+=1
    return TF





def IDF(repertoire):
    # Construire le chemin du répertoire
    directory = "./" + repertoire

    # Obtenir la liste des noms de fichiers avec l'extension "txt"
    files_names = list_of_files(directory, "txt")

    # Calculer la taille du corpus (nombre total de documents)
    taille = len(files_names)

    # Initialiser une liste pour stocker tous les mots dans le corpus
    liste_mot = []

    # Parcourir chaque fichier dans le répertoire
    for elt in files_names:
        # Construire le chemin complet du fichier
        chemin = os.path.join(directory, elt)

        # Lire le contenu du fichier
        with open(chemin, "r") as doc:
            contenu = doc.read()

            # Diviser le contenu en mots et ajouter à la liste
            contenu = contenu.split()
            liste_mot += contenu

    # Convertir la liste de mots en un ensemble pour obtenir des mots uniques
    list_mot = set(liste_mot)

    # Initialiser un dictionnaire pour stocker les scores IDF de chaque mot
    IDF = {}

    # Calculer le score IDF pour chaque mot dans le corpus
    for mot in list_mot:
        occurence = 0

        # Parcourir chaque fichier dans le répertoire
        for elt in files_names:
            # Construire le chemin complet du fichier
            chemin = os.path.join(directory, elt)

            # Lire le contenu du fichier
            with open(chemin, "r") as doc:
                contenu = doc.read()

                # Vérifier si le mot est présent dans le contenu du fichier
                if mot in contenu:
                    occurence += 1

        # Calculer le score IDF pour le mot
        score = math.log(taille / (occurence + 1))  # Ajout de 1 pour éviter une division par zéro

        # Ajouter le score IDF au dictionnaire
        IDF[mot] = score

    return IDF




def TF_IDF(repertoire):
    matrice = {}
    directory = "./" + repertoire
    files_names = list_of_files(directory, "txt")
    # Calcul de la liste de mots unique dans tous les documents
    idf = IDF(repertoire)
    for mot in idf.keys():
        L = []
        for j in range(len(files_names)):
            chemin = os.path.join(directory, files_names[j])
            with open(chemin, "r") as doc:
                contenu = doc.read()
                tf = TF(contenu)
                valeur_idf = idf.get(mot, 0)
                valeur_tf = tf.get(mot, 0)
                if valeur_tf==0:
                    L.append(0)
                else:
                    L.append(valeur_tf * valeur_idf)
        matrice[mot]=L
    return matrice




def mot_non_important(repertoire):
    # Obtenir la matrice TF-IDF du corpus
    matrice = TF_IDF(repertoire)

    # Initialiser une liste pour stocker les mots non importants
    mot = []

    # Parcourir chaque mot dans la matrice
    for key, val in matrice.items():
        j = 0

        # Chercher la première occurrence non nulle dans le vecteur TF-IDF du mot
        while j < len(matrice[key]) and val[j] == 0.0:
            j += 1

        # Si toutes les occurrences sont nulles, ajouter le mot à la liste des mots non importants
        if j == 8:
            mot.append(key)

    return mot



def plusgrand_TF_IDF(repertoire):
    # Obtenir la matrice TF-IDF du corpus
    matrice = TF_IDF(repertoire)

    # Initialiser la valeur maximale et la liste des mots ayant le score maximal
    max_score = 0
    max_mot = []

    # Parcourir chaque mot et son vecteur TF-IDF dans la matrice
    for mot, score in matrice.items():
        mot_score = 0

        # Trouver le score maximal dans le vecteur TF-IDF du mot
        for j in range(8):
            if score[j] > mot_score:
                mot_score = score[j]

        # Mettre à jour le score maximal et la liste des mots si nécessaire
        if mot_score > max_score:
            max_score = mot_score
            max_mot = [mot]
        elif mot_score == max_score:
            max_mot.append(mot)

    return max_mot, max_score



def mot_chirac():
    # Initialiser une chaîne de caractères pour stocker le contenu des fichiers
    contenu = ""

    # Parcourir les fichiers Nomination_Chirac1.txt et Nomination_Chirac2.txt
    for i in range(1, 3):
        chemin = os.path.join("./cleaned", 'Nomination_Chirac' + str(i) + '.txt')

        # Lire le contenu du fichier et ajouter à la chaîne
        with open(chemin, "r") as doc:
            contenu += doc.read()

    # Obtenir un dictionnaire de fréquence des mots (TF) à partir du contenu
    dico_mot = TF(contenu)

    # Initialiser une chaîne de caractères pour le mot avec le plus grand score TF
    mot = ""

    # Initialiser le score TF maximum
    TF_max = 0

    # Parcourir le dictionnaire de fréquence des mots
    for elt, val in dico_mot.items():
        # Trouver le mot avec le score TF maximum
        if val > TF_max:
            TF_max = val
            mot = elt

    return mot





def nation(repertoire):
    # Initialiser un dictionnaire pour stocker le nombre d'occurrences du mot "nation" pour chaque président
    list_nom = {}

    # Construire le chemin du répertoire
    directory = "./" + repertoire

    # Obtenir la liste des noms de fichiers avec l'extension "txt"
    files_names = list_of_files(directory, "txt")

    # Parcourir chaque fichier dans le répertoire
    for i in range(len(files_names)):
        chemin = os.path.join(directory, files_names[i])

        # Lire le contenu du fichier
        with open(chemin, "r") as doc:
            contenu = doc.read()

            # Diviser le contenu en mots
            contenu = contenu.split()

            # Extraire le nom du président du nom du fichier
            president = files_names[i][11:-4]
            code_asci = ord(president[-1])

            # Vérifier et ajuster le nom du président si nécessaire
            if code_asci >= 48 and code_asci <= 57:
                president = president[0:-1]

            # Initialiser le compteur d'occurrences du mot "nation" pour le président actuel
            list_nom[president] = list_nom.get(president, 0)

            # Compter le nombre d'occurrences du mot "nation" dans le contenu
            if "nation" in contenu:
                nbr = 0
                for elt in contenu:
                    if elt == "nation":
                        nbr += 1
                list_nom[president] += nbr

    # Trouver le président avec le plus grand nombre d'occurrences du mot "nation"
    max = 0
    nom_final = ""
    for nom, val in list_nom.items():
        if val > max:
            max = val
            nom_final = nom

    return list_nom, nom_final


def climat(repertoire):
    list_nom={}
    directory = "./" + repertoire
    files_names = list_of_files(directory, "txt")
    for i in range(len(files_names)):
        chemin = os.path.join(directory, files_names[i])
        with open(chemin, "r") as doc:
            contenu = doc.read()
            contenu = contenu.split()
            president = files_names[i][11:-4]
            code_asci = ord(president[-1])
            if code_asci >= 48 and code_asci <= 57:
                president = president[0:-1]
            list_nom[president]=list_nom.get(president,0)
            if "climat" in contenu :
                ind=contenu.index("climat")
                list_nom[president]+=ind
            if "écologie" in contenu :
                ind=contenu.index("écologie")
                list_nom[president]+=ind
    return list_nom


def mot_dit(repertoire):
    mot_important=[]
    matrice=TF_IDF(repertoire)
    non_important=mot_non_important(repertoire)
    for elt in non_important:
        del matrice[elt]
    for mot,val in matrice.items():
        c = True
        for i in range (1,8):
            if val[i]!="nul":
                c=True
            else:
                c=False
        if val[0]=="nul" and c==True:
            mot_important.append(mot)
        else:
            c = True
            for i in range (2,8):
                if val[i]!="nul":
                    c=True
                else:
                    c=False
            if val[1] == "nul" and val[0]!="nul" and c==True:
                mot_important.append(mot)
            else:
                c = True
                for i in range (0,6):
                    if val[i]!="nul":
                        c=True
                    else:
                        c=False
                if val[6]== "nul" and val[7]!="nul"and c==True:
                    mot_important.append(mot)
                else:
                    c = True
                    for i in range (0,7):
                        if val[i]!="nul":
                            c=True
                        else:
                            c=False
                    if val[7]=="nul" and c==True:
                        mot_important.append(mot)
                    else:
                        c = True
                        for i in range (2,6):
                            if val[i]!="nul":
                                c=True
                            else:
                                c=False
                        if val[1]=="nul" and val[6]=="nul" and val[0]!="nul" and val[7]!="nul"and c==True:
                            mot_important.append(mot)
                        else:
                            c = True
                            for i in range(1, 7):
                                if val[i] != "nul":
                                    c = True
                                else:
                                    c = False
                            if val[0]=="nul" and val[7]=="nul" and c==True:
                                mot_important.append(mot)
                            else:
                                c = True
                                for i in range(1, 6):
                                    if val[i] != "nul":
                                        c = True
                                    else:
                                        c = False
                                if val[0]=="nul" and val[6]=="nul" and val[7]!="nul" and c==True:
                                    mot_important.append(mot)
                                else:
                                    c = True
                                    for i in range(2, 7):
                                        if val[i] != "nul":
                                            c = True
                                        else:
                                            c = False
                                    if val[1]=="nul" and val[7]=="nul" and val[0]!="nul" and c==True:
                                        mot_important.append(mot)
    return mot_important


chirac1 = 'Nomination_Chirac1.txt'
chirac2 = 'Nomination_Chirac2.txt'
giscard = 'Nomination_Giscard dEstaing.txt'
hollande = 'Nomination_Hollande.txt'
macron = 'Nomination_Macron.txt'
mitterand1 = 'Nomination_Mitterrand1.txt'
mitterand2 = 'Nomination_Mitterrand2.txt'
sarkozy = 'Nomination_Sarkozy.txt'



#TEST :
# print(mot_dit("cleaned"))
# print(nation("cleaned"))
#print(mot_chirac())
# print(convertir_minuscule(chirac1))
# print(supprime_ponctuation(chirac1))
# print(ajout_prenom("cleaned"))
#print(TF_IDF("cleaned"))
#print(mot_non_important("cleaned"))
#print(plusgrand_TF_IDF("cleaned"))
#print(IDF("cleaned"))

