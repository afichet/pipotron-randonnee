#!/bin/env python3

import random

class Rando:
    def __init__(self):
        self.actions = ['tu longes', 'tu contournes', 'tu passes', 'tu descends', 'tu montes']
        self.directions = [('à côté', 0), ('derrière', 1), ('devant', 1), ('à droite', 0), ('à gauche', 0)]
        self.determinant = [('de la', 'du'), ('la', 'le')]
        self.places = [('guet', 1), ('combe', 0), ('grotte', 0), ('col', 1), ('pré', 1), ('lac', 1), ('gorge', 0)]
        self.noms = [
            'du pendu', 
            'de la glotte', 
            'de la soupière', 
            'de la vulve Saint Pierre', 
            'du brossard', 
            'de la verge',
            'Sainte Marie', 
            'de la grosse bosse',
            'du vieux coquin',
            'de la belette',
            'qui tue',
            'de la gouttière',
            'Saint Georges',
            'des perrières',
            'du framboisier',
            'de la mouille',
            'aux fleurs',
            'de la goute',
            'de la glaire',
            'du sac'
        ]
        self.liaisons = ['Bon, déjà,', 'Ensuite', 'Après', 'Avant', 'Puis', 'Enfin']

    def get_str_adpn(self):
        a = random.randint(0, len(self.actions) - 1)
        d = random.randint(0, len(self.directions) - 1)
        p = random.randint(0, len(self.places) - 1)
        n = random.randint(0, len(self.noms) - 1)

        action = self.actions[a]
        dir_place = self.get_dir_place(d, p)
        nom = self.noms[n]

        self.noms = self.noms[0:n] + self.noms[n+1:len(self.noms)+1]

        return action, dir_place, nom

    def get_dir_place(self, idx_dir, idx_place):
        direct, det = self.directions[idx_dir]
        place, genre = self.places[idx_place]

        return ' '.join([direct, self.determinant[det][genre], place])

rando = Rando()
bullshit = ''

for i in range(len(rando.liaisons)):
    action, dir_place, nom = rando.get_str_adpn()
    bullshit += ' '.join([rando.liaisons[i], action, dir_place, nom]) + '. '
    
    r = random.randint(0, 2)
    if r > 0:
        action, dir_place, nom = rando.get_str_adpn()
        inst = ' '.join([dir_place.capitalize(), nom])
                         
        action, dir_place, nom = rando.get_str_adpn()                         
        bullshit += inst + ', ' + ' '.join([action, dir_place, nom]) + '. '
       
print(bullshit)
