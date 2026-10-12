---
name: wyjasnij
description: Wytłumacz od podstaw plik, fragment kodu albo pojęcie programistyczne studentowi-początkującemu. Używaj, gdy student pyta "co to jest", "jak to działa", "nie rozumiem" albo podaje plik do omówienia.
---

# Wyjaśnij

Argument: ścieżka do pliku, fragment kodu albo pojęcie (np. `03-ControlStructures/atm.py`, `pętla while`, `self`).

## Kroki
1. **Ustal, co to jest.** Jeśli to plik – przeczytaj go. Jeśli to `_Temat.md` prowadzącego, sprawdź też sąsiednie pliki `.py`/dane, do których się odnosi. Jeśli to pojęcie – znajdź, w którym folderze kursu się pojawia (`grep -ril`), żeby oprzeć się na materiale z zajęć.
2. **Jedno zdanie „o co chodzi”** – zanim wejdziesz w szczegóły.
3. **Analogia z życia** (np. zmienna = podpisane pudełko, funkcja = przepis kulinarny, pętla = „powtarzaj, dopóki…”).
4. **Przejście przez kod** – dla pliku: kawałek po kawałku (po kilka linii), z cytatem kodu i wyjaśnieniem. Nie omawiaj każdej linii osobno, jeśli są oczywiste – grupuj.
5. **Pokaż działanie** – uruchom kod lub mały przykład (`python3 -c "..."` albo plik w scratchpadzie). Przy `input()` podawaj dane przez `printf "...\n" | python3 plik.py`. Pokaż wynik.
6. **Typowe pułapki** – 1–3 błędy, które początkujący robią przy tym temacie.
7. **💡 Warto wiedzieć** – coś ponad materiał: dobra praktyka, jak to wygląda w realnych projektach, powiązanie z późniejszym tematem kursu.
8. **Sprawdź się** – 1–2 krótkie pytania lub mini-zadanie. Nie podawaj od razu odpowiedzi.

## Styl
- Po polsku, termin angielski w nawiasie przy pierwszym użyciu.
- Zero żargonu bez wyjaśnienia. Jeśli musisz użyć nowego pojęcia, objaśnij je w jednym zdaniu.
- Raczej krócej niż dłużej – lepiej zaproponować „chcesz, żebym rozwinął X?”.
- Odsyłaj do książki `01-CourseIntroduction/py4e-PL-2023.pdf`, gdy jest tam pasujący rozdział.
