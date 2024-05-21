# System Zarządzania Przychodnią to aplikacja webowa umożliwiająca:
zarządzanie wizytami, lekarzami, pacjentami, płatnościami oraz receptami. 
Projekt zbudowany jest przy użyciu frameworka Flask i korzysta z bazy danych SQL Server.


# Możliwości systemu
Dodawanie wizyt: Formularz na stronie /wizyty pozwala na wprowadzenie danych dotyczących wizyt pacjentów, które są zapisywane w bazie danych.
Zarządzanie lekarzami: Na stronie /lekarze można dodawać nowe informacje o lekarzach, w tym imię, nazwisko, numer PESEL, specjalizację i kontakt.
Rejestracja pacjentów: Formularz na stronie /pacjenci umożliwia dodawanie nowych pacjentów do systemu, w tym ich dane kontaktowe i adresowe.
Rejestrowanie płatności: Strona /platnosci pozwala na wprowadzanie informacji o płatnościach za wizyty, które są następnie zapisywane w bazie danych.
Wystawianie recept: Na stronie /recepty można dodawać nowe recepty, wprowadzając dane takie jak data wystawienia oraz ID pacjenta i lekarza.


# Technologie użyte w projekcie
Flask: Framework do tworzenia aplikacji webowych w Pythonie.
SQL Server: System zarządzania relacyjną bazą danych.
HTML/CSS: Do tworzenia interfejsu użytkownika.
Struktura aplikacji
Pliki HTML: Znajdują się w folderze templates i odpowiadają za wygląd i strukturę stron internetowych.
Główna aplikacja: Plik app.py zawiera kod Pythona zarządzający logiką aplikacji oraz połączeniami z bazą danych.
