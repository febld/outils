#!/usr/bin/python3
# encoding=utf8

import codecs
import re
import sys

# ------------------------------------------------------------------------------
def main():

    if len( sys.argv ) == 2:
        egaliser( sys.argv[ 1 ] )
    else:
        print( "Fournir le fichier en entrée !" )


# ------------------------------------------------------------------------------
def egaliser( fileIn ):

    regex = re.compile( "^([^=]+)=(.*)$" )
    f = open( fileIn, "r" )
    for l in f:
        match = regex.search( l )
        if match:
            print( "{:12} ={}".format( match.group(1).strip(),  match.group(2) ) )
        else:
            print( l.rstrip() )
    f.close()


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    
    main()
