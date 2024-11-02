# module/__init__.py
"""
# Der __pycache__ Ordner verbessert die Performance, von python automatisch erzeugter Bytecode.
# bei komischen felern kann die __pycache__ bedenkenlos einfach gelöscht werden!
# __init__.py ist für ein Ordner der von python als Paketstruktur behandelt werden soll.
# z.b .modul_a der punkt ist wichtig! weil in disem ordner...


## Möglichkeiten von __status__

# Development
Das Paket befindet sich noch in der Entwicklungsphase
und kann instabil sein. Es wird möglicherweise noch aktiv verändert und getestet.

# Alpha
Eine frühe Version des Pakets, die vielleicht nicht alle geplanten Funktionen
enthält und möglicherweise noch viele Fehler aufweist.
Diese Version ist vor allem für frühe Tester gedacht.

# Beta
Eine fortgeschrittenere Testversion des Pakets, die alle oder die meisten
geplanten Funktionen enthält, aber noch nicht vollständig getestet wurde.
Diese Version ist für Tester und frühe Anwender gedacht, um Feedback zu geben.

# Release Candidate
Eine Version, die fast fertig ist und kurz vor der endgültigen
Veröffentlichung steht. Es können noch kleinere Fehler vorhanden sein,
aber diese Version ist weitgehend stabil.

# "Production" oder "Stable" oder "Safe"
Das Paket ist stabil und bereit für den Einsatz in der
Produktion. Es wurde gründlich getestet und alle geplanten Funktionen sind implementiert.

# Deprecated
Das Paket wird nicht mehr weiterentwickelt oder unterstützt und sollte
nicht mehr verwendet werden. Es wird möglicherweise in zukünftigen Versionen entfernt.
"""
# --- Metadaten für das Paket ---
__title__ = "fox_test_py_packet_1"
__description__ = "Ein Beispielpaket für Demonstrationszwecke"
__version__ = "0.0.1"
__author__ = "NIKI-FOX"
__license__ = "MIT"
__license_url__ = "https://github.com/NIKI-FOX/fox_test_py_packet_1/blob/main/LICENSE"
__url__ = "https://github.com/NIKI-FOX/fox_test_py_packet_1.git"
__dependencies__ = ["virtualenv"]
__copyright__ = "Copyright (c) 2024 NIKI FOX"
__status__ = "Development"
__maintainer__ = "NIKI-FOX"
__credits__ = ["NIKI-FOX", "LUNA Nr.7"]


#print("Das Paket 'module' wurde importiert")

# nur ausführen, wenn die __init__.py Datei direkt ausgeführt wird
if __name__ == "__main__":
    print(f"Title: {__title__}")
    print(f"Description: {__description__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__} ({__license_url__})")
    print(f"URL: {__url__}")
    print(f"Dependencies: {', '.join(__dependencies__)}")
    print(f"Copyright: {__copyright__}")
    print(f"Status: {__status__}")
    print(f"Maintainer: {__maintainer__}")
    print(f"Credits: {', '.join(__credits__)}")

# nur ausführen, wenn die __init__.py Datei nicht direkt ausgeführt wird
if __name__ != "__main__":
    from .modul_a import *
    from .modul_b import *
    
    # Option 1: Dynamisch alle nicht privaten Namen hinzufügen.
    #__all__ = [name for name in dir() if not name.startswith('_')]

    # Option 2: Manuell alle gewünschten Funktionen auflisten
    # __all__ = ['funktion_a', 'funktion_b']
