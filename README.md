# pychatbot-gun-jalaguier-f
```bash
  __  __             ______   _                _        _____   _               _       ____            _   
 |  \/  |           |  ____| (_)              | |      / ____| | |             | |     |  _ \          | |  
 | \  / |  _   _    | |__     _   _ __   ___  | |_    | |      | |__     __ _  | |_    | |_) |   ___   | |_ 
 | |\/| | | | | |   |  __|   | | | '__| / __| | __|   | |      | '_ \   / _` | | __|   |  _ <   / _ \  | __|
 | |  | | | |_| |   | |      | | | |    \__ \ | |_    | |____  | | | | | (_| | | |_    | |_) | | (_) | | |_ 
 |_|  |_|  \__, |   |_|      |_| |_|    |___/  \__|    \_____| |_| |_|  \__,_|  \__|   |____/   \___/   \__|
            __/ |                                                                                           
           |___/                                                                                            
  	by Louis GUN and Frédéric Jalaguier

```
Voici la notice d'utilisation de la première vertion de notre 'My first Chat Bot' :

Vous disposez de 2 fichiers : 'fonctions.py' et 'main.py' 


________________________________fonction.py________________________________

- 'fonction.py' contiaint les fonctions utiles au programme. Il est compsé de 4 parties :

	- La première est dédiée au traitement de texte. Voici les fonctions :

		- convertir_minuscule() : qui prend en argument le nom de l'un des 8 discours (chirac1, chirac2, giscard, hollande, macron, mitterand1, mitterand2, sarkizy). Elle convertie en minuscule le texte et crée un copie dans le dossier 'speeches'
		- supprime_ponctuation() : argument et le même / supprime toutes les ponctuations du fichier et elle remplace le fichier

	- La seconde est dédiée à la récupération des noms/prénoms des présidents. voici les fonctions :
		- list_of_files() : retourne la liste des noms des documents
		- recup_nom() : retourne la liste des noms des présidents à partir de la liste des documents
		- ajout_prenom() : retourne un dictionnaire sous la forme : clé = Nom Valeur = Prénom

	- La troisième partie est consacrée au TF-IDF :
		- TF() : Calcule la frequence d'un mot dans un texte 
		- IDF() : Associe un coefficien à chacun des mots présents dans les 8 textes
		- TF_IDF() : multiplie TF et IDF, chaque mot à donc un score qui permet de connaitre l'importance de celui ci dans un texte. La fonction renvoie une matrice.
		Les trois fonctions prennent en argument un répertoire de fichier contenant une chaine de caractère. Dans notre cas, c'est les 8 textes contenus dans 'speeches'

	- La quatrième partie contient toutes les fonctions que l'utilisateur peut demander lors de l'execution du fichier 'main.py'
		- mot_non_important() : Retourne la liste des mots les moins importants dans le corpus de documents
		- plusgrand_TF_IDF() : Retourne le(s) mot(s) ayant le score TD-IDF le plus élevé
		- mot_chirac() : Retourne le(s) mot(s) le(s) plus répété(s) par le président Chirac
		- nation() : Retourne le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
		- climat() [[[NON FONCTIONELLE]]]  : Retourne le premier président à parler du climat et/ou de l’écologie
		- mot_dit() [[[NON FONCTIONELLE]]]  : Hormis les mots dits « non importants », retourne le(s) mot(s) que tous les présidents ont évoqués.



________________________________main.py________________________________

- 'main.py' contient le programme principal à executer.

Lors du lancement, tout est expliqué dans la console 



______________________________________________________________________________________________________________________________________________

Rapport de Buggs : 

Pous la fonction climat() Il n'existe pas de mot qui ont tout leurs TF_IDF = 0. Nous sommes certain que l'erreur provient du log() dans la fonction TF_IDF. Nous devons donc trouver une autre solution pour trouver les mot que tous les présidents ont évoqués.


______________________________________________________________________________________________________________________________________________

Il ne reste plus qu'a lancer le prgramme main.py et laisser la magie opérer...