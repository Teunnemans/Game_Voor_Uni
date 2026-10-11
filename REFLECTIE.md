# Reflectie op mijn leerdoelen

# **Voorwoord:** <br>
Welkom bij mijn korte reflectiewerk op mijn gestelde leerdoelen van dit project. Ik heb veel plezier gehad om dit project te voltooien.
Het heeft ertoe geleid dat ik vele avonden bezig ben geweest en veel geleerd heb over wat je allemaal moet doen voor het maken van een spel.
Ik ben dankbaar dat ik de kans heb gekregen deze vervangende opdracht te mogen doen. Ik hoop dat ik deze met dit spel tevreden ter vervulling heb gemaakt. :)
~Teun Weijdener

## Leerdoel 1: "Ik leer hoe ik botsingsdetectie (collision detection) implementeer in een 2D-game" 

- **Heb ik dit leerdoel bereikt?** <i>gedeeltelijk</i> <br>
    Ik geloof dat ik een goede stap gezet heb naar dit leerdoel. Mijn spel heeft een volledig werkende en redelijk efficiënte botsingsdetectie.
    Het fundament daarvan is echter gebouwd op de pygame.rect class. Een class die al een hoop van het voorwerk doet. Ik heb wél mijn eigen collision-handling
    geïmplementeerd. Iets waar ik erg trots op ben. Het programma is nu schaalbaar tot circa 5000 entities. Dit werkt voor een klein spel, maar is al gauw te kort.
- **Waaruit blijkt dat?** <br>
    Ik verwijs u graag naar de entity-class in mijn code. Alle beweeglijke objecten in mijn spel hebben deze in hun inheritance-structuur.
    Dit maakt dat het samenwerken van de game-structuur eenvoudig op te bouwen was. Elke entity met een rect-object heeft een collision-method.
    Hierdoor is de onderliggende logica echt mega makkelijk abstract te maken. 
  - **Wat ging goed en wat vond je lastig?** <br>
    Zoals eerder genoemd is collision-detection(in dit geval 2D, vierkante-collision) een vrij eenvoudig systeem. Het schaalbaar maken van een implementatie hiervan is wel een uitdaging.
    Gezien de duur van de opdracht en de schaal van het spel is er geen ruimte en behoefte om een complex collision-detection-systeem te implementeren. 
    Ik zou dus niet zo goed kunnen zeggen of ik het niet misschien te makkelijk gemaakt heb. 
- **Wat zou je een volgende keer anders doen?** <br>
    Voor dit spel: Niets. Ik geloof dat de implementatie goed recht doet aan de behoeften van het spel.

## Leerdoel 2: "Ik leer hoe ik willekeur kan gebruiken in een procedurally-generated-game."

- **Heb ik dit leerdoel bereikt?** <i>ja</i> 
- **Waaruit blijkt dat?** <br>
  Ik ben erg trots op hoe ik dit leerdoel heb bereikt. Het spel gebruikt voor verschillende plekken willekeur. O.A. voor
het maken van de achtergrond(Te vinden in Functions.py), hierbij genereert het programma willekeurige een achtergrond met sterren
en planeten die vervolgens in de game-loop worden bewogen. Dit systeem is efficient, soepel en het resultaat is een leuke toevoeging voor de speler.
Ook het creëren van de enemies gebeurt met een willekeurige generator.(Spawner.py)
- **Wat ging goed en wat vond je lastig?** <br>
Het zijn best wel complexe systemen die al snel een beetje doen duizelen als je ze aan het programmeren bent. Het is een flinke oefening 
geweest om dit binnen de tijd van de opdracht te realiseren. Ik heb hierdoor grappig genoeg veel geleerd over het onderhouden van complexe game-strucuur. 
Dit is terug te vinden in mijn commits, die langzaam de structuur van het project laat verzinken tot wat het nu is geworden.
- **Wat zou je een volgende keer anders doen?** <br>
Ik zou het leuk vinden om dit systeem te gebruiken in mijn volgende project. Daar is veel ook omheen gebouwd. Modulaire classes die ook later gebruikt kunnen worden.
Toch denk ik dat het beter geweest was als ik het project minder uitgebreid had gemaakt. Nu ben ik veel tijd kwijt die ik ook op andere plekken binnen mijn studie hard nodig heb. Desondanks ben ik erg tevreden.

