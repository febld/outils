#!/usr/bin/python3
# encoding=utf8

import codecs
import locale
import re
import sys

DEBUG = ""

TAILLE_MAX_LIGNE = 42
TAILLE_MAX_NOM   = 12

SEP_EGAL    = " = "
SEP_VIRGULE = ", "

LOCALE1 = "es_ES.utf-8"
LOCALE2 = "fr_FR.utf-8"

dico        = dict()
dicoInverse = dict()
liens       = dict()

# ------------------------------------------------------------------------------
def main():

    if len( sys.argv ) != 2 and len( sys.argv ) != 4:
        print( "Fournir le fichier en entrée !" )
        quit()

    egaliser( sys.argv[1] )
    if len( sys.argv ) == 4:
        LOCALE1 = sys.argv[2]
        LOCALE2 = sys.argv[3]

# ------------------------------------------------------------------------------
def egaliser( nomFichier ):

    #afficherDico( nomFichier )
    dico = lireFichier( nomFichier )
    afficherDico( dico, LOCALE1 )
    dicoInverse = creerDicoInverse ( dico )
    afficherDico( dicoInverse, LOCALE2 )

# ------------------------------------------------------------------------------
def lireFichier( nomFichier ):

    monDico = dict()

    regexLettre = re.compile( "^\s*([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\s*$" )
    regexEqual = re.compile( "^([^=]+)=(.*)$" )
    regexLien = re.compile( "^([^->]+)->(.*)$" )
    regexMots = re.compile( "^\s*([^\s+].*)$" )

    nom = ""
    f = open( nomFichier, "r" )
    for l in f:
        if regexEqual.match( l ):
            match = regexEqual.search( l )
            nom = match.group(1).strip()
            logDebug( "EGAL   : " + nom + " = " + match.group(2) )
            ajouterValeursMotDico( monDico, nom, match.group(2) )
        elif regexLettre.match( l ) :
            nom = ""
            logDebug( "LETTRE : " + l.rstrip() )
        elif regexLien.match( l ) :
            match = regexLien.search( l )
            nom = match.group(1).strip()
            logDebug( "LIEN   : " + nom + " -> " + match.group(2) )
            ajouterValeursMotDico( monDico, nom, match.group(2) )
        elif nom and regexMots.match( l ):
            match = regexMots.search( l )
            logDebug( "VALEUR : " + nom + " ... " + match.group(1) )
            ajouterValeursMotDico( monDico, nom, match.group(1) )
        else:
            logErreur( "IGNORE : " + l.rstrip() )
    f.close()

    return monDico

# ------------------------------------------------------------------------------
def creerDicoInverse( pDico ):

    monDico = dict()

    for ( index, listeMots ) in pDico.items():
        for (mot, valeurs ) in listeMots.items():
            for valeur in valeurs:
                if "?" in valeur:
                    logInfo("valeur non sûre non ajoutée : " + valeur + "=" + mot)
                    continue
                ajouterValeursMotDico( monDico, valeur, mot )

    return monDico

# ------------------------------------------------------------------------------
def ajouterValeursMotDico( pDico, pMot, pValeurs ):

    if ( pMot and pValeurs ):
        #logDebug("AJOUT : " + pMot + " = " + pValeurs )

        index = pMot.upper()[0]
        valeursBrutes = re.split( '[,/]', pValeurs )

        if not index in pDico:
            pDico[index] = dict()
        
        valeurs = []
        if pMot in pDico[index]:
            valeurs = pDico[index][pMot]

        for mot in valeursBrutes:
            if not mot.strip() in valeurs:
                valeurs.append( mot.strip() )

        pDico[index][pMot] = valeurs
    else:
        print( "ERREUR ajouterValeursMotDico : paramètres erronnés [" + pMot + "/" + pValeurs + "]" )

# ------------------------------------------------------------------------------
def afficherDico( pDico, pLocale ):

    logDebug("LOCALE = " + pLocale )
    locale.setlocale( locale.LC_ALL, pLocale ) # for correct sorting purpose

    for ( index, listeMots ) in sorted ( pDico.items(), key = lambda item: locale.strxfrm( item[0] ) ):
        print(index)
        for ( mot, valeurs ) in sorted( listeMots.items(), key = lambda item: locale.strxfrm( item[0] ) ):
            if mot == "?":
                continue
            afficherLigneMot( mot, valeurs )
        print("")

# ------------------------------------------------------------------------------
def afficherLigneMot( pMot, pValeurs ):

    formatLigneNom = "{:" + str(TAILLE_MAX_NOM) + "}" + SEP_EGAL
    tailleMaxReste = TAILLE_MAX_LIGNE - ( TAILLE_MAX_NOM + len( SEP_EGAL ) )

    if pMot and pValeurs:
        ligne = formatLigneNom.format( pMot )
        reste = ""
        i = 0
        while i < len( pValeurs ):
            if not pValeurs[i]:
                i += 1
                continue
            elif len( reste ) == 0:
                reste = pValeurs[i]
            elif len(reste) + len(pValeurs[i]) + len(SEP_VIRGULE) > tailleMaxReste:
                print(ligne + reste)
                ligne = " " * ( TAILLE_MAX_NOM + len( SEP_EGAL ) )
                reste = pValeurs[i]
            else:
                reste = reste + SEP_VIRGULE + pValeurs[i]

            i += 1

        if reste:
                print(ligne + reste)

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
