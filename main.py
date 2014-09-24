import argparse
parser = argparse.ArgumentParser()
# Gestion des arguments positionnels
''' Le 1er paramètre correspond au nom que l'on veut attribuer à la playliste [chaine] (Ex: "maPlayliste") '''
parser.add_argument("nom_playlist", help = "Le nom du fichier contenant la playlist.")
# ToDo -> voir pour associer une fonction de vérification à la déclaration d'un argument -> paramètre "action" cf doc
''' Le 2ème paramètre correspond à la durée désirée pour la playliste [entier naturel] '''
parser.add_argument("temps_playlist", type=int,  help = "Spécifie la durée de la playlist, en minutes. [entier naturel] (Ex : 60)")

# Gestion des arguments optionnels
''' Paramètre permettant de renseigner le format de playliste désiré selon la liste {m3u,xspf,pls} '''
parser.add_argument("--format", nargs = 1, choices=['m3u','xspf','pls'], help = "Donne le format de sortie de la playliste (m3u | xspf | pls)")
# ToDo -> gèrer les paramètres et sous paramètres avec les <Arguments parents> Subparsers -> paramètre "nargs"

    # Gestion Titre
''' Paramètre permettant de renseigner le pourcentage d'un titre dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--titre", nargs = 2, help = "Indique qu'on spécifie le pourcentage d'un titre dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")

    # Gestion du genre
''' Paramètre permettant de renseigner le pourcentage d'un genre dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--genre", nargs = 2, help = "Indique qu'on spécifie le pourcentage d'un genre dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")


    # Gestion du sous-genre
''' Paramètre permettant de renseigner le pourcentage d'un sous-genre dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--sousgenre", nargs = 2, help = "Indique qu'on spécifie le pourcentage d'un sous-genre dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")


    # Gestion de l'artiste
''' Paramètre permettant de renseigner le pourcentage d'un artiste dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--artiste", nargs = 2, help = "Indique qu'on spécifie le pourcentage d'un artiste dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")

    # Gestion de l'album
''' Paramètre permettant de renseigner le pourcentage d'un album dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--album", nargs = 2, help = "Indique qu'on spécifie le pourcentage d'un album dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")

args = parser.parse_args()


''' Fonction de vérification des sous arguments '''
def checkSousArgs(arg):
    try:
        nb = int(arg[1])
        if (checkIntNatural(nb) == False):
            print ("La quantité doit être positive ! (" + arg[1] + ")")
        return 0
    except ValueError:
        print ("Impossible de convertir \"" + arg[1] + "\" en nombre entier !")
   
''' Vérifie qu'un nombre est un entier naturel '''     
def checkIntNatural(nb):
    if nb > 0:
        return True
    else:
        return False


checkSousArgs(args.genre)

