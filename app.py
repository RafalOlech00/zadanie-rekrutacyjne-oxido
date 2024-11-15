import openai
from dotenv import load_dotenv
import os
import sys

# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def validate_api_key():
    """Sprawdza, czy klucz API jest ustawiony i wyświetla odpowiedni komunikat."""
    if not openai.api_key:
        print("Błąd: Klucz API nie został ustawiony. Upewnij się, że jest on zapisany w pliku .env.")
        sys.exit(1)

def read_article(filename):
    """Funkcja odczytująca treść artykułu z pliku."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie został znaleziony.")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd podczas odczytywania pliku: {e}")
        sys.exit(1)

def process_article_with_openai(content):
    """Funkcja wysyłająca artykuł i prompt do OpenAI w celu generacji kodu HTML."""
    prompt = (
        "Przygotuj HTML artykułu poniżej, używając odpowiednich tagów HTML do strukturyzacji treści. "
        "Jeżeli w akapicie jest mowa o procesach, rzeczach lub koncepcjach, które mogą być zobrazowane i przykują uwagę czytelnika, "
        "umieść tam ilustrację. Użyj nagłówków <h1> i <h2> oraz akapitów <p> do strukturyzacji. Każdy obraz dodaj w odpowiednim kontekście, "
        "używając znacznika <figure><img src='image_placeholder.jpg' alt='Opis obrazu'><figcaption>Podpis obrazu</figcaption></figure>. "
        "Nie dodawaj CSS ani JavaScript. Zwróć tylko kod HTML, który można wstawić w sekcji <body>.\n\n"
        + content
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that formats content as structured HTML with context-aware image placement."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.5
        )
        html_content = response['choices'][0]['message']['content'].strip()

        # Usuwanie niechcianych fragmentów, takich jak "```html" i "```"
        html_content = html_content.replace("```html", "").replace("```", "").strip()

        # Walidacja odpowiedzi
        if "<body>" in html_content or "</body>" in html_content:
            print("Uwaga: Wygenerowany kod HTML zawiera niechciane znaczniki <body>. Upewnij się, że AI przestrzega instrukcji.")
            html_content = html_content.replace("<body>", "").replace("</body>", "")

        return html_content

    except openai.error.InvalidRequestError as e:
        print(f"Błąd: Nieprawidłowe żądanie do API OpenAI. Szczegóły: {e}")
        sys.exit(1)
    except openai.error.AuthenticationError:
        print("Błąd: Nieprawidłowy klucz API. Upewnij się, że klucz API jest poprawny.")
        sys.exit(1)
    except openai.error.APIConnectionError:
        print("Błąd: Problem z połączeniem do API OpenAI. Sprawdź swoje połączenie internetowe.")
        sys.exit(1)
    except openai.error.OpenAIError as e:
        print(f"Nieznany błąd po stronie OpenAI: {e}")
        sys.exit(1)

def save_html(content, filename="artykul.html"):
    """Funkcja zapisująca wygenerowany kod HTML do pliku."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Wygenerowano plik {filename}")
    except IOError as e:
        print(f"Błąd zapisu do pliku '{filename}': {e}")
        sys.exit(1)

def main():
    validate_api_key()  # Sprawdza, czy klucz API jest ustawiony

    # Odczyt artykułu z pliku
    article_content = read_article("article.txt")

    # Przetwarzanie artykułu przez OpenAI API
    html_content = process_article_with_openai(article_content)

    # Zapis wygenerowanego HTML do pliku
    save_html(html_content)

if __name__ == "__main__":
    main()
