#!/usr/bin/python3

"""Outil de gestion des connexions SSH

Auteur : François-Eugène Belliard 2025
   
->> Historique -----------------------------------------------------------------

26.06.2025 : François-Eugène Belliard / Création

->> Schéma architecture --------------------------------------------------------

   PRESENTATION :
       gestion de l'affichage
       interactions utilisateurs
   
   TRAITEMENT :
       gestion des opérations : lancement des connexions
   
   DONNÉES
       définition/configuration des connexions à gérer
   
   
   °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
   |
D  | Configuration dans un fichier JSON : ~/ssh-hosts.py.json
O  | Exemple :
N  |
N  |   {
É  |       "hosts": [
E  |           { "nom": "nom1", "hostname" : "serveur1", "description"  : "Serveur 1", "user" : "fbelliard" },
S  |           { "nom": "nom2", "hostname" : "serveur2", "description"  : "Serveur 2", "user" : "fbelliard" }
   |       ]
   |   }
   |
   °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
   
   
"""

# ->>>--------------------------------------------------------------------------
# Imports
#
import os
import sys
import cmd
import re
import json
from pathlib import Path


# ->>>--------------------------------------------------------------------------
# Variables
#
__version__ = "0.0.1"
debug = False
script = os.path.basename(__file__)
confFilename = script + ".json"
confPath = Path.home() / ".config" / script / confFilename
jsonModele = """{
    "hosts": [
        { "nom" : "SERVEUR_1", "user" : "login1", "hostname" : "host1.mondomaine.com", "description" : "Description serveur 1" },
        { "nom" : "SERVEUR_2", "user" : "login2", "hostname" : "host2.mondomaine2.fr", "description" : "Description serveur 2" }
    ]
}
"""

# ->>>--------------------------------------------------------------------------
def principale():
    """Gère l'exécution globale du script.
    """
    
    if sys.version_info[0] < 3:
        print("Cette version de l'outil est conçue pour Python 3.")
        return
    if not confPath.exists():
        print("Erreur : créez un fichier de configuration avant de démarrer dans\n   " + str(confPath))
        print("\nLe fichier est un fichier JSON répondant au modèle ci-dessous :" )
        print( jsonModele )
        return
            
    
    presentation = PresentationTXT()
    presentation.demarrer()
    

# ->>>--------------------------------------------------------------------------
class PresentationTXT(cmd.Cmd):
    """Classe definissant une interface de présentation en mode texte.
    """

    separateurCmd = re.compile(" +")
    
    # ->>>----------------------------------------------------------------------
    def __init__(self):
        """Constructeur de la classe.
        """
        
        # __init__ de la super-classe cmd.Cmd
        cmd.Cmd.__init__(self)

        # attributs propres à la classe
        self.stdprompt = script + "-" +__version__+"> "
        
        # attributs hérités
        self.prompt = self.stdprompt
        if debug:
            self.prompt += "--DEBUG-->> "
        
        self.intro = "Bienvenue sur le gestionnaire de connexions SSH.\n" \
                   + "Entrez \"help\" ou ? pour lister les commandes."
        self.sessions = SessionsSSH()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def demarrer(self):
        """Initialise la présentation texte.
        """
    
        # affichage de l'interface de commande
        self.cmdloop()
    # -<<<----------------------------------------------------------------------
        
    def do_aide(self, ligne):
        """aide
        
        Affiche l'aide du programme.
        """
        print("\n"\
              +" Commandes documentées\n"\
              +"=============================================\n"\
              +". aide|help    : affiche l'aide\n"\
              +". list         : liste les connexions SSH disponibles\n"\
              +". ssh          : gère le démarrage d’une connexion SSH\n"\
              +". sftp         : gère le démarrage d’une connexion SFTP\n"\
              +". bye|salut    : quitte l'application\n"
              )
        
        self.do_help(ligne)
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def emptyline(self):
        """Redéfinition de la méthode héritée de cmd.Cmd
        """
        
        pass
    # -<<<----------------------------------------------------------------------

    # ->>>----------------------------------------------------------------------
    def do_bye(self, ligne):
        """bye
        
        Quitte l'interface de commande.
        """
        return self.do_EOF(ligne)

    def do_quit(self, ligne):
        """quit
        
        Quitte l'interface de commande.
        """
        return self.do_EOF(ligne)

    def do_exit(self, ligne):
        """exit
        
        Quitte l'interface de commande.
        """
        return self.do_EOF(ligne)

    def do_salut(self, ligne):
        """salut
        
        Quitte l'interface de commande.
        """
        return self.do_EOF(ligne)

    def do_EOF(self, ligne):
        """EOF
        
        Quitte l'interface de commande.
        """
        
        print("salut bye bye !")
        return True
    # -<<<----------------------------------------------------------------------

    # ->>>----------------------------------------------------------------------
    def do_list(self, ligne):
        """list [<MOTIF>]
        
        Affiche les connexions SSH disponibles ou si un MOTIF est fourni, uniquement celles contenant la chaine MOTIF dans leur nom
        """
        
        args = self.separateurCmd.split(ligne)
        if len(args) == 1 and len(args[0]) > 0:
            self.sessions.afficherTous(args[0])
        else:
            self.sessions.afficherTous(None)
    # -<<<----------------------------------------------------------------------

    # ->>>----------------------------------------------------------------------
    def do_ssh(self, ligne):
        """ssh ( <ID> | <NOM_SESSION_SSH> )
        
        Gère le lancement d’une connexion SSH'
        """
        
        args = self.separateurCmd.split(ligne)
        if len(args) == 1 and len(args[0]) > 0:
            self.sessions.demarrer(args[0], "ssh")
        else:
            self.do_help("ssh")
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def do_sftp(self, ligne):
        """sftp ( <ID> | <NOM_SESSION_SSH> )
        
        Gère le lancement d’une connexion SFTP'
        """
        
        args = self.separateurCmd.split(ligne)
        if len(args) == 1 and len(args[0]) > 0:
            self.sessions.demarrer(args[0], "sftp")
        else:
            self.do_help("sftp")
    # -<<<----------------------------------------------------------------------
    
    