## Leerdoel 3: "Ik leer hoe je een startmenu maakt voor een kleinschalig spel."
- **Heb ik dit leerdoel bereikt?** <i>ja</i> <br>
- **Waaruit blijkt dat?** <br>
Dit heb ik volgens mij meer dan bereikt. Ik ben een stap verder gegaan en ik heb een modulair UI-Systeem geprogrammeerd. Ik heb hierbij inspiratie genomen
van programa's als Figma en Unity, waarbij een UI is opgebouwd uit Elementen en Groepen(zie ook mijn implementaties in de desbetreffende classes) die zich in een root-structuur
bevinden. Dit maakte het heel erg makkelijk om een startmenu te maken. Ik heb deze hierom ook aangedikt met een high-score systeem, dat op het startscherm
je 10 beste pogingen weergeeft. Deze scores slaat hij op in een JSON bestand.
- **Wat ging goed en wat vond je lastig?** <br>
Het Ui-systeem kostte mij veel denktijd, nog nooit eerder had ik gewerkt met een dergelijk root-systeem. Ook zat ik lang vast bij het definiëren van elements.
Het was een hele leuke uitdaging, maar ik had mij niet eerder zo diep afgevraagd wat een knop is, en wat deze moet doen(zie UI-types.py). Ik denk dat wat hier nu staat mooi werkt en schaalbaar is.
- **Wat zou je een volgende keer anders doen?** <br>
Ik geloof dat ik ook hier mijn complexiteit had moeten terugschalen. Het systeem is veel te uitgebreid voor mijn spel. Ook ben ik niet helemaal tevreden met mijn
implementatie van TextElement(), dit is een class die beloofd makkelijk tekst op het scherm te krijgen maar ik heb mijzelf vaak gefrustreerd met hoe ik die gemaakt heb.
Het is het niet waard geweest het hele ui-systeem om te schrijven om oa Bold/Italic font rendering te krijgen, maar ik had dat wel leuk gevonden.

## Algemene reflectie

Als ik heel eerlijk ben, is het een vreselijk uit de kluiten gewassen project geworden. Onder het mom van zelf-uitdaging
is er geen deelvak van de studie geweest waar ik de afgelopen weken zo druk mee ben geweest. Het idee dat ik helemaal mijn eigen
game mocht programmeren en de kansen die dat bood, is een supermooie, maar ook hele gevaarlijke kans geweest. Ik begon met het maken
van een basic-game-structuur waar al gauw veel facetten aan toegevoegd werden en ik heb mijzelf echt moeten bedwingen om ook niet features
als multiplayer en animaties toe te voegen. Puur omdat ik dit zo'n leuke opdracht vond. Ik heb zo enorm veel geleerd van dit project 
en kan met trots zeggen dat ik mijn eigen mini-game geschreven heb :) Ik nodig u uit om op uw gemak door de code heen te lopen. Ik 
hoop dat er voldoende gedocumenteerd is. Ook heb ik een .exe build toegevoegd, die het delen van het spel gemakkelijker zou moeten maken!

Er is bij dit project geen AI gebruikt voor het ontwerp van het spel, de codestructuur, de muziek, de sprites/andere Art. 
Features en code zijn allemaal met de menselijke hand geschreven. Ik heb een bloedhekel aan AI en geloof in authenticiteit en de menselijke geest.
Dit project is mij iets waard omdat ik het gemaakt heb. Geen AI. 

Waar wel AI gebruikt is is bij triviale debugging. Dit in de vorm van de autocomplete van Pycharm en het opsturen van probleembeschrijving naar ChatGPT.

Ik hoop u hiermee voldoende geïnformeerd te hebben.

In licht en vooruitgang,

Teun Weijdener