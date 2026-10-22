# Fundacja im. Stefana Drzewieckiego — strona

Statyczna strona-wizytówka Fundacji im. Stefana Drzewieckiego
(historia podboju głębin, przestworzy i kosmosu).

Wersja poglądowa hostowana przez GitHub Pages. Produkcyjnie strona działa
na https://fundacjadrzewiecki.pl

## Struktura
- `index.html` — cała strona (jeden plik)
- `assets/` — obrazy, logo oraz sekwencja klatek animacji nurka (`assets/dive/`)
- `dev-server.js` — prosty lokalny serwer deweloperski (Node.js)

## Podgląd lokalny
```
node dev-server.js
```

## Wersja angielska
`en/index.html` jest generowany z `index.html` skryptem `tools/build_en.py`
(pary tekst PL → EN). Po każdej zmianie w wersji polskiej: `python3 tools/build_en.py`.
