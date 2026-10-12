---
name: nowe-materialy
description: Pobierz nowe materiały od prowadzącego z oryginalnego repozytorium kursu (stalj/prg-basics) i omów, co się zmieniło. Używaj, gdy student mówi, że prowadzący coś dodał, albo pyta, co nowego na zajęciach.
---

# Nowe materiały od prowadzącego

Oryginalne repo kursu: `https://github.com/stalj/prg-basics`, gałąź `master`.

## Kroki (każdą komendę git wyjaśnij studentowi jednym zdaniem)
1. Sprawdź, czy jest remote `upstream` (`git remote -v`). Jeśli nie – dodaj: `git remote add upstream https://github.com/stalj/prg-basics.git`.
2. `git status` – jeśli są niezacommitowane zmiany studenta, poinformuj i zaproponuj commit przed połączeniem.
3. `git fetch upstream`, potem pokaż różnice: `git log --oneline main..upstream/master` i `git diff --stat main...upstream/master`.
4. Jeśli są nowości – **zapytaj o zgodę** i dopiero wtedy `git merge upstream/master`. Konflikty rozwiąż razem ze studentem, tłumacząc, co się dzieje.
5. **Omów nowe materiały:** dla każdego nowego/zmienionego `_Temat.md` – streszczenie po polsku (o czym, jakie zadania, co jest nowym pojęciem). Zaproponuj `/wyjasnij` dla najtrudniejszej części.
6. Jeśli zmieniła się struktura folderów – zaktualizuj tabelę w `CLAUDE.md`.
7. Pushowanie do `origin` tylko na prośbę.
