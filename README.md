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
Voici la notice d'utilisation de la première version de notre 'My first Chat Bot' :

Vous disposez de 3 fichiers : 'fonctions_texte.py', 'fonction_question.py' et 'main.py' 


________________________________fonction_texte.py________________________________

- 'fonction_texte.py' contiaint les fonctions utiles au programme au niveau du traitement de texte. Il est compsé de 4 parties :

	- La première est dédiée au traitement de texte. Voici les fonctions :

		- convertir_minuscule() : qui prend en argument le nom de l'un des 8 discours (chirac1, chirac2, giscard, hollande, macron, mitterand1, mitterand2, sarkizy). Elle convertit en minuscule le texte et crée une copie dans le dossier 'speeches'
		- supprime_ponctuation() : argument et le même / supprime toutes les ponctuations du fichier et elle remplace le fichier

	- La seconde est dédiée à la récupération des noms/prénoms des présidents. voici les fonctions :
		- list_of_files() : retourne la liste des noms des documents
		- recup_nom() : retourne la liste des noms des présidents à partir de la liste des documents
		- ajout_prenom() : retourne un dictionnaire sous la forme : clé = Nom Valeur = Prénom

	- La troisième partie est consacrée au TF-IDF :
		- TF() : Calcule la fréquence d'un mot dans un texte 
		- IDF() : Associe un coefficient à chacun des mots présents dans les 8 textes
		- TF_IDF() : multiplie TF et IDF, chaque mot à donc un score qui permet de connaitre l'importance de celui-ci dans un texte. La fonction renvoie une matrice.
		Les trois fonctions prennent en argument un répertoire de fichier contenant une chaine de caractère. Dans notre cas, c'est les 8 textes contenus dans 'speeches'

	- La quatrième partie contient toutes les fonctions que l'utilisateur peut demander lors de l'execution du fichier 'main.py'
		- mot_non_important() : Retourne la liste des mots les moins importants dans le corpus de documents
		- plusgrand_TF_IDF() : Retourne le(s) mot(s) ayant le score TD-IDF le plus élevé
		- mot_chirac() : Retourne le(s) mot(s) le(s) plus répété(s) par le président Chirac
		- nation() : Retourne le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
		- climat() : Retourne le premier président à parler du climat et/ou de l’écologie
		- mot_dit() : Hormis les mots dits « non importants », retourne le(s) mot(s) que tous les présidents ont évoqués.



________________________________main.py________________________________

- 'main.py' contient le programme principal à exécuter.

Lors du lancement, tout est expliqué dans la console 



________________________________fonction_question.py________________________________

Il contient toutes les fonctions utiles au traitement de la question de l'utilisateur. Au niveau du main, il n'est utilisé que quand l'utilisateur presse la touche '7'


Il contient des fonctions qui :
- Traitent la question (ponctuation, majuscules) 
- Calculent un TF-IDF à la question
- Comparent les mots de la question à ceux des textes.
Enfin, il renvoie le texte le plus pertinent pour l'utilisateur.


______________________________________________________________________________________________________________________________________________

Rapport de bugs : 

La fonction TF_IDF_question du fichier "fonction_question.py" ne fonctionne pas, nous n'arrivons pas à trouver de solution par manque de temps.
Nous avons effectués des tests sans l'utilisation de cette fonction et cela fonctionne à peu près bien.

L'option '7' de l'utilisateur n'est donc pas encore disponible, mais elle ne saurait tarder

______________________________________________________________________________________________________________________________________________

Il ne reste plus qu'à lancer le programme main.py et laisser la magie opérer...