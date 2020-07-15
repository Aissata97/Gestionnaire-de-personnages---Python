class Personnage:
    """
    Attributes:
        energie_depart_defaut (int): L'énergie de départ par défaut
        energie_depart_min (int): L'énergie de départ minimum
        energie_max (int): L'énergie maximum en tout temps
        longueur_nom_min (int) : La longueur minimale du nom
        longueur_nom_max (int) : La longueur maximale du nom
        nom (str) : Le nom
        energie_depart (int): L'énergie de départ
        energie_courante (int): L'énergie courante

    """

    #Attibuts
    energie_depart_defaut = 20
    energie_depart_min = 1
    energie_max = 100
    longueur_nom_min = 3
    longueur_nom_max = 30
    nom = ''
    energie_depart = 0
    energie_courante = 0


    def __init__(self, nom, energie_depart):
        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """
        self.nom = nom
        self.energie_depart = energie_depart
        self.energie_courante = energie_depart


    def crier(self):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """
        pass


    def attaquer(self, force_attaque):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """
        pass


    def est_mort(self):
        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """
        if self.energie_courante == 0 :
            return True
        else:
            return False


    @classmethod
    def valider_nom(self, nom):
        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """

        if self.longueur_nom_min <= len(nom) <= self.longueur_nom_max:
            return True
        else:
            return False


    @classmethod
    def valider_energie_courante(self, energie_courante):
        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.

        """
        if 0 <= energie_courante <= self.energie_max :
            return True
        else :
            return False


    @classmethod
    def valider_energie_depart(self, energie_depart):
        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """

        if self.energie_depart_min <= energie_depart <= self.energie_max :
            return True
        else :
            return False


    def reset_energie(self):
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """
        self.energie_courante = self.energie_depart


    def get_energie_courante(self):
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """
        return self.energie_courante


    def set_energie_courante(self, energie_courante):
        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_energie_courante(energie_courante):
            self.energie_courante = energie_courante
            return True
        else:
            return False


    def get_nom(self):
        """
        Retourne le nom.
        Returns (str): Le nom.
        """
        return self.nom


    def set_nom(self,nom):
        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_nom(nom):
            self.nom = nom
            return True
        else:
            return False


    def get_energie_depart(self):
        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """
        return self.energie_depart


    def set_energie_depart(self, energie_depart):
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_energie_depart(energie_depart):
            self.energie_depart = energie_depart
            return True
        else:
            return False


    def to_string (self):

        """
        Retourne une chaine du genre : nom du Personnage, a une énergie de valeur de l’énergie.

        """
        return '{} a une énergie de {}'.format(self.nom, self.energie_courante)


##########     TESTS UNITAIRES        ##############

if __name__ == '__main__':

    test = Personnage('angel', 20)
    # test de la méthode valider_nom
    assert test.valider_nom("angel") == True
    assert test.valider_nom('sa') == False
    assert test.valider_nom("abcdefghijklmnopqrstuvwxyzabcdefg") == False
    # test de la méthode valider_energie_courante
    assert test.valider_energie_courante(50) == True
    assert test.valider_energie_courante(150) == False
    assert test.valider_energie_courante(-1) == False
    # test de la méthode valider_energie_depart
    assert test.valider_energie_depart(1) == True
    assert test.valider_energie_depart (30) == True
    assert test.valider_energie_depart(110) == False
    assert test.valider_energie_depart(-1) == False
    #test de la méthode set_energie_courante
    assert test.set_energie_courante(20) == True
    #test de la méthode set_energie_depart
    assert test.set_energie_depart(20) == True
    #test de la méthode get_energie_depart
    assert test.get_energie_depart() == 20
    assert not test.get_energie_depart() == 25
    #test de la méthode get_energie_courante
    assert test.get_energie_courante() == 20
    assert not test.get_energie_courante() == 21
    #test de la méthode set_nom
    assert test.set_nom('angel') == True
    #test de la méthode get_nom
    assert test.get_nom() == "angel"
    assert not test.get_nom() == 'daviee'
    #test de la méthode to_string
    assert test.to_string() == 'angel a une énergie de 20'
















