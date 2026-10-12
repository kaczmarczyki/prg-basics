---
name: sprawdz
description: Przejrzyj kod napisany przez studenta i daj mu feedback jak korepetytor – co działa, co poprawić i dlaczego – bez przepisywania wszystkiego za niego. Używaj, gdy student prosi o sprawdzenie, ocenę lub "czy to jest dobrze".
---

# Sprawdź mój kod

Argument: plik (lub folder) studenta. Bez argumentu: pliki zmienione ostatnio (`git status`, `git log --author=kaczmarczyki -3 --stat`).

## Kroki
1. **Przeczytaj kod i polecenie zadania.** Jeśli plik leży w folderze tematu, znajdź odpowiednie zadanie w `_Temat.md`, żeby ocenić, czy kod robi to, o co prosił prowadzący.
2. **Uruchom go** z kilkoma danymi wejściowymi, w tym nietypowymi (0, liczba ujemna, tekst zamiast liczby, pusty plik). Pokaż wyniki.
3. **Napisz feedback w tej kolejności:**
   - ✅ **Co jest dobrze** – konkretnie (nie „fajny kod”, tylko „dobrze, że zaokrąglasz wynik `round()`”).
   - 🐛 **Błędy** – rzeczy, które dają zły wynik albo wywalają program. Pokaż dane, przy których się psuje.
   - 🔧 **Do poprawy** – czytelność, nazwy zmiennych, powtórzenia, zbędne elementy (np. `;` na końcu linii w Pythonie). Maks. 3–4 punkty, najważniejsze pierwsze.
   - 💡 **Następny poziom** – jedna rzecz, która podniesie kod wyżej (np. `elif` zamiast kilku `if`, funkcja, f-string), z krótkim wyjaśnieniem *dlaczego*.
4. **Nie przepisuj całego pliku.** Pokazuj małe fragmenty „przed → po”. Zapytaj, czy chce sam wprowadzić poprawki, czy żebyś pomógł.
5. Nie edytuj pliku, dopóki student wyraźnie o to nie poprosi.

## Ton
Zachęcający, ale szczery. To początkujący – błędy są normalne, ale mają być nazwane wprost.
