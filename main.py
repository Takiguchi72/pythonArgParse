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
parser.add_argument("--format", choices=['m3u','xspf','pls'], help = "Donne le format de sortie de la playliste (m3u | xspf | pls)")
# ToDo -> gèrer les paramètres et sous paramètres avec les <Arguments parents> Subparsers -> paramètre "nargs"
    # Gestion Titre
''' Paramètre permettant de renseigner le pourcentage d'un titre dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--titre", help = "Indique qu'on spécifie le pourcentage d'un titre dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")
''' Sous paramètre indiquant le titre désiré [chaine] '''
parser.add_argument("--strTitre", help = "Chaine correspondante au titre désiré")
''' Sous paramètre indiquant le pourcentage du titre désiré '''
parser.add_argument("--intTitre", type=int, help = "Entier naturel correspondant au pourcentage du titre désiré")
    # Gestion du genre
''' Paramètre permettant de renseigner le pourcentage d'un genre dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--genre", help = "Indique qu'on spécifie le pourcentage d'un genre dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")
''' Sous paramètre indiquant le genre désiré [chaine] '''
parser.add_argument("--strGenre", help = "Chaine correspondante au genre désiré")
''' Sous paramètre indiquant le pourcentage du genre désiré '''
parser.add_argument("--intGenre", type=int, help = "Entier naturel correspondant au pourcentage du genre désiré")
    # Gestion du sous-genre
''' Paramètre permettant de renseigner le pourcentage d'un sous-genre dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--sousgenre", help = "Indique qu'on spécifie le pourcentage d'un sous-genre dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")
''' Sous paramètre indiquant le sous genre désiré [chaine] '''
parser.add_argument("--strSousgenre", help = "Chaine correspondante au sous-genre désiré")
''' Sous paramètre indiquant le pourcentage du sous genre désiré '''
parser.add_argument("--intSousgenre", type=int, help = "Entier naturel correspondant au pourcentage du sous-genre désiré")
    # Gestion de l'artiste
''' Paramètre permettant de renseigner le pourcentage d'un artiste dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--artiste", help = "Indique qu'on spécifie le pourcentage d'un artiste dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")
''' Sous paramètre indiquant l'ariste désiré [chaine] '''
parser.add_argument("--strArtiste", help = "Chaine correspondante à l'artiste désiré")
''' Sous paramètre indiquant le pourcentage de l'artiste désiré '''
parser.add_argument("--intArtiste", type=int, help = "Entier naturel correspondant au pourcentage de l'artiste désiré")
    # Gestion de l'album
''' Paramètre permettant de renseigner le pourcentage d'un album dans la playliste [entier naturel] (Ex: "60" -> 60%) '''
parser.add_argument("--album", help = "Indique qu'on spécifie le pourcentage d'un album dans la playliste. [entier naturel] (Ex: 30 -> 30%%)")
''' Sous paramètre indiquant l'album désiré [chaine] '''
parser.add_argument("--strAlbum", help = "Chaine correspondante à l'album désiré")
''' Sous paramètre indiquant le pourcentage de l'album désiré '''
parser.add_argument("--intAlbum", type=int, help = "Entier naturel correspondant au pourcentage de l'album désiré")

args = parser.parse_args()

print("youpi")

