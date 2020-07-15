
from tkinter.filedialog import *
from tkinter import simpledialog, messagebox
from sorcier import Sorcier
from guerrier import Guerrier


class Util:
    """
    Classe utilitaire comportant uniquement des méthodes statiques.
    """

    TYPE_SORCIER = "Sorcier"
    TYPE_GUERRIER = "Guerrier"


    @staticmethod
    def lire_fichier_personnages(fichier, liste_personnages):
        """
        Permet de lire un fichier de personnages reçu en entrée et de remplir la liste de personnages. Pour plus
        de détails, voir l'énoncé du travail.
        Args:
            fichier (str): Le nom du fichier à lire
            liste_personnages (list): La liste de personnages que la méthode doit remplir.

        Returns:

        """
        try:
            f = open(fichier,'r')
            L = f.readlines()
            for ligne in L:
                ligne = ligne[:-1]
                personnage,nom,energie_depart,energie,pouvoir=ligne.split(";")
                if personnage == Util.TYPE_GUERRIER:
                    liste_personnages.append(Guerrier(nom,energie_depart,energie,pouvoir))
                elif personnage == Util.TYPE_SORCIER:
                    liste_personnages.append(Sorcier(nom,energie_depart,energie,pouvoir))
            f.close()
            return True
        except:
            return messagebox.showwarning("Erreur lecture fichier","La lecture du fichier a rencontrée une erreur")


    @staticmethod
    def ecrire_fichier_personnages(fichier, liste_personnages):
        """
        Permet d’écrire la liste de personnages reçue en paramètre dans le fichier de personnages aussi reçu en entrée.
        Pour plus de détails, voir l'énoncé du travail.
        Args:
            fichier:
            liste_personnages:
        """
        try:
            f = open(fichier,'w')
            for personnage in liste_personnages:
                if isinstance(personnage,Guerrier):
                    f.write("Guerrier;{};{};{};{}\n".format(personnage.get_nom(),personnage.get_energie_depart(),personnage.get_energie_courante(),personnage.get_force()))
                elif isinstance(personnage,Sorcier):
                    f.write("Sorcier;{};{};{};{}\n".format(personnage.get_nom(),personnage.get_energie_depart(),personnage.get_energie_courante(),personnage.get_nbr_charmes()))
            return True
        except:
            return messagebox.showwarning("Erreur ecriture fichier","L'écriture du fichier a rencontrée une erreur")


    @staticmethod
    def saisir_objet_entier(question):
        """
        Permet de demander la saisie d'un entier et de le valider
        Args:
            question (str): La question à poser

        Returns (int): L'entier saisi

        """
        objet_entier = -1

        valide = False

        while not valide:
            objet_entier = simpledialog.askstring("Saisie d'un entier", question)

            try:
                objet_entier = int(objet_entier)
                valide = True
            except ValueError:
                print("aucune sasie")

        return objet_entier


    @staticmethod
    def saisir_string(question):
        """
        Permet de demander la saisie d'une chaîne de caractères
        Args:
            question (str): La question à poser

        Returns (str): La chaîne saisie

        """
        string_temp = ""

        valide = False

        while string_temp == "" and not valide:
            string_temp = simpledialog.askstring("Saisie d'une chaine de caractères", question)

            if string_temp == "":
                print("aucune saisie")
            else:
                valide = True

        return string_temp
