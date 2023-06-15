Plugin Builder Results

Your plugin WtyczkaQGIS was created in:
    C:\Users\Poradnia dla palaczy\AppData\Roaming\QGIS\QGIS3\profiles\default\python\wtyka
Your QGIS plugin directory is located at:
    C:/Users/Poradnia dla palaczy/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins

Aby użyć naszej wtyczki musimy wykonać poniższe etapy:

- Kopiujemy cały katalog zawierający nową wtyczkę do katalogu wtyczek QGIS,

- Otwieramy program QGIS,

- W głownym panelu QGISa znajdujemy zakładkę Wtyczki -> Zarządanie wtyczkami,

- Następnie zaintaluj wtyczkę zapisaną w pliku zip,

- Aby ją uruchomić w tym samym oknie wchodzimy w zakładkę zainstalowane i obok nazwy naszej wtyczki "Wtyczka QGIS" zaznaczamy checkboxa,

- W głownym oknie w zakładce Wtyczki możemy znaleźć nasz zainstalowany i gotową do użytku aplikację

WAŻNE INFORMACJE!

- Aby poprawnie używać naszego programu, potrzebujemy poprawnie przetworzonych plików typu txt,

- Muszą ona zostać przygotowane tak jak w poniższym przykładzie (jest to spowodowane faktem, iż nasz program liczy wymagane polecenia na podstawie tabeli atrybutów w programie QGIS):
nr;y92;x92;h
1;672600;352600;198.34
2;672700;352600;197.49
3;672800;352600;199.61

- Tłumacząc podany przykład opracowany plik na którym chcemy wykorzystać naszą wtyczkę, plik ten musi zawierać kolejno w kolumnach:
nr -> numery punktów
y -> współrzędne y punktów
x -> współrzędne x punktów
h -> wysokości punktów

- Uwzględniajać powyższe elementy należy również pamiętać, że przy importowaniu pliku do QGISa należy zachować odpowiednie typy kolumn w tabeli atrybutów, czyli:
nr w tabeli ma przyjąć typ "tekstowy" (string)
y w tabeli ma przyjąć typ "integer" (64 bit)
x w tabeli ma przyjąć typ "integer" (64 bit)
h w tabeli ma przyjąć typ "decimal" (double)

- Zachowując powyższe polecenia, użycie 2 punktów umożliwi nam obliczenie wysokości natomiast wybranie 3 punktów umożliwi nam policzenie pola powierzchni pomiędzy tymi punktami (pole powierzchni trójkąta)

- Używając 0, 1 lub powyżej 3 punktów, nasz program przedstawi błąd, który będzie mówił o niepoprawnej liczbie wybranej punktów!

- W oknie wynikowym w momencie wykonania poprawnych obliczeń powinny pokazać się:
w przypadku obliczenia wysokości -> wybrane punkty oraz wysokość podana w metrach
w przypadku obliczenia powierzchni -> wybrane punkty oraz pole powierzchni podane w metrach kwadratowych


For more information, see the PyQGIS Developer Cookbook at:
http://www.qgis.org/pyqgis-cookbook/index.html

(C) 2011-2018 GeoApt LLC - geoapt.com
