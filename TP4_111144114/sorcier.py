from personnage import Personnage

class Sorcier(Personnage):
    """
    Classe représentant un Sorcier. Hérite de Personnage.
    Attributes:
        nb_charmes_defaut (int): Le nombre de charmes par défaut
        nb_charmes_max (int): Le nombre de charmes maximum
        nb_charmes (int): Le nombre de charmes courant
    """

    #Attributs
    nbr_charmes_defaut = 20
    nbr_charmes_max = 20
    nbr_charmes = 0


    def __init__(self, nom, energie_depart, energie, nbr_charmes):
        """
        Le constructeur du Sorcier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et
        le nombre de charmes. NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom: Le nom du sorcier
            energie_depart:  L'énergie de départ du sorcier
            energie: L'énergie courante du sorcier
            nbr_charmes:  Le nombre de charmes du sorcier
        """
        Personnage.__init__(self, nom, energie_depart)
        self.energie_courante = energie
        self.nbr_charmes = nbr_charmes


    def to_string(self):
        """
        Retourne une chaîne du genre "Le sorcier, nom de Personnage, a une énergie de, valeur de l’énergie et,
        valeur du nombre de charmes, charmes."
        Returns (str): La chaîne représentant le Sorcier.
        """
        return 'Le sorcier {} a une énergie de {} et {} charmes.'.format(self.nom, self.energie_courante, self.nbr_charmes)


    @classmethod
    def valider_nbr_charmes(self, nb_charmes):
        """
        Valide que le nombre de charmes est positif (0 inclus) et ne doit pas dépasser nbr_charmes_max. 
        Args:
            nb_charmes (int): Le nombre de charmes à valider 

        Returns (bool): True si le nombre de charmes est valide, false sinon.
        """
        if 0 <= nb_charmes <= self.nbr_charmes_max:
            return True
        else :
            return False


    def crier(self):
        """
        Retourne le cri du sorcier: "Je vais tous vous anéantir!"
        Returns: Le cri du sorcier
        """
        return 'Je vais tous vous anéantir!'


    def attaquer(self, force_attaque):
        """
        Lorsqu’un sorcier se fait attaquer son énergie est diminuée de la force de l’attaque. Si la force de l’attaque est
        plus grande que son énergie, l’énergie du sorcier devient 0 (il meurt). 
        Args:
            force_attaque (int): La force de l'attaque 
        """
        if force_attaque > self.energie_courante:
            self.energie_courante = 0
        else :
            self.energie_courante -= force_attaque


    def get_nbr_charmes(self):
        """
        Retourne le nombre de charmes du sorcier.
        Returns (int): Le nombre de charmes du sorcier.
        """
        return self.nbr_charmes


    def set_nbr_charmes(self, nb_charmes):
        """
        Assigne le nombre de charmes du sorcier. Le nombre de charmes doit être valide.
        Args:
            nb_charmes (int): Le nombre de charmes  

        Returns (bool): True si le nombre de charmes est valide et a été modifié, False sinon.
        """
        if self.valider_nbr_charmes(nb_charmes):
            self.nb_charmes = nb_charmes
            return True
        else :
            return False


######## TEST UNITAIRES  ##############

if __name__ == '__main__':

    #test de Sorcier
    test = Sorcier ('milla',20,30,20)
    #test de la méthode valider_nbr_charmes
    assert test.valider_nbr_charmes(15) == True
    assert test.valider_nbr_charmes(0) == True
    assert test.valider_nbr_charmes(30) == False
    assert test.valider_nbr_charmes(-1) == False
    #test de la méthode crier
    assert test.crier() == 'Je vais tous vous anéantir!'
    #test de la méthode to_string
    assert test.to_string() == 'Le sorcier milla a une énergie de 30 et 20 charmes.'
    #test de la méthode get_nbr_charmes
    assert test.get_nbr_charmes () == 20
    #test de la méthode set_nbr_charmes
    assert test.set_nbr_charmes(20) == True


