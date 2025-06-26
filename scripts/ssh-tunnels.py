#!/usr/bin/python3

"""Outil de gestion de tunnels SSH

Auteur : francois.belliard@gfi.fr
   
->> Historique -----------------------------------------------------------------

14.12.2018 : v0.0.1 / François Belliard / Création
17.12.2018 : v0.0.2 / François Belliard / Mise à jour
18.12.2018 : v0.0.3 / François Belliard / Gestion stdout processus et màj statut
02.01.2019 : v0.0.4 / François Belliard / Màj présentation statut

->> Schéma architecture --------------------------------------------------------

   PRESENTATION :
       gestion de l'affichage
       interactions utilisateurs
   
   TRAITEMENT :
       gestion des opération : démarrage/arrêt tunnels
   
   DONNÉES
       définition/configuration des tunnels à gérer
   
   
   °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
   |
P  |   .------------------------. 
R  |   |PresentationTXT(cmd.Cmd)|
E  |   o------------------------o
S  |   | .                      |
E  |   | .                      |
N  |   | demarrer()             |
T  |   | do_XXXXX()             |
A  |   | <heritage cmd.Cmd>     |
T  |   |                        |
I  |   o------------------------o
O  |
N  |
   |
   °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
   |
T  |      o----------------o      o----------------o
R  |      |    Tunnels     |      |     Tunnel     |
A  |      o----------------o      |.nom            |
I  |      |.tunnels[]      |      |.type           |
T  |      |.               |      |.portLocal      |
E  |      |.               |      |.distant        |
M  |      |.               |      |.portDistant    |
E  |      |.               |      |.utilisateurSSH |
N  |      |.               |      |.serveurSSH     |
T  |      |.               |      |.processus      |
   |      |.               |      |afficher()      |
   |      o----------------o      |arreter()       |
   |                              |demarrer()      |
   |                              o----------------o
   |
   °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
   |
D  | Configuration dans un fichier JSON : ~/ssh-tunnels.py.json
O  | Exemple :
N  |    {
N  |        "tunnels": [
E  |            {
E  |                "nom"            : "serveur2-ssh",
S  |                "portLocal"      : "2022",
   |                "distant"        : "10.5.5.5",
   |                "portDistant"    : "22",
   |                "serveurSSH"     : "192.168.1.10",
   |                "utilisateurSSH" : "fbelliard"
   |            },
   |            ...
   |        ]
   |    }
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
import subprocess
import json
from pprint import pprint
import threading
import queue
from pathlib import Path


# ->>>--------------------------------------------------------------------------
# Variables
#
__version__ = "0.0.3"
debug = False
script = os.path.basename(__file__)

# ->>>--------------------------------------------------------------------------
def principale():
    """Gère l'exécution globale du script.
    """
    
    if sys.version_info[0] < 3:
        print("Cette version de l'outil est conçue pour Python 3.")
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
        
        self.intro = "Bienvenue sur le gestionnaire de tunnels SSH.\n" \
                   + "Entrez \"help\" ou ? pour lister les commandes."
        self.tunnels = Tunnels()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def demarrer(self):
        """Initialise la présentation texte.
        """
    
        # affichage de l'interface de commande
        self.cmdloop()
    # -<<<----------------------------------------------------------------------
        
    # ->>>----------------------------------------------------------------------
    #def do_help(self, ligne):
    #    self.do_aide(ligne)
        
    def do_aide(self, ligne):
        """aide
        
        Affiche l'aide du programme.
        """
        print("\n"\
              +" Commandes documentées\n"\
              +"=============================================\n"\
              +". aide|help    : affiche l'aide\n"\
              +". statut       : affiche le statut des tunnels\n"\
              +". start        : gère le démarrage des tunnels\n"\
              +". stop         : gère l'arrêt des tunnels\n"\
              +". restart      : gère l'arrêt/redémarrage des tunnels\n"\
              +". debug on|off : active/désactive le mode debug\n"\
              +". bye|salut    : quitte l'application\n"
              )
        
        self.do_help(ligne)
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def afficherOptions(self):
        """"Affiche les valeurs actives des options.
        """
        
        if debug:
            print("    . debug             :   vrai")
        else:
            print("    . debug             :   faux")
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def do_debug(self,ligne):
        """debug on|off
        
        Active/désactive le mode debug.
        """
        
        global debug
        if ligne == "on":
            debug = True
            self.prompt = self.stdprompt + "--DEBUG ON-- "
        elif ligne == "off":
            debug = False
            self.prompt = self.stdprompt
        else:
            print("Syntaxe : debug on|off")
        self.afficherOptions()
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

    def do_salut(self, ligne):
        """salut
        
        Quitte l'interface de commande.
        """
        return self.do_EOF(ligne)

    def do_EOF(self, ligne):
        """EOF
        
        Quitte l'interface de commande.
        """
        
        print("Arrêt des tunnels ...")
        self.do_stop("all")
        
        print("salut bye bye !")
        return True
    # -<<<----------------------------------------------------------------------

    # ->>>----------------------------------------------------------------------
    def do_stop(self, ligne):
        """stop all|<NOM_TUNNEL>
        
        Gère l'arret des tunnels
        """
         
        args = self.separateurCmd.split(ligne)
        if len(args) == 1 and args[0] == "all" :
            self.tunnels.arreterTous()
            self.tunnels.statut()
        elif len(args) == 1 and len(args[0]) > 0 :
            self.tunnels.arreter(args[0])
            self.tunnels.statut()
        else:
            self.do_help("stop")
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def do_start(self, ligne):
        """start all|<NOM_TUNNEL>
        
        Gère le démarrage des tunnels'
        """
        
        args = self.separateurCmd.split(ligne)
        if  len(args) == 1 and args[0] == "all":
            self.tunnels.demarrerTous()
            self.tunnels.statut()
        elif len(args) == 1 and len(args[0]) > 0:
            self.tunnels.demarrer(args[0])
            self.tunnels.statut()
        else:
            self.do_help("start")
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def do_restart(self, ligne):
        """restart all|<NOM_TUNNEL>
        
        Gère l'arrêt et le démarrage des tunnels'
        """
        
        args = self.separateurCmd.split(ligne)
        if  len(args) == 1 and args[0] == "all":
            self.tunnels.arreterTous()
            self.tunnels.demarrerTous()
            self.tunnels.statut()
        elif len(args) == 1 and len(args[0]) > 0:
            self.tunnels.arreter(args[0])
            self.tunnels.demarrer(args[0])
            self.tunnels.statut()
        else:
            self.do_help("restart")
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def do_statut(self, ligne):
        """Affiche le statut des tunnels
        """
        
        self.tunnels.statut()
    # -<<<----------------------------------------------------------------------

# ->>>--------------------------------------------------------------------------
class Tunnels():
    """Classe gérant les tunnels SSH.
    """
    
    tunnels = []
    
    # ->>>----------------------------------------------------------------------
    def __init__(self):
        
        print("Chargement config json ...")
        confFilename = script + ".json"
        confPath = Path.home() / confFilename
        config = None
        if confPath.exists():
            with confPath.open() as f:
                config = json.load(f)
        else:
            print("Configuration n'existe pas : " + str(confPath))
            
        if config is not None:
            for t in config["tunnels"] :
                self.tunnels.append(Tunnel(
                    t["nom"],
                    t["portLocal"],
                    t["distant"],
                    t["portDistant"],
                    t["serveurSSH"],
                    t["utilisateurSSH"]
                    ))
                self.tunnels[len(self.tunnels)-1].afficher()
        else:
            print("Configuration is none")
    # -<<<----------------------------------------------------------------------

    # ->>>----------------------------------------------------------------------
    def afficher(self):
        for t in self.tunnels:
            t.afficher()
            print("\n")
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def demarrerTous(self):
        for t in self.tunnels:
                t.demarrer()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def demarrer(self, nom):
        for t in self.tunnels:
            if t.nom == nom:
                t.demarrer()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def arreterTous(self):
        for t in self.tunnels:
            t.arreter()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def arreter(self, nom):
        for t in self.tunnels:
            if t.nom == nom:
                t.arreter()
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def statut(self):
        """Affiche l'état des tunnels (1 tunnel par ligne)
        """
        
        separation = '+-{nom:16}-+-{typ:6}-+-{pid:5}-+-{loc:6}-+-{dis:24}-+-{pod:6}-+-{srv:38}-+'.format(
            nom = "----------------",
            typ = "------",
            pid = "-----",
            loc = "------",
            dis = "------------------------",
            pod = "------",
            srv = "--------------------------------------")

        print(separation)
        print('| {nom:16} | {typ:6} | {pid:5} | {loc:6} | {dis:24} | {pod:6} | {srv:38} |'.format(
            nom = "nom tunnel",
            typ = "type",
            pid = "pid",
            loc = "port L",
            dis = "hôte D",
            pod = "port D",
            srv = "SSH -> login@serveur:port"))
        print(separation)
        
        for t in self.tunnels:
            pStatus = ""
            if t.processus is None or t.processus.pid is None:
                pStatus = "s/o"
                id = "---"
            elif t.processus is not None and t.processus.poll() is None:
                pStatus = str(t.processus.pid)
            else:
                pStatus = "KO !"

            print('| {nom:16} | {typ:6} | {pid:5} | {loc:6} | {dis:24} | {pod:6} | {srv:38} |'.format(
                nom = str(t.nom),
                typ = str(t.type),
                pid = pStatus,
                loc = str(t.portLocal),
                dis = str(t.distant),
                pod = str(t.portDistant),
                srv = str(t.utilisateurSSH) + "@" + str(t.serveurSSH) + ":" + str(t.portSSH) ))

        print(separation)
    # -<<<----------------------------------------------------------------------
    
# -<< Classe Tunnels -----------------------------------------------------------

# ->>>--------------------------------------------------------------------------
class Tunnel():
    """Classe définissant un tunnel SSH.
    """
    
    # ->>>----------------------------------------------------------------------
    def __init__(self, nom, portLocal, distant, portDistant, serveurSSH, utilisateurSSH):
        """Constructeur Tunnel.
        
        Attributs:
            . nom            = nom générique du tunnel (unique)
            . type           = type de tunnel ssh : "local" ("distant" non géré)
            . portLocal      = port local
            . distant        = nom DNS ou @ip de l'hôte distant
            . portDistant    = port sur l'hôte distant
            . serveurSSH     = nom DNS ou @ip du serveur SSH servant de relais 
            . utilisateurSSH = login utilisateur sur le serveur SSH
            . portSSH        = port SSH sur le serveur SSH (22 par défaut)
            . processus      = objet process lorsque le tunnel est démarré
        """
        
        cmd.Cmd.__init__(self)
        
        self.nom = nom
        self.type = "local"
        self.portLocal = portLocal
        self.distant = distant
        self.portDistant = portDistant
        self.serveurSSH = serveurSSH
        self.utilisateurSSH = utilisateurSSH
        self.portSSH = "22"
        self.processus = None
    # -<<<----------------------------------------------------------------------
        
    # ->>>----------------------------------------------------------------------
    def demarrer(self):
        """Démarre le tunnel SSH.
        """
        
        prefix = "Tunnel " + str(self.nom) + " : "
        
        if self.nom is None \
           or self.portLocal is None \
           or self.distant is None \
           or self.portDistant is None \
           or self.serveurSSH is None \
           or self.utilisateurSSH is None :
            
            print("Erreur : tunnel mal configuré !")
            self.afficher() 
            return
        
        if self.type is not "local":
            print("ERREUR : tunnels n'est pas de type \"local\" !")
            self.afficher()
            
        if self.processus is None or self.processus.poll() == 0:
            print(prefix + "démarrage ...")
            argsList = ['ssh']
            argsList.append('-N')
            argsList.append('-L')
            argsList.append(self.portLocal + ':' + self.distant + ':' + self.portDistant)
            argsList.append(self.utilisateurSSH + '@' + self.serveurSSH)
            #argsList.append('&')
            processus = subprocess.Popen(argsList, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
            self.processus = processus
            stdout_reader = AsynchronousFileReader(processus.stdout, self.nom)
            stdout_reader.start()

            #print("proc.pid = " + str(processus.pid))
        else:
            print(prefix + "déjà démarré. PID=" + str(self.processus.pid))
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def arreter(self):
        """Arrête le tunnel SSH (kill du processus)
        """
        
        prefix = "Tunnel " + str(self.nom) + " : "
        
        if self.processus is None:
            print(prefix + "non démarré !")
        else:
            #argsList = ['kill']
            #argsList.append(str(self.pid))
            #processus = subprocess.Popen(argsList, shell=False)
            #if processus.returncode == 0 :
            #    print (prefix + "arrêt OK")
            #else:
            #    print(prefix + "arrêt KO -> vérifiez manuellement le process " + str(self.pid))
            
            #self.processus.kill()
            self.processus.terminate()
            self.processus = None
    # -<<<----------------------------------------------------------------------
    
    # ->>>----------------------------------------------------------------------
    def afficher(self):
        """Affiche les attributs du tunnel.
        """
        
        print("Tunnel :\n"\
              +"    . nom tunnel        = " + self.nom + "\n"\
              +"    . type              = " + str(self.type) + "\n"\
              +"    . port local        = " + str(self.portLocal) + "\n"\
              +"    . hôte:port distant = " + str(self.distant) + ":" + str(self.portDistant) + "\n"\
              +"    . login@serveur SSH = " + str(self.utilisateurSSH) + "@" + str(self.serveurSSH) + ":" + str(self.portSSH) + "\n"\
              +"    . ID processus      = " + " s/o " if self.processus is None or self.processus.pid is None else str(self.processus.pid) + "\n"\
              )
    # -<<<----------------------------------------------------------------------
    
# ->>>--------------------------------------------------------------------------
class AsynchronousFileReader(threading.Thread):
    '''
    Helper class to implement asynchronous reading of a file
    in a separate thread. Pushes read lines on a queue to
    be consumed in another thread.
    '''

    def __init__(self, fd, prefix):
        #assert isinstance(queue, queue.Queue)
        assert callable(fd.readline)
        threading.Thread.__init__(self)
        self._fd = fd
        #self._queue = queue
        if prefix is not None:
            self._prefix = prefix +  " : "
        else:
            self._prefix = ""

    def run(self):
        '''The body of the tread: read lines and put them on the queue.'''

        for line in iter(self._fd.readline, b''):
            print(self._prefix + line.decode("utf-8"))

    def eof(self):
        '''Check whether there is no more content to expect.'''
        return not self.is_alive()
# -<<<--------------------------------------------------------------------------


# ->>> Principal ---------------------------------------------------------------
#
if __name__ == "__main__":
    if debug:
        print("encodage : "+sys.getdefaultencoding())
        locale = locale.getdefaultlocale()
        print("locale   : "+locale[0]+"/"+locale[1])
    
    principale()



