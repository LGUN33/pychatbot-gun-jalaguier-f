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
    ch=ch.split()
    for elt in ch:
        if elt not in TF:
            TF[elt]=1
        else:
            TF[elt]+=1
    return TF


def IDF(repertoire):
    directory = "./"+repertoire
    files_names = list_of_files(directory, "txt")
    taille= len(files_names)
    list_mot=[]
    for elt in files_names:
        chemin = os.path.join(directory, elt)
        with open(chemin, "r") as doc:
            contenu = doc.read()
            contenu=contenu.split()
            list_mot+=contenu
    list_mot=set(list_mot)
    IDF={}
    for mot in list_mot:
        occurence=0
        for elt in files_names:
            chemin = os.path.join(directory, elt)
            with open(chemin, "r") as doc:
                contenu = doc.read()
                if mot in contenu:
                    occurence+=1
        score=math.log10((taille/occurence)+1)
        IDF[mot]=score
    return IDF


def TF_IDF(repertoire):
    matrice = []
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
                L.append(valeur_tf * valeur_idf)
        matrice.append(L)
    return matrice

def mot_non_important(repertoire):
    matrice=TF_IDF(repertoire)
    mot=[]
    n=0
    for i in range(len(matrice)):
        j=0
        while j<=len(matrice[i]) and n==0:
            j+=1
            if matrice[i][j]!=0:
                n=1
        if n!=1:
            mot.append(matrice[i])
    print(mot)
    return mot




#ajout_prenom(files_names)


chirac1 = 'Nomination_Chirac1.txt'
chirac2 = 'Nomination_Chirac2.txt'
giscard = 'Nomination_giscard dEstaing.txt'
hollande = 'Nomination_Hollande.txt'
macron = 'Nomination_Macron.txt'
mitterand1 = 'Nomination_Mitterrand1.txt'
mitterand2 = 'Nomination_Mitterrand2.txt'
sarkozy = 'Nomination_Sarkozy.txt'

#convertir_minuscule(chirac1)
#supprime_ponctuation(chirac1)


#TF_IDF("cleaned")
mot_non_important("cleaned")