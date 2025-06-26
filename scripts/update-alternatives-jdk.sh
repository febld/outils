#!/bin/bash

# :1,$s/^\(.*\)$/update-alternatives --install \"\/usr\/bin\/\1\" \"\1\" \"\/usr\/lib\/jvm\/jdk-17\/bin\/\1\" 1
export BIN_LIEN="/usr/bin"
export BIN_JDK_17="/usr/lib/jvm/jdk-17/bin"
export BIN_OPENJDK_11="/usr/lib/jvm/java-11-openjdk-amd64/bin"
export PRIORITE="1"

NOMS_JDK_17="jar jarsigner java javac javadoc javap jcmd jconsole jdb jdeprscan jdeps jfr jhsdb jimage jinfo jlink jmap jmod jps jrunscript jshell jstack jstat jstatd keytool rmiregistry serialver jpackage"
NOMS_OPENJDK_11="jar jarsigner java javac javadoc javap jcmd jconsole jdb jdeprscan jdeps jfr jhsdb jimage jinfo jlink jmap jmod jps jrunscript jshell jstack jstat jstatd keytool rmiregistry serialver unpack200 jaotc jjs pack200 rmic rmid "

# ------------------------------------------------------------------------------
#
usage() {
    echo
    echo "Usage : $(basename $0)   \"set_jdk_17 | set_openjdk_11 | install_jdk_17\""
    echo
    echo "    . set_jdk_17     : active les alternatives jdk-17 (java Oracle 17)"
    echo "    . set_openjdk_11 : active les alternatives java-11-openjdk-amd64"
    echo "    . install_jdk_17 : installe les alternatives jdk-17"
    echo
}

# ------------------------------------------------------------------------------
#
install_jdk_17() {
    for NOM in ${NOMS_JDK_17}
    do
        echo "update-alternatives --install \"${BIN_LIEN}/${NOM}\" \"${NOM}\" \"${BIN_JDK_17}/${NOM}\" ${PRIORITE}"
        update-alternatives --install "${BIN_LIEN}/${NOM}" "${NOM}" "${BIN_JDK_17}/${NOM}" ${PRIORITE}
    done
}

# ------------------------------------------------------------------------------
#
set_jdk_17() {
    for NOM in ${NOMS_JDK_17}
    do
        echo "update-alternatives --set \"${NOM}\" \"${BIN_JDK_17}/${NOM}\""
        update-alternatives --set "${NOM}" "${BIN_JDK_17}/${NOM}"
    done
}

# ------------------------------------------------------------------------------
#
set_openjdk_11() {
    for NOM in ${NOMS_OPENJDK_11}
    do
        echo "update-alternatives --set \"${NOM}\" \"${BIN_OPENJDK_11}/${NOM}\""
        update-alternatives --set "${NOM}" "${BIN_OPENJDK_11}/${NOM}"
    done
}

# ------------------------------------------------------------------------------
# MAIN
#
if [ "$1" = "install_jdk_17" -o "$1" = "set_jdk_17" -o "$1" = "set_openjdk_11" ]
then
    echo "$1 ...."
    $1
else
    usage
fi

exit

