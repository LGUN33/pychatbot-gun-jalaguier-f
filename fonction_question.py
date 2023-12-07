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



print(token_question("salut C'est moi, fred."))