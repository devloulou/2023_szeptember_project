"""
Git kezelés:


Git 2 flowja van:

Amikor még nem git kezelt a kódod:
1. git init parancs kiadása a megfelelő mappában -> létrejön .git mappa, minden file-t és mappát "észrevesz"
2. el kell döntened, hogy mely file-okat / mappákat NEM akarod feltölteni a git repositoryba
    - szenzitív adatok: jelszavak, user nevek, stb.
    - olyan adatok, amelyeknek nincs relevanciája a fejlesztés során: 
        - temporális mappák,
        - virtuális környezetek, 
        - IDE beállítások stb.
3. initial commit - ő a mentett állapot
    - a változásokat stage-elni kell -> ez után már commitálni tudsz -> elmented az állapotot
    - commit-olom a változást: adok egy commit üzenetet, lerögzítem az állapotot
Amikor már git kezelt:
-> létrehozol valamilyen változást a kódbázison: (új sor, új karakter, új file, új mappa)
-> ezeket a változásokat figyelni akarod: git add . 
    - azt az állapotot, amit figyelek ahhoz mérten fogom tudni a visszaállítást alkalmazni
    - vagy a flow további lépcsőjére lépni: -
"""