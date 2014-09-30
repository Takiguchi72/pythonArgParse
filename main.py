#!/usr/bin/python3
''' Fonction de vérification des sous arguments '''
def checkSousArgs(arg, nomArg):
    try:
        # Conversion en entier
        nb = int(arg[1])
        # Si nb n'est pas un entier naturel et qu'il est supérieur ou égal à 100, on lève une exception !
        if (checkIntNatural(nb) == False):
            raise Exception('EntierNaturel',' --' + nomArg + ', la valeur "' + arg[1] + '" doit être positive !')
        if (checkIntInfCent(nb) == False):
            raise Exception('SuperieurACent', ' --' + nomArg + ', la valeur "' + arg[1] + '" doit être inférieure à "100" !')
        # Si il n'y a pas d'erreur, on retourne la valeur 0
        else:
            return 0
    except Exception as er:
        if er.args[0] == 'EntierNaturel' and er.args[0] == 'SuperieurACent':
            logging.error(er.args[1])
        else:
            logging.error(' --' + nomArg + ', impossible de convertir "' + arg[1] + '" en nombre entier !')

''' Vérifie qu'un nombre est un entier naturel '''
def checkIntNatural(nb):
    if nb > 0:
        return True
    else:
        return False
    
''' Vérifie qu'un nombre est inférieur à 100 '''
def checkIntInfCent(nb):
    if nb < 100:
        return True
    else:
        return False

''' Traitement du programme principal '''
import argparse
import logging

parser = argparse.ArgumentParser()          # Création d'un objet de classe ArgumentParser
logging.basicConfig(filename='errors.log', level=logging.DEBUG)   # Les erreurs seront redirigées dans le fichier de log nommé 'errors.log'

# Gestion des arguments positionnels
''' Le 1er paramètre correspond au nom que l'on veut attribuer à la playliste [chaine] (Ex: "maPlayliste") '''
parser.add_argument("nom_playlist", help = "Le nom du fichier contenant la playlist.")
''' Le 2ème paramètre correspond à la durée désirée pour la playliste [entier naturel] '''
parser.add_argument("temps_playlist", type=int,  help = "Spécifie la durée de la playlist, en minutes. [entier naturel] (Ex : 60)")

# Gestion des arguments optionnels
    # Gestion Format
''' Paramètre permettant de renseigner le format de playliste désiré selon la liste {m3u,xspf,pls} '''
parser.add_argument("--format", nargs = 1, choices=['m3u','xspf','pls'], help = "Donne le format de sortie de la playliste (m3u | xspf | pls)")
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

#''' Boucle pour tester l'ensemble des paramètres optionnels, et réalise le test uniquement si l'argument est renseigné '''
# for ARG in ['titre','genre','sousgenre','artiste','album']:
#     if getattr(args, ARG) is not None:
#         checkSousArgs(getattr(args, ARG), ARG)

# Gestion de l'argument genre et ses sous-arguments
# Pour chaque argument, si ils sont renseignées, on les affiche dans le fichier de logs
for ARG in ['titre','genre','sousgenre','artiste','album']:
    if getattr(args, ARG) is not None:
        logging.info(' Argument --' + ARG + ' :\t' + getattr(args, ARG)[0] + ' ; ' + getattr(args, ARG)[1])
# On vérifie que le 2em sous argument de genre est bien un entier naturel
if checkSousArgs(args.genre,'genre') == 0:
    print ('ok')
    
    
logging.debug(' *****************************************')
# la commande exit(0) permet de quitter le programme sans omettre d'erreur, alors que exit(1) lève une erreur