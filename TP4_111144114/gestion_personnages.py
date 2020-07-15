
from tkinter.filedialog import *
from tkinter import messagebox
from util import Util
from personnage import Personnage
from sorcier import Sorcier
from guerrier import Guerrier


class GestionPersonnages:
    """
    Classe s'occupant de la gestion des personnages.
    Attributes:
        liste_personnages (list): La liste des personnages
        fichier_courant (str): Le nom du fichier courant
    """

    liste_personnages = []
    fichier_courant = ""


    def mettre_a_jour_liste(self):
        """
        Mets à jour et trie la liste des personnages par rapport à l'énergie courante.
        Returns (list str): La liste triée des chaînes de caractères des personnages
        """
        self.liste_personnages.sort(key=lambda personnage: int(personnage.energie_courante))


    def gestion_creer_sorcier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier)
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.
        Sinon, on affiche seulement que le sorcier n'a pas été ajouté.
        """
        try:
            nom,energie_depart,energie_courante,nb_charmes = self.saisir_et_creer_sorcier()
            self.ajouter_personnage(Sorcier(nom,energie_depart,energie_courante,nb_charmes))
            messagebox.showinfo("Ajout d'un Sorcier","Le nouveau sorcier a été ajouté à la liste")
            self.mettre_a_jour_liste()
        except:
            messagebox.showwarning("Erreur ajout d'un Sorcier","Le nouveau sorcier n'a pas pu etre ajouté")


    def saisir_et_creer_sorcier(self):
        """
        Retourne un objet Sorcier valide. Chaque information du sorcier demandée doit être validée.
        L'annulation d'une info entraine automatiquement l'annulation des informations suivantes.
        Si toutes les informations sont valides, un sorcier est alors instancié.

        Return (Sorcier): Le sorcier instancié si la création a réussie, None sinon.
        """
        nom = Util.saisir_string("Donnez le nom du sorcier ? (entre {} À {})".format(Sorcier.longueur_nom_min,Sorcier.longueur_nom_max))
        if not Sorcier.valider_nom(nom):
            return False
        energie_depart = Util.saisir_objet_entier("Indiquer l'énergie de départ du sorcier ? (entre {} À  {})".format(Sorcier.energie_depart_min,Sorcier.energie_max))
        if not Sorcier.valider_energie_depart(energie_depart):
            return False
        energie_courante = Util.saisir_objet_entier("Indiquer l'énergie courante du sorcier ? (entre {} À {})".format(0,Sorcier.energie_max))
        if not Sorcier.valider_energie_courante(energie_courante):
            return False
        nb_charmes = Util.saisir_objet_entier("Indiquer le nombre de charmes du sorcier ? (entre {}  À {})".format(0,Sorcier.nbr_charmes_max))
        if not Sorcier.valider_nbr_charmes(nb_charmes):
            return False
        return (nom,energie_depart,energie_courante,nb_charmes)


    def gestion_creer_guerrier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier)
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.
        Sinon, on affiche seulement que le sorcier n'a pas été ajouté.
        """
        try:
            nom,energie_depart,energie_courante,force = self.saisir_et_creer_guerrier()
            self.ajouter_personnage(Guerrier(nom,energie_depart,energie_courante,force))
            messagebox.showinfo("Ajout d'un Guerrier","Le nouveau guerrier a été ajouté à  la liste")
            self.mettre_a_jour_liste()
        except:
            messagebox.showwarning("Erreur ajout d'un Guerrier","Le nouveau guerrier n'a pas pu être ajouté")


    def saisir_et_creer_guerrier(self):
        """
        Retourne un objet Guerrier valide.  Chaque information du guerrier demandée doit être validée.
        L'annulation d'une information entraine automatiquement l'annulation des informations suivantes.
        Si toutes les infos sont valides, un guerrier est alors instancié.

        Returns (Guerrier): Le guerrier instancié si la création a réussie, None sinon.
        """
        nom = Util.saisir_string("Donnez le nom du guerrier ? (entre {} À  {})".format(Guerrier.longueur_nom_min,Guerrier.longueur_nom_max))
        if not Guerrier.valider_nom(nom):
            return False
        energie_depart = Util.saisir_objet_entier("Indiquer l'énergie de départ du guerrier ? (entre {} À  {})".format(Guerrier.energie_depart_min,Guerrier.energie_max))
        if not Guerrier.valider_energie_depart(energie_depart):
            return False
        energie_courante = Util.saisir_objet_entier("Indiquer l'énergie courante du guerrier ? (entre {} À  {})".format(0,Guerrier.energie_max))
        if not Guerrier.valider_energie_courante(energie_courante):
            return False
        force = Util.saisir_objet_entier("Indiquer la force du guerrier ? (entre {} À  {})".format(0,Guerrier.force_max))
        if not Guerrier.valider_force(force):
            return False
        return (nom,energie_depart,energie_courante,force)


    def ajouter_personnage(self, personnage):
        """
        Ajoute le Personnage à la liste.
        Args:
            personnage (Personnage): Le personnage à  ajouter.
        """
        self.liste_personnages.append(personnage)


    def gestion_attaquer(self, index):
        """
        Reçoit l'indice du personnage sélectionné ou -1 si aucun personnage n'est sélectionné.
        Si le personnage sélectionné n'est pas mort, on saisit avec validation la force de l'attaque
        (> 0 et <= energie_max).  Lorsque la force saisie est valide, on attaque le personnage sélectionné sinon on
        affiche un message adéquat.  S'il n' y a aucun personnage sélectionné ou s'il est mort,
        un message est affiché.

        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        try:
            if not self.liste_personnages[int(index[0])].est_mort():
                force_attaque = Util.saisir_objet_entier("Entrer la force de l'attaque? (entre 0 À 101)")
                if self.liste_personnages[int(index[0])].valider_energie_courante(force_attaque):
                    self.liste_personnages[int(index[0])].attaquer(force_attaque)
                    messagebox.showinfo('Attaque',"L'attaque a fonctionné")
                    self.mettre_a_jour_liste()
                else:
                    messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")
            else:
                messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")
        except:
            messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")


    def gestion_augmenter_energie(self, index):
        """
        Reçoit l'indice du personnage sélectionné ou -1 si aucun personnage n'est sélectionné.
        Si le personnage sélectionné n'est pas mort, réinitialiser son énergie. S'il n y a aucun personnage
        sélectionné ou s'il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        try:
            if not self.liste_personnages[int(index[0])].est_mort():
                self.liste_personnages[int(index[0])].reset_energie()
                messagebox.showinfo('Reset energie',"Le reset de l'énergie a fonctionné")
                self.mettre_a_jour_liste()
            else:
                messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")
        except:
            messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")


    def gestion_crier(self, index):
        """
        Reçoit l'indice du personnage sélectionné ou -1 si aucun personnage n'est sélectionné.
        Si le personnage sélectionné n'est pas mort, émettre son cri.  S'il n'y a aucun personnage sélectionné ou
        s'il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        try:
            if not self.liste_personnages[int(index[0])].est_mort():
                messagebox.showinfo('Cri du personnage',self.liste_personnages[int(index[0])].crier())
            else:
                messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")
        except:
            messagebox.showinfo('Action sur un personnage',"Il n'y a aucun personnage sélectionné ou le personnage sélectionné est mort, donc il ne peut être attaqué")


    def gestion_ouvrir(self):
        """
        Permet de gérer l'ouverture et la lecture d'un fichier de personnages
        (un fichier .txt qui contient des informations sur des personnages, un personnage par ligne).
        Si la liste n'est pas vide, on demande à  l'utilisateur s'il veut sauvegarder les données courantes et
        s'il répond oui, on fait appel à  gestion_enregistrer_sous.  Ensuite, on demande à l'utilisateur le nom du
        fichier à ouvrir.  Si le fichier choisi n'est pas null, le fichier à ouvrir devient le fichier courant
        et si la lecture du fichier n' a pas bien fonctionné (voir méthode lireFichierPersonnages dans classe Util),
        un message d'erreur est affiché.
        """
        try:
            if self.liste_personnages == []:
                self.fichier_courant = askopenfilename(title="Gestion personnages",filetypes=[('txt files','.txt'),('all files','.*')])
                Util.lire_fichier_personnages(self.fichier_courant,self.liste_personnages)
                self.mettre_a_jour_liste()
            else:
                if messagebox.askyesno('Gestion personnages',"Voulez-vous sauvegarder les données courantes avant d'ouvrir un nouveau fichier?"):
                    self.gestion_enregistrer_sous()
                self.fichier_courant = askopenfilename(title="Gestion personnages",filetypes=[('txt files','.txt'),('all files','.*')])
                self.liste_personnages = []
                Util.lire_fichier_personnages(self.fichier_courant,self.liste_personnages)
                self.mettre_a_jour_liste()
        except:
            return messagebox.showwarning("Erreur ouverture","L'ouverture du fichier a rencontrée une erreur")


    def gestion_enregistrer(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans le fichier courant.
        Si on a un fichier courant, on écrit les personnages de la liste dedans
        (voir méthode ecrire_fichier_personnages dans la classe Util) et on affiche un message approprié.
        Si l'enregistrement n'a pas fonctionné, un message d'erreur est affiché. Si on n'a pas de fichier courant,
        on enregistre dans un nouveau fichier en appelant la méthode (gestion_enregistrer_sous).
        """
        if self.fichier_courant != "":
            try:
                Util.ecrire_fichier_personnages(self.fichier_courant,self.liste_personnages)
                return messagebox.showinfo('Sauvegarde',"Sauvegarde des données effectuée correctement")
            except:
                return messagebox.showwarning("Erreur sauvegarde","La sauvegarde a rencontrée une erreur")
        else:
            return self.gestion_enregistrer_sous()


    def gestion_enregistrer_sous(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans un nouveau fichier.
        On demande un nom de fichier à  l'utilisateur, on l'assigne au fichier courant et on écrit
        dedans les personnages (voir méthode ecrire_fichier_personnages dans la classe Util).
        Afficher un message personnalisé s'il y a erreur lors de la sauvegarde ou si la sauvegarde est ok.
        """
        try:
            self.fichier_courant = asksaveasfilename(title="Gestion personnages",filetypes=[('txt files','.txt'),('all files','.*')])
            Util.ecrire_fichier_personnages(self.fichier_courant, self.liste_personnages)
            return messagebox.showinfo('Sauvegarde',"Sauvegarde des données effectuée correctement")
        except:
            return messagebox.showwarning("Erreur sauvegarde","La sauvegarde a rencontrée une erreur")


    def gestion_fermer(self):
        """
        Permet de fermer le fichier courant. Si la liste n'est pas vide et que l'utilisateur veut sauvegarder ses
        donnÃ©es, enregistrer les donnÃ©es de la liste dans le fichier courant (gestion_enregistrer) ou dans un
        nouveau fichier (gestion_enregistrer_sous) sâ€™il nâ€™y a pas de fichier courant.
        La liste est vidÃ©e et le fichier courant devient null.
        """
        if self.liste_personnages != []:
            if messagebox.askyesno('Gestion personnages',"Voulez-vous sauvegarder les données courantes avant de vider la liste de personnages"):
                self.gestion_enregistrer()
            self.liste_personnages = []
            self.fichier_courant = ""
            self.mettre_a_jour_liste()


    def gestion_quitter(self):
        """
        Permet de quitter l'application aprÃ¨s confirmation de l'utilisateur.
        """
        if messagebox.askyesno("Gestion personnages","Voulez-vous vraiment quitter ce programme?"):
            sys.exit()