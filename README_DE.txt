Programm starten:

1.1 Bei Windows im CMD ipconfig eingeben und die ipv4 in der "Server.py" bei host eintragen.
1.2 Bei Linux im Terminal ifconfig eingeben und die ipv4 in der "Server.py" bei host eintragen.
2. Die "Server.py" starten (Auf dem Gerät wo ACC läuft)
3. Die Datei "Dashboard_UI.py" starten und der Anweisung im Programm folgen (Auf dem anzeige Gerät)
4. Die Hotkeys(siehe weiter unten) in ACC setzen, um das Programm zum Laufen zu bekommen

Hotkeys:

ABS+ : G
ABS- : R
TC1+ : W
TC1- : K
TC2+ : J
TC2- : D
ING  : S
LIGHT: Q

Ordnerverzeichnis:

DE: In diesem Verzeichnis liegt die Anwendung in deutscher ausführung
EN: In diesem Verzeichnis liegt die Anwendung in englischer ausführung
Development: In diesem Verzeichnis liegt die Entwicklungsvarriante der Anwendung, wo noch mehr Debugging
             Zeilen vorhanden sind

Dependencis:

Server:
    Python 11.x oder neuer
    pyautogui
    socket

UI:
    Python 11.x oder neuer
    tkinter
    socket

Anmerkung:
Das Programm befindet sich noch in der Entwicklung und kann noch
fehler beinhalten, diese gerne bei Github in den Issues melden