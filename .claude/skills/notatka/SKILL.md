---
name: notatka
description: Zamień surowe notatki z zajęć (wklejone, podyktowane lub z pliku) w uporządkowaną notatkę markdown w odpowiednim folderze tematu, uzupełnioną o wyjaśnienia i przykłady. Używaj, gdy student chce zapisać lub uporządkować notatki z wykładu/ćwiczeń.
---

# Notatka z zajęć

Argument: temat lub folder (np. `funkcje`, `04-Functions`) + surowe notatki w wiadomości albo ścieżka do pliku z nimi.

## Kroki
1. **Ustal folder** – dopasuj temat do folderu `NN-Temat`. Jeśli nie pasuje do żadnego (np. inny przedmiot), zaproponuj nowy folder i zapytaj.
2. **Docelowy plik:** `NN-Temat/notatki.md`. Jeśli już istnieje – dopisz nową sekcję z datą zajęć, nie nadpisuj.
3. **Zachowaj to, co napisał student** – porządkujesz i uzupełniasz, nie zastępujesz. Jeśli coś w notatkach jest błędne, popraw i oznacz `> ⚠️ Poprawka: ...`, żeby wiedział.
4. **Struktura sekcji:**
   ```markdown
   ## Zajęcia RRRR-MM-DD – <temat>

   ### Najważniejsze w 3 punktach
   ### Pojęcia
   - **termin (*english term*)** – definicja jednym zdaniem
   ### Przykłady
   (krótki, działający kod Pythona z komentarzami po polsku – sprawdź, że się uruchamia)
   ### Pułapki
   ### Pytania do siebie
   (2–3 pytania kontrolne; odpowiedzi w <details>)
   ```
5. Dodaj krótkie odniesienie do materiału prowadzącego (`_Temat.md`, sekcja) i do rozdziału `py4e-PL-2023.pdf`, jeśli pasuje.
6. Zapisz plik i pokaż studentowi skrót. Nie commituj bez prośby.
