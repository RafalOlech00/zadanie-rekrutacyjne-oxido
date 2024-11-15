# Zadanie Rekrutacyjne - Oxido (Junior AI Developer)

## Opis projektu
Aplikacja w Pythonie, która:
- Łączy się z API OpenAI.
- Przetwarza artykuł z pliku `article.txt` i generuje kod HTML z odpowiednimi strukturami, miejscami na obrazy oraz podpisami.
- Generuje plik `artykul.html` zawierający gotowy HTML artykułu.
- Udostępnia pliki `szablon.html` oraz `podglad.html`:
  - `szablon.html`: Pusty szablon gotowy do dynamicznego wczytywania treści za pomocą funkcji JavaScript.
  - `podglad.html`: Pełny podgląd wygenerowanego artykułu.

## Instrukcja uruchomienia
### 1. Klonowanie repozytorium:

`git clone https://github.com/twoja_nazwa_uzytkownika/zadanie-rekrutacyjne-oxido.git`

`cd zadanie-rekrutacyjne-oxido`

---

### 2. Instalacja środowiska i zależności
* Wymagany jest `Python 3.9` lub nowszy.
* Upewnij się, że masz zainstalowane `pip` oraz `virtualenv`.

Utwórz i aktywuj wirtualne środowisko, a następnie zainstaluj wymagane pakiety:

**Tworzenie wirtualnego środowiska**

`python -m venv venv`

**Aktywacja środowiska**

**- Na Linux/macOS:**
`source venv/bin/activate`

**- Na Windows:**
`venv\Scripts\activate`

**Instalacja wymaganych bibliotek**

`pip install -r requirements.txt`

---

### 3. Utworzenie pliku .env z kluczem API
W katalogu głównym projektu utwórz plik .env i umieść w nim swój klucz API od OpenAI, używając poniższego formatu:

`OPENAI_API_KEY=your_api_key`

Zamień `your_api_key` na swój faktyczny klucz API, uzyskany z OpenAI.

---

### 4. Uruchomienie aplikacji i generowanie pliku HTML
Aby wygenerować plik `artykul.html` na podstawie treści artykułu z `article.txt`, uruchom poniższą komendę:

`python app.py`

Po zakończeniu działania skryptu, w katalogu projektu pojawi się plik `artykul.html`, zawierający wygenerowaną stronę HTML.

---

### 5. Podgląd artykułu
Otwórz plik `podglad.html` w przeglądarce, aby zobaczyć pełny podgląd wygenerowanego artykułu z zaimplementowanymi stylami.

Aby przetestować plik `szablon.html`, otwórz go w przeglądarce, a następnie w konsoli (F12) wprowadź poniższy kod JavaScript, aby dynamicznie załadować treść do sekcji `<body>`:

`loadArticleContent('<h1>Testowy artykuł</h1><p>To jest dynamicznie wczytana treść do sekcji body.</p>');`

Treść powinna się dynamicznie załadować w sekcji `<body`>, umożliwiając przetestowanie szablonu.

