#!/bin/bash

# Przechodzenie przez każdy katalog
for dir in */; do
    # Sprawdzanie czy katalog zawiera folder o nazwie "migrations"
    if [ -d "${dir}migrations" ]; then
        echo "Czyszczenie ${dir}migrations..."

        # Usuwanie wszystkich plików i katalogów wewnątrz "migrations"
        find "${dir}migrations" -mindepth 1 -maxdepth 1 -exec rm -rf {} +

        # Tworzenie pustego pliku __init__.py, jeśli nie istnieje
        touch "${dir}migrations/__init__.py"

        echo "Zakończono czyszczenie ${dir}migrations."
    fi
done

echo "Zakończono czyszczenie migrations w każdym katalogu."

