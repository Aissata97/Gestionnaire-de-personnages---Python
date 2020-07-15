
from tkinter import *
from tkinter.filedialog import *

from gestion_personnages import GestionPersonnages
from sorcier import Sorcier
from guerrier import Guerrier

liste_personnages_precedent = []
pf = True

class Interface(Frame):
    """
    Classe héritant d'un Frame de TKInter et permetant d'afficher et de gérer l'interface graphique.
    """
    gp = GestionPersonnages()

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        global liste_personnages_precedent, pf
        pareil = True
        if len(Interface.gp.liste_personnages) != len(liste_personnages_precedent):
            pareil = False
        ind = 0
        try:
            while pareil and ind < len(Interface.gp.liste_personnages):
                if (isinstance(Interface.gp.liste_personnages[ind],Guerrier) and isinstance(liste_personnages_precedent[ind],Sorcier)) or (isinstance(Interface.gp.liste_personnages[ind],Sorcier) and isinstance(liste_personnages_precedent[ind],Guerrier)) and pareil:
                    pareil = False
                elif Interface.gp.liste_personnages[ind].nom != liste_personnages_precedent[ind].nom and pareil:
                    pareil = False
                elif Interface.gp.liste_personnages[ind].energie_depart != liste_personnages_precedent[ind].energie_depart and pareil:
                    pareil = False
                elif Interface.gp.liste_personnages[ind].energie_courante != liste_personnages_precedent[ind].energie_courante and pareil:
                    pareil = False
                elif isinstance(Interface.gp.liste_personnages[ind],Guerrier) and pareil:
                    if Interface.gp.liste_personnages[ind].force != liste_personnages_precedent[ind].force:
                        pareil = False
                elif isinstance(Interface.gp.liste_personnages[ind],Sorcier) and pareil:
                    if Interface.gp.liste_personnages[ind].nbr_charmes != liste_personnages_precedent[ind].nbr_charmes:
                        pareil = False
                ind+=1
        finally:
            if not pareil or pf:
                self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")
                self.parent.configure(width=800,height=400)

                self.menubar = Menu(self.parent)
                filemenu = Menu(self.menubar, tearoff=0)
                filemenu.add_command(label="Ouvrir...", command=Interface.gp.gestion_ouvrir)
                filemenu.add_command(label="Enregistrer", command=Interface.gp.gestion_enregistrer)
                filemenu.add_command(label="Enregistrer sous...", command=Interface.gp.gestion_enregistrer_sous)
                filemenu.add_command(label="Fermer", command=Interface.gp.gestion_fermer)
                filemenu.add_command(label="Quitter", command=Interface.gp.gestion_quitter)
                self.menubar.add_cascade(label="Fichier", menu=filemenu)
                self.parent.config(menu=self.menubar)

                self.yDefilB = Scrollbar(self.parent, orient='vertical')
                self.yDefilB.grid(row=0, column=1, rowspan=5, sticky='ns')

                self.liste = Listbox(self.parent,width=80,height=22,yscrollcommand=self.yDefilB.set,activestyle=NONE)
                self.liste.grid(row=0, column=0, rowspan=5, sticky='nsew')
                self.yDefilB['command'] = self.liste.yview

                for personnage in Interface.gp.liste_personnages:
                    self.liste.insert(END,personnage.to_string())

                self.bouton=Button(self.parent, text="Créer un sorcier", height=4, width=35, command=Interface.gp.gestion_creer_sorcier)
                self.bouton.grid(row=0,column=2)

                self.bouton1=Button(self.parent, text="Créer un guerrier", height=4, width=35, command=Interface.gp.gestion_creer_guerrier)
                self.bouton1.grid(row=1,column=2)

                self.bouton2=Button(self.parent, text="Attaquer", height=4, width=35, command=lambda : Interface.gp.gestion_attaquer(self.liste.curselection()))
                self.bouton2.grid(row=2,column=2)

                self.bouton3=Button(self.parent, text="Réinitialiser l'énergie", height=4, width=35, command=lambda : Interface.gp.gestion_augmenter_energie(self.liste.curselection()))
                self.bouton3.grid(row=3,column=2)

                self.bouton4=Button(self.parent, text="Crier", height=4, width=35, command=lambda : Interface.gp.gestion_crier(self.liste.curselection()))
                self.bouton4.grid(row=4,column=2)

                liste_personnages_precedent = []
                for e in Interface.gp.liste_personnages:
                    if isinstance(e,Guerrier):
                        liste_personnages_precedent.append(Guerrier(e.nom,e.energie_depart,e.energie_courante,e.force))
                    elif isinstance(e,Sorcier):
                        liste_personnages_precedent.append(Sorcier(e.nom,e.energie_depart,e.energie_courante,e.nbr_charmes))
                pf = False

        return self.parent.after(1000,self.initUI)


root = Tk()
I = Interface(root)
root.mainloop()