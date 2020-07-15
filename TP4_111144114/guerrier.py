from personnage import Personnage

class Guerrier(Personnage):

    """
    Classe représentant un Guerrier. Hérite de Personnage.
    Attributes:
        force_defaut (int): La valeur par défaut de la force
        force_max (int): La valeur maximum de la force
        perte_force_defaut (int): La perte de force lors d'une attaque
        gain_force_defaut (int): Le gain de force lors d'une resitution d'énergie
        force (int): La force courante du guerrier
    """
    #Attributs
    force_defaut = 20
    force_max = 80
    perte_force_defaut = 2
    gain_force_defaut = 10
    force = 0


    def __init__(self, nom, energie_depart, energie, force):
        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie (int): L'énergie courante du guerrier 
            force (int): La force du guerrier 
        """
        Personnage.__init__(self,nom, energie_depart)
        self.energie_courante = energie
        self.force = force


    def to_string(self):
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de 
        l’énergie et une force de valeur de la force."
 
        Returns (str): La chaîne représentant le guerrier. 
        """
        return 'Le guerrier, {} a une énergie de {} et une force de {}.'.format(self.nom, self.energie_courante,self.force)


    @classmethod
    def valider_force(self, force):
        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider 

        Returns (bool): True si la force est valide, False sinon
        """
        if 0 <= force <= self.force_max:
            return True
        else:
            return False


    def crier(self):
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """
        return 'Vous allez goûter à la puissance de mon épée!'


    def attaquer(self, force_attaque):
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """
        if force_attaque > self.energie_courante:
            self.energie_courante = 0
            self.force = 0
        else :
            self.energie_courante -= force_attaque
            self.force -= self.perte_force_defaut


    def reset_energie(self):
        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """
        super(Guerrier, self).reset_energie()
        self.force += self.gain_force_defaut
        if self.force > 80:
            self.force = 80


    def get_force(self):
        return self.force


    def set_force(self, force):
        if self.valider_force(force):
            self.force = force
            return True
        else:
            return False


#########   TESTS   UNITAIRES    ##########

if __name__ == '__main__' :

    #test guerrier
    test = Guerrier ('warrior', 20, 25, 70)
    #test de la méthode crier
    assert test.crier() == 'Vous allez goûter à la puissance de mon épée!'
    #test de la méthode valider_force
    assert test.valider_force(60) == True
    assert test.valider_force(90) == False
    assert test.valider_force(-1) == False
    #test de la méthode get_force
    assert test.get_force() == 70
    #test de la méthode set_force
    assert test.set_force(70) == True
    #test de la méthode to_string
    assert test.to_string() == 'Le guerrier, warrior a une énergie de 25 et une force de 70.'


