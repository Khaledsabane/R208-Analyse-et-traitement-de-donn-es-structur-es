import re
# La fonction re.match () permet de chercher à partir du début de la chaîne de caractères et
# la fonction re.search () permet de chercher dans la chaîne de caractères.


def match_prenom_compose(nom)-> bool :
    result = re.search("^[a-z]+-[a-z]+$", nom)
    #print(result)
    if result :
        return True
    else:
        return False

print(match_prenom_compose("jean-claud"))

def match_domaine(domaine)->bool :
    result = re.search("^[a-z]+\.[a-z]{2,3}$", domaine )
    if result :
        return True
    else:
        return False

print(match_domaine("google.fr"))


def number_match_bash(file):
    desc = open(file ,"r")
    contenu = desc.read()
    desc.close()
    result = re.findall("/bin/bash", contenu)
    return len(result)

def user_match_bash(file):
    result =[]
    desc = open (file ,"r")
    contenu = desc.read()
    desc.close()
    result = re.findall(".*/bin/bash", contenu)
    print(result)
    for idx in result:
        user = (idx.split(":")[0])
        print(user)

def user_with_2o(file):
    desc = open(file ,"r")
    contenu = desc.readlines()
    desc.close()
    for idx in contenu :
        user = idx.split(":")[0]
        result = re.search("[o].*[o]",user)
        if result :
            print(user)



def verif_mot_passe(mot_de_passe):
    correct = False
    maj = re.search("[A-Z].*[A-Z]",mot_de_passe)
    if maj :
        chiffre = re.search("[0-9].*[0-9].*[0-9]",mot_de_passe)
    if chiffre :
        special = re.search("[\.\?\*\+\-]",mot_de_passe)
    if special :
        correct = True
    return correct



f="utilisateur.txt"
print(number_match_bash(f))
user_match_bash(f)
user_with_2o(f)

print(verif_mot_passe("sdsdfAs323Asdf+?"))