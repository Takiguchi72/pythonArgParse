#!/usr/bin/python3
# -*- coding: utf-8 -*-
import motDePasse
import sqlalchemy
from sqlalchemy.sql.schema import Column, PrimaryKeyConstraint

# Déclaration et connexion au moteur sql utilisé
engine = sqlalchemy.create_engine('posgresql://f.thierry:' + motDePasse.getMdp() + '@172.16.99.2:5432/radio_libre')
# Déclaration et initialisation des metadata
metadata = sqlalchemy.MetaData()
# Création de la structure de la bdd
morceaux = sqlalchemy.Table('morceaux', metadata, Column('titre', str, primary_key = True),Column('album', str), Column('artiste', str), Column('genre', str), Column('sousgenre', str), Column('duree',int(7)), Column('format',str), Column('polyphonie',int(9)),Column('chemin',str))
# Création de la base dans le model PYTHON2_EXCEPTIONS
metadata.create_all(engine)