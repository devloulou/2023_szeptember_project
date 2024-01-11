"""
Docker

Docker: konténerizációs technológia

Docker-t a következőkre használjuk:
 - applikációk és szoftverek fejlesztésére: weboldal a dockerben fog futni
 - fejlesztői környezet kialakítására
 - microservice architektúra kialakítására
 
Mire nem jó: 
  - operációs rendszert
  - production adatbázist ne futtasatok Dockerben

Elméletileg a Docker platformfüggetlen - "módosítás nélkül" - (kénytelen leszel, de miniálisan kell módosítani)
tudod a konténereket futtatni Windowson, Linuxon, Macen

Docker flow:

 - Saját image készítése és használata
    1. létrehozol egy ún. Dockerfile -t (egyfajra leíró, paraméterfile)
    2. CLI-al kiadod a parancsot, hogy a Dockerfile buildelődjön image-é: így hozod létre
        buildeltük az image-et
    3. CLI-al kiadom a parancsot, hogy az image fusson -> container
    4. különböző dolgokat lehet a futó containerrel csinálni:
        - lehet "elemezni" -> logokat lehet nézni
                           -> meg lehet vizsgálni a stuktúráját
        - le lehet állítani a containert
        - bizonyos containerekre fel lehet lépni -> hozzá tudok csatlakozni a container belsejébe

 - már létrehozott image használata
    2. CLI-al kiadod a parancsot, hogy a registryből vegyen ki egy / több imaget
    3. CLI-al kiadom a parancsot, hogy az image fusson -> container
    4. különböző dolgokat lehet a futó containerrel csinálni:
        - lehet "elemezni" -> logokat lehet nézni
                           -> meg lehet vizsgálni a stuktúráját
        - le lehet állítani a containert
        - bizonyos containerekre fel lehet lépni -> hozzá tudok csatlakozni a container belsejébe


"""