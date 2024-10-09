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
oder
```
#!/bin/bash

# Informationen für den Banner sammeln
remote_host=$(echo $SSH_CLIENT | awk '{print $1}')      # IP des Clients (Verbindung von)
remote_port=$(echo $SSH_CLIENT | awk '{print $3}')      # Port des Clients
local_ip=$(hostname -I | awk '{print $1}')               # IP-Adresse des Servers

# Funktion zur Ermittlung des Hostnamens mit dig
get_hostname() { hostname=$(dig -x "$1" +short); echo "${hostname%.}"; }

# Hostname ermitteln
local_hostname=$(get_hostname "$local_ip")
remote_hostname=$(get_hostname "$remote_host")

# Wenn kein Hostname, verwende die IP
[[ -z "$remote_hostname" ]] && remote_hostname=$remote_host

# SSH-Port des Servers
local_port=$(ss -tnlp | grep sshd | awk '{print $4}' | cut -d':' -f2 | head -n1)

print_aligned() { printf "%-25s%-10s%s\n" "$1" ">" "$2"; }


# ASCII-Logo als Array
ascii_logo=(
"          ."
"         / \\"
"        /   \\"
"       /     \\"
"      /_______\\"
"________     ________"
"\\      / / \\ \\      /"
" \\    / /   \\ \\    /"
"  \\  / /     \\ \\  /"
"   \\/ /_______\\ \\/"
"       _______"
"       \\     /"
"        \\   /"
"         \\ /"
"          v"
)


banner_title="LUNA SSH NETWORK $(date +"%d.%m.%Y %H:%M:%S")"
banner_line=$(printf '=%.0s' {1..60})

# Funktion zur Ausgabe des Banners mit festem Abstand von 100 Zeichen
print_with_logo() {
    # Ausgabe des Banners links
    printf "%-65s%s\n" "$1" "${ascii_logo[$2]}"
}

# Banner anzeigen
print_with_logo "$banner_line" 0
print_with_logo "$banner_title" 1
print_with_logo "$banner_line" 2
print_with_logo "$(print_aligned "Client" "Server")" 3
print_with_logo "$banner_line" 4
print_with_logo "$(print_aligned "$remote_hostname" "$local_hostname")" 5
print_with_logo "$(print_aligned "IP: $remote_host:$remote_port" "IP: $local_ip:$local_port")" 6
print_with_logo "$banner_line" 7
print_with_logo "System Uptime: $(awk '{print int($1/86400)":"int(($1%86400)/3600)":"int(($1%3600)/60)":"$1%60" dhms"}' /proc/uptime)" 8

# Ausgabe des ASCII-Logos in den folgenden Zeilen ohne Bannerinhalt
for i in {9..14}; do
    printf "%65s%s\n" "" "${ascii_logo[$i]}"
done
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
  ForceCommand /etc/ssh/generate_ssh_banner.sh && /bin/bash --login
######
```
jetzt musst du das Skript noch ausführbar machen \
``sudo chmod +x /etc/ssh/generate_ssh_banner.sh``

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