# ->>>--------------------------------------------------------------------------
class SessionsSSH():
    """Classe gérant les sessions SSH/SFTP.
    """
    
    hosts = []
    
    # ->>>----------------------------------------------------------------------
    def __init__(self):
        
        print("Chargement config json ...")
        config = None
        if confPath.exists():
            with confPath.open() as f:
                config = json.load(f)
        else:
            print("Configuration n'existe pas : " + str(confPath))
            
        if config is not None:
            for t in config["hosts"] :
                self.hosts.append(Host(
                    t["nom"],
                    t["hostname"],
                    t["description"],
                    t["user"]
                    ))
            self.afficherTous(None)
        else:
            print("Configuration is none")
    # -<<<----------------------------------------------------------------------

    # ->>>----------------------------------------------------------------------
    def afficherTous( self, motif ):
        modele = "{:>3}  {:<25}  {:<45}  {:<25}"
        print( modele.format( "ID", "Nom", "user@host", "Description" ) )
        print( modele.format( "-" * 3, "-" * 25, "-" * 45, "-" * 25 ) )
        i = 0
        for h in self.hosts:
            i += 1
            if ( ( not motif is None ) and ( not motif.lower() in h.nom.lower() ) ):
                continue
            print( modele.format( i, h.nom, h.user + "@" + h.hostname, h.description ) )
        print()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def afficherDetails(self, nom):
        for h in self.hosts:
            if h.nom == nom:
                h.afficherDetails()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def demarrer(self, nom, mode):
        if nom.isnumeric() and ( int( nom ) <= len( self.hosts ) ) :
                self.hosts[ int( nom ) - 1 ].demarrer( mode )
        else:
            for h in self.hosts:
                if h.nom == nom:
                    h.demarrer( mode )
    # -<<<----------------------------------------------------------------------
    
# -<< Classe SessionsSSH -------------------------------------------------------

# ->>>--------------------------------------------------------------------------
class Host():
    """Classe définissant un Host SSH.
    """
    
    # ->>>----------------------------------------------------------------------
    def __init__(self, nom, hostname, description, user):
        """Constructeur Host.
        
        Attributs:
            . nom            = nom générique du host (unique)
            . hostname       = hostname DNS ou adresse IP du host
            . description    = description du host
            . user           = nom de l’utilisateur à utiliser pour la connexion SSH
        """
        
        cmd.Cmd.__init__(self)
        
        self.nom = nom
        self.hostname = hostname
        self.description = description
        self.user = user
    # -<<<----------------------------------------------------------------------
        
    # ->>>----------------------------------------------------------------------
    def demarrer(self, mode):
        """Démarre une connexion SSH
        """
        
        if  mode is None or mode != "ssh" or mode != "sftp":
            print( "ERREUR mode de commande non reconnu : {}".format( mode ) )

        if self.nom is None \
           or self.hostname is None :
            print( "Erreur : host mal configuré !" )
            self.afficherDetails() 
            return
        
        commande = mode + " " + self.hostname
        if not self.user is None and len( self.user ) > 0 :
            commande = mode + " " + self.user + "@" + self.hostname

        print(" SSH/SFTP : " + commande )
        os.system( commande )
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def afficherDetails(self):
        """Affiche les attributs du host.
        """
        
        print("Host :\n"\
              +"    . nom         = " + self.nom + "\n"\
              +"    . hostname    = " + self.hostname + "\n"\
              +"    . description = " + self.description + "\n"\
              +"    . user        = " + self.user
              )
    # -<<<----------------------------------------------------------------------
    
# ->>> Principal ---------------------------------------------------------------
#
if __name__ == "__main__":
    if debug:
        print("encodage : "+sys.getdefaultencoding())
        locale = locale.getdefaultlocale()
        print("locale   : "+locale[0]+"/"+locale[1])
    
    principale()


