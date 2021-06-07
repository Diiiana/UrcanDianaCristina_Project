# UrcanDianaCristina_Project
Weather prediction using Django.

Urcan Diana-Cristina, grupa 30236.

Pentru a adauga in baza de date, am folosit fisierul response_data.py, unde am facut request-urile si am transmis datele spre view.
La partea de predictii, am folosit fisierul de predictions - pentru unele, am realizat eroarea medie, respectiv, eroarea pentru fiecare pas sau graficul care sa evidentieze diferenta dintre valorile actuale si cele prezise. Am realizat predictii pentru parametrii ceruti (conditii meteo, directie si viteza vant, directie si inaltime
valuri, vizibilitate).
Am extras date pentru trei puncte diferite din zona NY si am facut partea de predictii temperatura
pentru toate cele trei puncte. Datele sunt in intervalul 05.06.2020-03.09.2020; se puteau prelua mai multe date, dar era dificil de antrenat modelul, avand in vedere ca nu s-au salvat valorile antrenate.
Executia este lansata cu python manage.py runserver.

Fisierul Results continte rezultatele obtinute.
