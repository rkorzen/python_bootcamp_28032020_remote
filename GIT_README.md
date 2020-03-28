# Podstawy korzystania z GIT

## konfiguracja

	git config --global user.name=<nazwa>
	git config --global user.email=

## tworzenie noweg repozytorium

W katalogu projektu piszemy:

	git init

## branch 
Gałąź

master
devel

	git branch  # sprawdza jaki to branch
	git checkout -b nazwa_brancha

## commit 

punkt przywracania

By utworzyć commit, musimy
0. sprawdzenie obecnego stanu

	git status

1. dodać pliki, które chcemy mieć w commicie

	git add <sciezka do pliku>

można dodać wszystkie pliki:	
	git add . 				

a na koniec commit

	git commit 
	
	git commit -m "Prosta zmiana"