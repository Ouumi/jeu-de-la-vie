from grille_cellule_regles import Grille, Cellule, jeu_de_la_vie


def test_voisines():
    grille = Grille(25)
    grille.generer()
    cellule = Cellule(5,5,grille)
    liste = [(4,4),(4,5),(4,6),(5,4),(5,6),(6,4),(6,5),(6,6)]
    assert(cellule.donner_voisines(grille) == liste)


def test_block():
    # Block
    # 0 0 0 0
    # 0 1 1 0
    # 0 1 1 0
    # 0 0 0 0
    grille = Grille(4)
    grille.generer()
    vivantes = [(1, 1), (1, 2), (2, 1), (2, 2)]
    grille.modifier(vivantes)
    nouvelles_vivantes = jeu_de_la_vie(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == sorted(vivantes))

def test_blinker():
    # Blinker
    # 0 0 0 0 0
    # 0 0 0 0 0
    # 0 1 1 1 0
    # 0 0 0 0 0
    # 0 0 0 0 0
    # Puis :
    # 0 0 0 0 0
    # 0 0 1 0 0
    # 0 0 1 0 0
    # 0 0 1 0 0
    # 0 0 0 0 0    
    grille = Grille(5)
    grille.generer()
    vivantes = [(2, 1), (2 , 2), (2, 3)]
    grille.modifier(vivantes)
    nouvelles_vivantes = jeu_de_la_vie(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == [(1, 2), (2, 2), (3, 2)])








    
