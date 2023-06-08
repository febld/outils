
1) Installer JDK


2) Création utilisateur tomcat

    ```
    sudo groupadd tomcat
    sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
    ```

3) Installer  Apache Tomcat

    ```
    #wget https://downloads.apache.org/tomcat/tomcat-10/v10.0.18/bin/apache-tomcat-10.0.18.tar.gz
    #wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.27/bin/apache-tomcat-10.0.27.tar.gz 
    wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.9/bin/apache-tomcat-10.1.9.tar.gz
    ```

    ```
    mkdir /opt/tomcat
    sudo tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1

    sudo chown -R tomcat:tomcat /opt/tomcat/ 
    sudo chmod -R u+x /opt/tomcat/bin/*.sh
    ```

4) Configurer les roles/utilisateurs tomcat

    ```
    sudo vi /opt/tomcat/conf/tomcat-users.xml
    ```

5) Configurer l'accès à distance à l'interface web de tomcat

    Commenter la section concernant la restriction d'adresse IP
    - dans le fichier context.xml du manager
    - dans le fichier context.xml du host-manager

    ```
    sudo vi /opt/tomcat/webapps/manager/META-INF/context.xml
    sudo vi /opt/tomcat/webapps/host-manager/META-INF/context.xml
    ```

6) Créer un fichier systemd pour Apache Tomcat

    ```
    vi /etc/systemd/system/tomcat.service
    ```

    ```
    [Unit]
    Description=Tomcat webs servlet container
    After=network.target

    [Service]
    Type=forking
    User=tomcat
    Group=tomcat
    RestartSec=10
    Restart=always
    Environment="JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64"
    Environment="JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom"
    Environment="CATALINA_BASE=/opt/tomcat"
    Environment="CATALINA_HOME=/opt/tomcat"
    Environment="CATALINA_PID=/opt/tomcat/temp/tomcat.pid"
    Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"
    ExecStart=/opt/tomcat/bin/startup.sh
    ExecStop=/opt/tomcat/bin/shutdown.sh

    [Install]
    WantedBy=multi-user.target
    ```
    
    Relancer le daemon "systemctl" pour charger le nouveau fichier et démarrer le service tomcat

    ```
    sudo systemctl daemon-reload
    sudo systemctl start tomcat.service
    ```

    Pour activer le démarrage de tomcat au boot :

    ```
    sudo systemctl enable tomcat.service
    ```
