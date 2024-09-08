## WireGuard Public und private Keys erstellen

Private key erstellen:\
``wg genkey > privkey``

Private Key anzeigen:\
``cat .\privkey``

Public Key aus dem Private key erstellen:\
``cat privkey | wg pubkey > pubkey``

Public Key anzeigen:\
``cat .\pubkey``
