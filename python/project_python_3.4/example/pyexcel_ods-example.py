#
# Created 30/06/2020
# generateAnnounces.py for LeBonCoin
# Read an ODS table and create files for LBC announces
# Quick and dirty example for pyexcel_ods lib
#

import pyexcel_ods
import os
import json

BASE_ANNOUNCE='/tmp/announce{}.txt'
DEFAULT="/media/bigDisk/01-Document/11-Le bon Coin/figsAVendre.ods"

data = pyexcel_ods.get_data(DEFAULT)
print((json.dumps(data, indent=4, sort_keys=True)))

for jsonLine in data['Feuille1']:
    # Data format: ['ID', 'Jeu', 'Taille', 'Armée', 'Description générale', 'Etat', 'Bonus', 'Autres', ' Prix']
    id = jsonLine[0]
    bonus = jsonLine[6]
    if bonus:
        bonus = "Donne (a jeter sinon) avec le lot: \n{}".format(bonus)

    title = "{}-Figurines GW: {}-{}-{}\n\n".format(id, jsonLine[3], jsonLine[2], jsonLine[1])
    text = "Figurines de la marque Citadel (Games Workshop), lot {}:\n{}\n".format(id, jsonLine[4]) + \
           "Etat des figurines:\n{}\n".format(jsonLine[5]) + \
           bonus + \
           jsonLine[7] + \
           "\nPrix: {}\n".format(jsonLine[8]) + \
           "Je vends 14 lots de figurines, n'hésitez pas à aller voir les autres annonces\n"

    filePath = BASE_ANNOUNCE.format(id)
    if os.path.exists(filePath):
        os.remove(filePath)
    newAnnounce = open(filePath, mode="a+", encoding="utf-8")
    newAnnounce.writelines(title)
    newAnnounce.writelines(text)

exit(0)

