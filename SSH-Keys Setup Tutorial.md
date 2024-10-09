## SSH key Generiren und auf Remote-Server instaliren.
\
_Auf deinem pc:_
## 1. Generierung eines SSH ECDSA-Schlüssels
``ssh-keygen -t ecdsa -b 521 -C -f ~/.ssh/dein-ssh-key``

Optional: mit email:\
``ssh-keygen -t ed25519 -C "deine_email@example.com" -f ~/.ssh/dein-ssh-key``

## 2. Öffentlichen Schlüssel kopieren
``cat ~/.ssh/dein-ssh-key.pub``

## 3. * Über SSH zum Remote-Server verbinden
wen OpenSSH schon auf dem remote server instalirt ist:\
``ssh benutzername@ip-oder-host-name-vom-remote-server``

\
\
_Auf deinem Remote-Server:_
## 4. * OpenSSH Instaliren und zum system startup hinzufügen
``sudo apt-get update``\
``sudo apt-get upgrade -y``
``sudo apt-get install openssh-server``
``sudo systemctl enable ssh``
``sudo systemctl start ssh``

## 5. Verzeichnis für SSH-Schlüssel erstellen (falls nicht vorhanden)
``mkdir -p ~/.ssh``

## 6. Schlüssel in die Datei ``authorized_keys`` einfügen
Öffne die Datei ``authorized_keys`` im Verzeichnis ``~/.ssh``\
``nano ~/.ssh/authorized_keys``

## 7. Einstellen das ``authorized_keys`` als Key datei benutzt wird
``sudo nano /etc/ssh/sshd_config`` \
Folgende Zeilen überprüfen oder erstelen und ggf. anpassen: \
``AuthorizedKeysFile %h/.ssh/authorized_keys``

## 8. Berechtigungen setzen
Stelle sicher, dass die Berechtigungen korrekt gesetzt sind:\
``chmod 700 ~/.ssh``\
``chmod 600 ~/.ssh/authorized_keys``

## _9. Optional: nur über ssh key einlogen ohne password_
optional schalte den ssh root login und pasword mechanismen ab: \
``sudo nano /etc/ssh/sshd_config`` \
Finde die Zeilen: \
``#PasswordAuthentication``\
``#PermitRootLogin`` \
``#PubkeyAuthentication`` \
 und ändere sie zu: \
``PasswordAuthentication no`` \
``PermitRootLogin prohibit-password`` \
``PubkeyAuthentication yes``

## _10. Optional: Costum SSH Banner_
wen du ein costum banner sehen wilst beim verbinden über ssh: \
und dan noch ein das script vür den Hostnamen... \
``sudo nano /etc/ssh/generate_ssh_banner.sh``
```
#!/bin/bash

# Dynamischer Banner mit Hostname und IP-Adresse
echo "LUNA SSH NETWORK"
echo "Hostname: $(hostname)"
echo "Host IP: $(hostname -I | awk '{print $1}')"
```


es ist hierbei noch wichtig dass du die Variable ``Banner`` \
in ``/etc/ssh/sshd_config`` mit einem ``#`` auskommentierst!

``sudo nano /etc/ssh/sshd_config``
```
######
# Disable the static Banner
#Banner none

# ForceCommand block to run the banner script and start a Bash session
Match all
  ForceCommand /usr/local/bin/generate_ssh_banner.sh && /bin/bash --login
######
```
dan noch eben den sshd dinst neustarten: \
``sudo systemctl restart sshd`` \
und wenn du dich jetzt neu verbindest über SSH \
solltest du das Banner auch schon sehen können.

## 11. SSH-Server Dienst neuladen und neustarten
``sudo systemctl reload ssh`` \
``sudo systemctl restart ssh`` \
``sudo systemctl reload sshd`` \
``sudo systemctl restart sshd``
## 12. Teste Über SSH zum Remote-Server die verbinden
``ssh benutzername@ip-oder-host-name-vom-remote-server``
