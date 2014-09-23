import argparse
parser = argparse.ArgumentParser()
# Gestion des arguments
# La durée doit être renseignée avec les arguments "temps" et "valeur_temps" 
parser.add_argument("temps")                                        # Indique qu'on renseigne la duree
parser.add_argument("tempsValeur", help = "Valeur en minutes")     # Renseigne la duree désiree

args = parser.parse_args()