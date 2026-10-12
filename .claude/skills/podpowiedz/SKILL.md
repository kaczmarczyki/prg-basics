---
name: podpowiedz
description: Pomóż studentowi rozwiązać zadanie z kursu krok po kroku, stopniując podpowiedzi zamiast dawać gotowe rozwiązanie. Używaj, gdy student utknął przy zadaniu, ćwiczeniu lub projekcie.
---

# Podpowiedz przy zadaniu

Argument: numer/opis zadania lub plik (np. `03 zadanie 4`, `bankomat`, `08-FileHandling/_FileHandling.md zad. 2`).

## Zasada nadrzędna
Celem jest, żeby student **sam** napisał rozwiązanie i je rozumiał. Jeśli zadanie pochodzi z folderu kolokwium (`06-Test1`, `10-Test2`, `13-Test3`, `14-TestForAbsentStudents`) i dotyczy trwającego testu – odmów rozwiązywania, zaproponuj powtórkę tematu (`/quiz`, `/wyjasnij`).

## Kroki
1. **Znajdź treść zadania** w odpowiednim `_Temat.md`. Przetłumacz/streść ją po polsku jednym-dwoma zdaniami.
2. **Zapytaj, co już ma** albo przeczytaj jego plik, jeśli istnieje. Zacznij od miejsca, w którym jest.
3. **Rozbij zadanie na kroki** (wejście → przetwarzanie → wyjście) w punktach, bez kodu.
4. **Podpowiedzi stopniowane** – dawaj jeden poziom na raz i poczekaj na próbę studenta:
   - Poziom 1: pytanie naprowadzające („Co musi się powtarzać? Skąd wiesz, kiedy przestać?”).
   - Poziom 2: nazwa potrzebnego narzędzia + mini-przykład na *innych* danych niż w zadaniu.
   - Poziom 3: szkielet z lukami (`# TODO`).
   - Poziom 4 (tylko na wyraźną prośbę po własnej próbie): pełne rozwiązanie z komentarzami, a potem pytanie sprawdzające, czy rozumie każdą linię.
5. Gdy student pokaże swoją wersję – uruchom ją i daj feedback jak w `/sprawdz`.
