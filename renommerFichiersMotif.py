#!/usr/bin/python3
# encoding=utf8

import codecs
import locale
import os
import re
import sys

DEBUG = "VRAI"

TAILLE_MAX_LIGNE = 42
TAILLE_MAX_NOM   = 12

# ------------------------------------------------------------------------------
# Fonction d'incrémentation d'index
#
#def increment:
#    result=$(expr $1 + 1)
#    prefix="00"
#    if [ $result -ge 10  -a $result -lt 100 ]
#    then
#        prefix="0"
#    elif [ $result -ge 100 ]
#    then 
#        prefix=""
#    fi
#    echo ${prefix}${result}

# ------------------------------------------------------------------------------
# Principal
# ------------------------------------------------------------------------------
def main():

    if len( sys.argv ) != 3 :
        usage()
        quit()

    listerEtRenommer( ".", sys.argv[1], sys.argv[2] )

# ------------------------------------------------------------------------------
# Usage
# ------------------------------------------------------------------------------
def usage():
    print( "" ) 
    print( "Usage : " + os.path.basename(__file__) + " MOTIF_SRC MOTIF_DEST" )
    print( "" )
    print( "Renomme une série de fichiers dans le répertoire courant :" )
    print( "    . dont le nom commence par le motif MOTIF_SRC" )
    print( "    . vers un fichier avec un nom :" )
    print( "         . commençant par le motif MOTIF_DEST" )
    print( "         . suffixé par un index automatique" )
    print( "         . suffixé par l'extension du fichier original" )
    print( "" )

# ------------------------------------------------------------------------------
def listerEtRenommer( dossier, motifSrc, motifDst ):

    if not os.path.isdir( dossier ) :
        logErreur( "dossier source incorrect : " + dossier )
        quit()

    regexMOTIF = re.compile( "^" + motifSrc + ".*$" )

    # Initialisation liste des fichiers
    dicoFichiers = dict()
    liste = os.listdir( dossier ).sort()
    fichiers = []
    for f in sorted( os.listdir( dossier ) ):
        if os.path.isfile( os.path.join( dossier, f )) and regexMOTIF.match( f ):
            root, ext = os.path.splitext( f )
            logInfo( "Sélection fichier   : " + root + ext )
            fichiers.append( (root, ext) );
        else:
            logDebug( "fichier rejeté      : " + f )

    pad = len( "{}".format( len( fichiers )) )
    logInfo( f"TOTAL sélectionné   : {len( fichiers )} (pad={pad:d})" )

    # Vérification avant renommage des fichiers
    index = 1
    onContinue = 1
    for root, ext in fichiers:
        cible = f"{motifDst}-{str(index).zfill(pad)}{ext}"
        if os.path.isfile( os.path.join( dossier, cible ) ):
            logErreur( f"Vérification cible   : KO fichier cible existe déjà --> {cible}" )
            onContinue = 0
        else:
            logInfo( f"Vérification cible   : OK fichier cible inexistant   --> {cible}" )
        index += 1
    if not onContinue:
        logErreur( "" )
        logErreur( "des fichiers cibles existent déjà. Veuillez corriger avant de continuer. Abandon" )
        logErreur( "" )
        quit()

    # Renommage des fichiers
    index = 1
    for root, ext in fichiers:
        cible = f"{motifDst}-{str(index).zfill(pad)}{ext}"
        logInfo( f"Renommage fichier   : {root}{ext} --> {cible}" )
        os.rename( f"{root}{ext}", cible )
        index += 1


# ------------------------------------------------------------------------------
def logDebug( msg ):

    if DEBUG:
        print( "DEBUG  " + msg )

# ------------------------------------------------------------------------------
def logInfo( msg ):

    print( "INFO   " + msg )

# ------------------------------------------------------------------------------
def logErreur( msg ):

    print( "ERREUR " + msg )

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    
    main()
