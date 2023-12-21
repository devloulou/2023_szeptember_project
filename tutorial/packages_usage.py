"""
A packageknek általában van verziója
nem mindegy, hogy melyik verziót használod

2 megközelítése van a package használatnak:
    - mindig a latest verziót használom
        - pro:
            - mindig a legfrisebb verzió áll rendelkezésre -> általában a legjobb verzió
        - con
            - production-be minden package változásnál veszélyezteted az ütemezett működést azzal
                hogy előfordulhat, hogy a fejlesztés más verzión történt, mint az élesítés
    
    - fix verziókkal dolgozom
        - pro:
            - tudsz tervezni a releasekkel -> ha valamelyik modult le kell cserélned újra
              akkor meg tudod tervezni ezt a munkafolyamatot
        - con:
            - foglalkoznod kell a package managelléssel

Virtuális környezet létrehozása requirements.txt-vel:
pip install -r requirements.txt

"""