#!/bin/env python3

import random

actions = ['tu longes', 'tu contournes', 'tu passes', 'tu descends', 'tu montes']
directions = [('à côté', 0), ('derrière', 1), ('devant', 1), ('à droite', 0), ('à gauche', 0)]
determinant = [('de la', 'du'), ('la', 'le')]
places = [('guet', 1), ('combe', 0), ('grotte', 0), ('col', 1)]
noms = ['du pendu', 'de la glotte', 'de la vulve Saint Pierre', 'du brossard', 'de la verge', 'Sainte Marie', 'de la grosse bosse']

liaisons = ['Bon, déjà,', 'Ensuite', 'Après', 'Puis', 'Enfin']

bullshit = ''

for i in range(len(liaisons)):
    a = random.randint(0, len(actions) - 1)
    d = random.randint(0, len(directions) - 1)
    p = random.randint(0, len(places) - 1)
    n = random.randint(0, len(noms) - 1)
    
    direct, det = directions[d]
    place, genre = places[p] 
    
    dir_place = ' '.join([direct, determinant[det][genre], place])
    
    bullshit += ' '.join([liaisons[i], actions[a], dir_place, noms[n]]) + '. '
    noms = noms[0:n] + noms[n+1:len(noms)+1]
    
print(bullshit)
