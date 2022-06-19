#!/bin/sh
#

# ------------------------------------------------------------------------------
# Fonction d'incrémentation d'index
#
usage() {
    echo 
    echo "Usage : $(basename $0) MOTIF_SRC MOTIF_DEST"
    echo
    echo "Renomme une série de fichiers dans le répertoire courant :"
    echo "    . dont le nom commence par le motif MOTIF_SRC"
    echo "    . vers un fichier avec un nom commençant par le motif MOTIF_DEST"
    echo "      suffixé par un index automatique"
    echo
}

# ------------------------------------------------------------------------------
# Fonction d'incrémentation d'index
#
increment() {
    result=$(expr $1 + 1)
    prefix="00"
    if [ $result -ge 10  -a $result -lt 100 ]
    then
        prefix="0"
    elif [ $result -ge 100 ]
    then 
        prefix=""
    fi
    echo ${prefix}${result}
}

# ------------------------------------------------------------------------------
# Principal
#

[ -z "$1" -o -z "$2" ] && usage && exit 1

MOTIF_SRC=$1
MOTIF_DEST=$2

export i=0
ls -atr ${MOTIF_SRC}* | while read f
do
    i=$(increment $i)
    echo "$f -> ${MOTIF_DEST}_$i"
    mv $f ${MOTIF_DEST}_$i
done

