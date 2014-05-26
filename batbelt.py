#!/usr/bin/python
# -*-coding:Utf-8 -*

import re
import os
import sqlite3
import unidecode
import datetime
from dateutil.parser import parse
from dateutil import relativedelta

"""Module pour fct de secours ou qui n'ont rien à voir avec les thèmes des autres
modules"""


def sizeof(nbr, unit="o", rounded=1):

    """On récupère la taille en octets, et on la formate en Mo
    ou en Go si plus grand que 1000 Mo. Si on passe l'argument 'b'
    en paramètre, on calcule en ibytes"""
    #http://www.fevrierdorian.com/blog/post/2011/06/26/Taille-d-un-fichier-humainement-comprehensible-en-Python

    if unit == "o":
        for x in ['octets','ko','Mo','Go','To']:
            if nbr < 1000.0:
                return "{0} {1}".format(round(nbr, rounded), x)
            nbr /= 1000.0
    elif unit == "b":
        for x in ['bytes','KiB','MiB','GiB','TiB']:
            if nbr < 1024.0:
                return "{0} {1}".format(round(nbr, rounded), x)
            nbr /= 1024.0


def simpleChar(chaine):

    """Fct retournant la version minuscule et sans accent de la chaine
    entrante"""
    #http://www.siteduzero.com/forum-83-810635-p1-sqlite-recherche-avec-like-insensible-a-la-casse.html#r7767300

    # Nouvelle fct de renommage, qui prend aussi les chiffres
    #http://stackoverflow.com/questions/5574042/string-slugification-in-python
    chaine = unidecode.unidecode(chaine).lower()
    return re.sub(r'\W+', ' ', chaine)


def recent(date, days=1):

    """Fct qui renvoie True si la date passée
    en paramètre est récente. 1 jour est le
    paramètre par défaut pour récent"""

    now = datetime.datetime.now()

    date = parse(date)

    if now - relativedelta.relativedelta(days =+ days) < date:
        return True
    else:
        return False


def strByteToOctet(size):

    """Fct pour convertir une chaîne du type '300 MiB' en bytes,
    et pour retourner une chaîne en Mo"""

    nbr, unit = size.split(" ")
    nbr = float(nbr)

    if unit == "MiB":
        nbr *= 2**20
    elif unit == "GiB":
        nbr *= 2**30

    nbr_octets = nbr

    for x in ['o','Ko','Mo','Go','To']:
        if nbr < 1000.0:
            return "{0} {1}".format(round(nbr, 1), x), int(round(nbr_octets, 0))
        nbr /= 1000.0

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L



if __name__ == "__main__":
    pass
