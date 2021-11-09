def verhaal():

    #Het begin
    print("Een hele goede dag, ik ben je narrator, ik vertel aan jou wat er in het verhaal gebeurt. Je kan zelf keuzes maken en de keuzes die je maakt veranderd het einde, dus probeer een beetje slimme keuzes te maken! Maar oke tijd voor een kleine backstory en de character die jij bestuurd voor te stellen!")
    print("")
    print("Je naam is Maksim Belov, je bent een 57 jarige Russische man die vroeger voor de maffia werkte. Nadat de maffia waar je eerst voor werkte veel onschuldige mensen had vermoord had je samen gewerkt met de politie om hun op te sluiten, dit was gelukt en je bent nu al 17 jaar met pension en je hebt een gelukkige leven met een vrouw, 3 kinderen en 4 kleinkinderen.")
    print("")
    print("Wat Maksim niet wist is dat 2 maanden geleden de meeste maffia members en je oude baas zijn ontsnapt van de gevangenis door members die nooit waren opgepakt.")
    print("")
    print("Je zit in een levensbedreigende situatie en je door middel van jou keuzes kan je Maksim helpen veilig te vluchten. Elke keuze veranderd het einde, de juiste keuze maken kan het verschil betekenen tussen levens of dood, hoe je ontkomt, hoeveel gewonden er komen en of je je familie nog ziet. Kan jij de juiste keuzes maken..?")
    print("")
    keuze0 = input("Ja dat klinkt wel leuk he? Typ ja of nee: ")
    if keuze0 == "ja":
        print("")
        print("Dat dacht ik al ja!")
    elif keuze0 == "nee":
        print("")
        print("klootzak")
    elif keuze0 == "ja of nee":
        print("")
        print("Oh... Jij bent zeker de grappigste thuis...")
    else:
        print("Okay?")

    #Hoofdstuk 1
    print("")
    print("Hoofdstuk 1: Voor het vertrek")
    print("")
    print("")
    print("Je zit rustig met de 2 jongste kleinkinderen TV te kijken tot Maksim plotseling mensen buiten zijn deur zacht Russische hoort praten, je voelde dat er iets mis was dus je brengt je kleinkinderen naar de schuilkelder waar een vlucht tunnel zit. Er word nu met geweld op de deur geklopt en de Russen schreeuwen 'Maksim, we weten dat jij daar bent! Doe open nu, vuile verrader!' Wat doe je nu?")
    print("")
    #Keuze 1 Begin
    keuze1 = input("A: Ga mee de schuilkelder in met je kleinkinderen. B: Doe de deur open. C: probeer met hun te praten. Jouw keuze: ")
    if keuze1 == "A":
        print("")
        kelder()
    elif keuze1 == "B":
        print("")
        print("Je doet de deur open en je wordt meteen aangevallen door 3 grote mannen, je overleefd het niet...")
        print("")
        print("")
        print(" Je wordt gezocht door de maffia die JIJ hebt verraden en JIJ bent de reden waarom ze in de gevangenis zaten, om te overleven moet je slimme keuzes maken en er alles aan doen om hun te vermijden")
        print("")
        restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
        if restart == "ja":
            verhaal()
        else:
            exit()
    elif keuze1 == "C":
        print("")
        print("Je gaat naast de deur staan en je vraagt 'Wat moeten jullie?'. 1 van de mannen zegt 'Jij weet precies wat wij willen verrader, jou hoofd!'")
        print("")
        keuze11 = input("A: Ren naar de kast waar je geweer is. B: Probeer verder te praten. Jouw keuze: ")
        if keuze11 == "A":
            print("")
            print("Net op het moment dat je wilt gaan rennen wordt de deur open getrapt en 3 grote sterke mannen komen naar binnen")
            print("")
            keuze12 = input("A: Probeer nog steeds naar de kast te rennen. B: Probeer te vechten. Jouw keuze: ")
            if keuze12 == "A":
                print("")
                print("Je rent naar de kast en het lukt je op je geweer te pakken zonder geraakt/gepakt te worden, jullie schieten allemaal op elkaar maar omdat jij al bijna 40 jaar ervaring hebt met geweren win jij het gevecht. Het grootste probeem is nu dat heel de buurt de schoten hoorde, binnen 10 minuten zal het of vol staan met de politie of met de maffia, of misschien wel het ergste, beide...")
                #BEGIN KOPIEREN HIER
                print("")
                keuze14 = input("A: Ren weg. B: Ren naar je kleinkinderen. Jouw keuze: ")
                if keuze14 == "A":
                    print("")
                    print("Terwijl je wegrent hoor je sirenes en zie je de politie, je ziet 5 agenten het huis binnen gaan en 4 gaan meteen weer naar buiten om rond te kijken. 1 van agenten ziet jou en schreeuwt dat je moet stoppen en je overgeven, alles wat hun zien is 3 lijken en een renende man met een geweer, op geen een manier zou dit goed voor je aflopen...")
                    print("")
                    keuze15 = input("A: Blijf rennen. B: Geef je over. Jouw keuze: ")
                    if keuze15 == "A":
                        print("")
                        print("Je blijft rennen en rennen tot je uiteindelijk langs een gelanden vliegtuig komt, je ziet een man van het midden-oosten in de vliegtuig deur staan. Je ziet dat de man verbaasd naar je kijkt dus je geeft hem een knipoog terwijl je voorbij de vliegtuig rent.")
                        print("")
                        print("Nadat je voor bijna een half uur hebt gerend durf je pas achter je te kijken, je hebt de politie afgeshud.")
                        print("")
                        keuze16 = input("A: Ga naar het vliegveld. B: Kijk of er landen zijn waar je kan wonen. Jouw keuze: ")
                        if keuze16 == "A":
                            vliegtuig()
                        elif keuze16 == "B":
                            print("")
                            print("Je kijkt of er landen zijn en je komt op Nederland, je leest dat er veel andere vluchtelingen zijn van allemaal verschillende landen die er zijn voor allemaal verschillende redenen. De reis zal niet makkelijk zijn aangezien je officeel nu een voortvluchtige bent, maar als je er eenmaal bent wordt alles beter")
                            print("")
                            print("Er zijn een paar manieren om te reizen, de vraag is alleen welke het slimst is")
                            print("")
                            keuze17 = input("A: Ga lopend. B: Probeer vervoer te regelen. Jouw keuze: ")
                            if keuze17 == "A":
                                print("")
                                print("Je probeert naar Nederland te lopen, niet wetend hoe zwaar de reis was. Na 2 weken lopen en bijna niet eten kan je gewoon niet meer. Je besluit om eventjes te gaan liggen, je ogen worden steeds zwaarder en zwaarder en je doet je ogen dicht. Je zakt steeds meer en meer weg, tot je uiteindelijk helemaal weg bent...")
                                print("")
                                print("")
                                print("Misschien kan je een beter einde krijgen?")
                                print("")
                                restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen: ")
                                if restart == "ja":
                                    verhaal()
                                else:
                                    exit()
                            elif keuze17 == "B":
                                print("")
                                print("Je gaat naar Nederland door vervoer te regelen, Auto na auto, bus na bus. Na ongeveer 3 dagen lang voertuigen switchen ben je er eindelijk, de Nederlandse grens. 1 Van de agenten daar houd je aan en je legt heel je verhaal uit, de man belt iemand op en hij zegt dat je mee moet komen naar het bureau, hij zegt dat ze veel vragen hebben maar dat je je niet zorgen moet maken want ze gaan kijken of ze iets kunnen regelen")
                    elif keuze15 == "B":
                        print("")
                        print("Je geeft je over en de politie neemt je mee naar het bureau, ze zien dat je 3 mensen hebt vermoord, en geweer op zak had en dat je vroeger voor de maffia werkte. Je wordt bestraft met levenslang in de gevangenis... Je bent nu teminsten veilig van de maffia en je kan af en toe met je familie praten... Misschien is dit wel het beste...")
                        print("")
                        print("")
                        print("Misschien kan je een beter einde krijgen als je het opnieuw probeert?")
                        print("")
                        restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                elif keuze14 == "B":
                    print("")
                    print("Je gaat me de schuilkelder in en je gaat samen met je kleinkinderen via de geheime vlucht tunnel naar buiten, terwijl jullie wegrennen pak je je mobiel en stuur je '678' naar je vrouw. 678 betekende dat het niet meer veilig was en dat zijn vrouw de kinderen/kleinkinderen moest halen en vluchten naar je schoonmoeder terwijl jij het probeerde op te lossen. Maar op het moment dat je de tunnel uitloopt zit het vol met agenten")
                    print("")
                    print("Je geeft je over en de politie neemt je mee naar het bureau, ze zien dat je 3 mensen hebt vermoord, en geweer op zak had en dat je vroeger voor de maffia werkte. Je wordt bestraft met levenslang in de gevangenis... Je bent nu teminsten veilig van de maffia en je kan af en toe met je familie praten... Misschien is dit wel het beste...")
                    print("")
                    print("")
                    print("Misschien kan je een beter einde krijgen als je het opnieuw probeert?")
                    print("")
                    restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
                    if restart == "ja":
                        verhaal()
                    else:
                        exit()
            elif keuze12 == "B":
                print("")
                print("Je valt de 3 grote mannen aan en er is een groot gevecht, omdat je nu al 23 jaar veel vechtsporten kan win je. Je bent nu alleen erg uitgeput en omdat je een paar keer goed bent geraakt doet het nu pijn als je loopt/rent")
                print("")
                print("Je hebt nu misschien wel gewonnen van deze 3 mannen, maar dit is nog lang niet het eind. Je besluit om naar de kelder te gaan waar je kleinkinderen zitten.")
                print("")
                kelder()
                #STOP KOPIEREN HIER

        elif keuze11 == "B":
            print("")
            print("Je probeert verder te praten met de mannen maar in de midden van je zin wordt de deur open getrapt en 3 grote sterke mannen komen naar binnen.")
            print("")
            keuze13 = input("A: Probeer naar de kast te rennen. B: Probeer te vechten. Jouw keuze: ")
            if keuze13 == "A":
                print("")
                print("Je rent naar de kast en het lukt je op je geweer te pakken zonder geraakt/gepakt te worden, jullie schieten allemaal op elkaar maar omdat jij al bijna 40 jaar ervaring hebt met geweren win jij het gevecht. Het grootste probeem is nu dat heel de buurt de schoten hoorde, binnen 10 minuten zal het of vol staan met de politie of met de maffia, of misschien wel het ergste, beide...")
                print("")
                keuze14 = input("A: Ren weg. B: Ren naar je kleinkinderen. Jouw keuze: ")
                if keuze14 == "A":
                    print("")
                    print("Terwijl je wegrent hoor je sirenes en zie je de politie, je ziet 5 agenten het huis binnen gaan en 4 gaan meteen weer naar buiten om rond te kijken. 1 van agenten ziet jou en schreeuwt dat je moet stoppen en je overgeven, alles wat hun zien is 3 lijken en een renende man met een geweer, op geen een manier zou dit goed voor je aflopen...")
                    print("")
                    keuze15 = input("A: Blijf rennen. B: Geef je over. Jouw keuze: ")
                    if keuze15 == "A":
                        print("")
                        print("Je blijft rennen en rennen tot je uiteindelijk langs een gelanden vliegtuig komt, je ziet een man van het midden-oosten in de vliegtuig deur staan. Je ziet dat de man verbaasd naar je kijkt dus je geeft hem een knipoog terwijl je voorbij de vliegtuig rent.")
                        print("")
                        print("Nadat je voor bijna een half uur hebt gerend durf je pas achter je te kijken, je hebt de politie afgeshud.")
                        print("")
                        keuze16 = input("A: Ga naar het vliegveld. B: Kijk of er landen zijn waar je kan wonen. Jouw keuze: ")
                        if keuze16 == "A":
                            vliegtuig()
                        elif keuze16 == "B":
                            print("")
                            print("Je kijkt of er landen zijn en je komt op Nederland, je leest dat er veel andere vluchtelingen zijn van allemaal verschillende landen die er zijn voor allemaal verschillende redenen. De reis zal niet makkelijk zijn aangezien je officeel nu een voortvluchtige bent, maar als je er eenmaal bent wordt alles beter")
                            print("")
                            print("Er zijn een paar manieren om te reizen, de vraag is alleen welke het slimst is")
                            print("")
                            keuze17 = input("A: Ga lopend. B: Probeer vervoer te regelen. Jouw keuze: ")
                            if keuze17 == "A":
                                print("")
                                print("Je probeert naar Nederland te lopen, niet wetend hoe zwaar de reis was. Na 2 weken lopen en bijna niet eten kan je gewoon niet meer. Je besluit om eventjes te gaan liggen, je ogen worden steeds zwaarder en zwaarder en je doet je ogen dicht. Je zakt steeds meer en meer weg, tot je uiteindelijk helemaal weg bent...")
                                print("")
                                print("")
                                print("Misschien kan je een beter einde krijgen?")
                                print("")
                                restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen: ")
                                if restart == "ja":
                                    verhaal()
                                else:
                                    exit()
                            elif keuze17 == "B":
                                print("")
                                print("Je gaat naar Nederland door vervoer te regelen, Auto na auto, bus na bus. Na ongeveer 3 dagen lang voertuigen switchen ben je er eindelijk, de Nederlandse grens. 1 Van de agenten daar houd je aan en je legt heel je verhaal uit, de man belt iemand op en hij zegt dat je mee moet komen naar het bureau, hij zegt dat ze veel vragen hebben maar dat je je niet zorgen moet maken want ze gaan kijken of ze iets kunnen regelen")
                    elif keuze15 == "B":
                        print("")
                        print("Je geeft je over en de politie neemt je mee naar het bureau, ze zien dat je 3 mensen hebt vermoord, en geweer op zak had en dat je vroeger voor de maffia werkte. Je wordt bestraft met levenslang in de gevangenis... Je bent nu teminsten veilig van de maffia en je kan af en toe met je familie praten... Misschien is dit wel het beste...")
                        print("")
                        print("")
                        print("Misschien kan je een beter einde krijgen als je het opnieuw probeert?")
                        print("")
                        restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                elif keuze14 == "B":
                    print("")
                    print("Je gaat me de schuilkelder in en je gaat samen met je kleinkinderen via de geheime vlucht tunnel naar buiten, terwijl jullie wegrennen pak je je mobiel en stuur je '678' naar je vrouw. 678 betekende dat het niet meer veilig was en dat zijn vrouw de kinderen/kleinkinderen moest halen en vluchten naar je schoonmoeder terwijl jij het probeerde op te lossen. Maar op het moment dat je de tunnel uitloopt zit het vol met agenten")
                    print("")
                    print("Je geeft je over en de politie neemt je mee naar het bureau, ze zien dat je 3 mensen hebt vermoord, en geweer op zak had en dat je vroeger voor de maffia werkte. Je wordt bestraft met levenslang in de gevangenis... Je bent nu teminsten veilig van de maffia en je kan af en toe met je familie praten... Misschien is dit wel het beste...")
                    print("")
                    print("")
                    print("Misschien kan je een beter einde krijgen als je het opnieuw probeert?")
                    print("")
                    restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
                    if restart == "ja":
                        verhaal()
                    else:
                        exit()
            elif keuze13 == "B":
                print("")
                print("Je valt de 3 grote mannen aan en er is een groot gevecht, omdat je nu al 23 jaar veel vechtsporten kan win je. Je bent nu alleen erg uitgeput en omdat je een paar keer goed bent geraakt doet het nu pijn als je loopt/rent")
                print("")
                print("Je hebt nu misschien wel gewonnen van deze 3 mannen, maar dit is nog lang niet het eind. Je besluit om naar de kelder te gaan waar je kleinkinderen zitten.")
                print("")
                kelder()

    print("")
    print("Hoofdstuk 3: In Nederland")
    print("")
    print("")
    print("Je wordt naar het bureau gebracht en ze stellen je heel veel vragen. Ze vragen over je maffia tijden, over je samenwerking met de politie, je familie en hoe en waarom je hier bent gekomen. Na ongeveer 2 uur vragen zijn ze klaar en komt er een jonge vrouw binnen met papieren. Ze legt uit hoe het allemaal werkt.")
    print("")
    print("")
    print("Je gaat naar een aanmeldcentrum toe en je meld je aan als asielzoeker, alles gaat goed en je begint je asielprocedure.")
    print("")
    print("Na 8 dagen de procedure doen geven ze je toestemming om in Nederland te blijven, wat ga je nu doen?")
    print("")
    keuze18 = input("A: Zoek werk. B: Ga leren. C: Familie. Jouw keuze: ")
    if keuze18 == "A":
        werk1()
    elif keuze18 == "B":
        print("")
        print("Wat ga je leren?")
        print("")
        keuze19 = input("A: Psychologie. B: Coderen. C: Menselijke rechten. Jouw keuze: ")
        if keuze19 == "A" or keuze19 == "B" or keuze19 == "C":
            print("")
            print("Je begint met leren, maar het lukt je gewoon niet. Alles is in dit stomme Nederlandse taal, je begrijpt het gewoon simpel weg niet. Wat ga je doen?")
            print("")
            keuze20 = input("A: Stop met school en zoek werk. B: Blijf het proberen. Jouw keuze: ")
            if keuze20 == "A":
                werk1()
            elif keuze20 == "B":
                print("")
                print("Thats the spirit! Je geeft toch niet zomaar op na alles wat je hebt mee gemaakt? Dus je leert verder en na heel veel harde vermoeiende dagen kan je eindelijk een beetje Nederlands lezen/schrijven. Wat nu?")
                print("")
                keuze21 = input("A: Zoek werk. B: Leer verder. Jouw keuze: ")
                if keuze21 == "A":
                    werk1()
                elif keuze21 == "B":
                    print("")
                    print("Je leert verder en je hebt je HBO behaald, Je kan nu zonder moeite een formele brief schrijven die er ook redelijk goed uit ziet. En niet vergeten dat je nu met je HBO diploma een veel grote kans hebt om werk te zoeken!")
                    print("")
                    keuze22 = input("A: Zoek werk. B: Leer verder. C: Familie. Jouw keuze: ")
                    if keuze22 == "A":
                        werk2()
                    elif keuze22 == "B":
                        print("")
                        print("Je leert verder en je behaald een bachelors degree!")
                        print("")
                        keuze23 = input("A: Zoek werk. B: Leer verder. C: Familie. Jouw keuze: ")
                        if keuze23 == "A":
                            werk2()
                        elif keuze23 == "B":
                            print("")
                            print("Je besluit om NOG meer te leren en je behaald een masters degree!")
                            print("")
                            keuze24 = input("A: Zoek werk. B: Leer verder. C: Familie. Jouw keuze: ")
                            if keuze24 == "A":
                                werk2()
                            elif keuze24 == "B":
                                print("")
                                print("Je leert verder en je behaald een PhD!!! Je hebt nu het hoogste van het hoogste behaald. Je krijgt bijna elke dag wel een mailtje van een bedrijf die je wilt aannemen")
                                print("")
                                keuze25 = input("A: Lees je mail. B: Zoek werk. C: Familie. Jouw keuze: ")
                                if keuze25 == "A":
                                    print("")
                                    print("Je leest al je mailtjes en alles is hetzelfde, bedrijven die jou willen aannemen, logische ook, je bent een van de beste die er is. Maar er is een mailtje die anders is, je leest hem en het is een mail van iemand van BBC. Ze vragen je of je een interview wilt doen?! ")
                                    print("")
                                    keuze26 = input("A: Interview!! B: Je hebt wel betere dingen te doen. Jouw keuze: ")
                                    if keuze26 == "A":
                                        print("")
                                        print("Je stuurt een mail terug en na veel mailtjes hebben jullie nu een afspraak voor volgende week woensdag.")
                                        print("")
                                        print("Je gaat naar de interview en ze stellen je veel vragen, over je opleiding, je verleden, hoe je hier bent gekomen. Het is net als die tijd in het politie bureau, de interview is klaar en ze bedanken je met dure bloemen en veel lekkerijen.")
                                        print("")
                                        print("Een weekje later wordt je opeens gebeld, je neemt op en het is een beroemde uitgever. Hij zegt dat hij je interview met BBC geweldig vond en hij vraagt of je misschien geintreseerd bent in een boek uitgeven, je mag zelf kiezen waar het over gaat.")
                                        print("")
                                        keuze27 = input("A: Schrijf een boek. B: Wijs af, je hebt betere dingen te doen. Jouw keuze: ")
                                        if keuze27 == "A":
                                            print("")
                                            print("Je besluit een boek te schrijven, maar waar over?")
                                            print("")
                                            keuze28 = input("A: Verzin een fantasie verhaal. B: Boek over je verleden. C: Boek over je opleiding. Jouw keuze: ")
                                            if keuze28 == "A":
                                                print("")
                                                print("Je besluit om een boek te schrijven over een zelf gemaakte fantasie verhaal, na 5 maanden alleen maar bezig zijn met schrijven is je boek klaar. Je belt de uitgever en verteld je verhaal, hij is voor een paar seconde stil voordat hij begint met praten 'Tja, ik had je beloofd om je boek te releasen en een belofte is een belofte..'")
                                                print("")
                                                print("De uitgever released je boek en hij wordt bijna niet verkocht, alleen een paar nerds kopen te boek af en toe en dat is het. Wat had je ook verwacht? Je bent een fucking ex-maffia die gevlucht is met een PhD en je schrijft een fantasie boek??")
                                                print("")
                                                print("Je besluit om werk te zoeken")
                                                werk2()
                                            elif keuze28 == "B":
                                                print("")
                                                print("Na 5 maanden alleen maar bezig zijn met schrijven is je boek klaar, je belt de uitgever op en hij klinkt enthausiast")
                                                print("")
                                                print("De uitgever releasd je boek en het wordt wereldwijd verkocht, iedereen over heel de wereld vind jou boek of je verleden geweldig en veel mensen zijn er geinspireerd. Je hebt heel de wereld laten zien dat je verleden niet je toekomst bepaald, JIJ bepaald je toekomst.")
                                                print("")
                                                print("Je bent nu een beroemdheid, je verdiend veel geld. Maar wat nu")
                                                print("")
                                                keuze30 = input("A: Koop een huis. B: Familie. Jouw keuze: ")
                                                if keuze30 == "A":
                                                    huis2()
                                                elif keuze30 == "B":
                                                    fam2()
                                            elif keuze28 == "C":
                                                print("")
                                                print("Je bent een paar maandjes zoet met een boek schrijven en wanneer het klaar is bel je de uitgever")
                                                print("")
                                                print("Je verteld hem over je boek en hij vindt het een goed idee! Het is altijd intressant als een vluchteling die eerst bijna geen Nederlands kon opeens een PhD haald!")
                                                print("")
                                                print("De uitgever released je boek en hit zit in de top 10 van Nederland!")
                                                print("")
                                                print("Je bent nu een beroemdheid, je verdiend veel geld. Maar wat nu")
                                                print("")
                                                keuze31 = input("A: Koop een huis. B: Familie. Jouw keuze: ")
                                                if keuze31 == "A":
                                                    huis2()
                                                elif keuze31 == "B":
                                                    fam2()
                                        elif keuze27 == "B":
                                            print("")
                                            print("Je wijst het af en de man klinkt teleurgesteld, maar hij begrijpt het, wat ga je nu doen?")
                                            print("")
                                            keuze29 = input("A: Zoek werk. B: Familie. Jouw keuze: ")
                                            if keuze29 == "A":
                                                werk2()
                                            elif keuze29 == "B":
                                                fam052()
                                    elif keuze26 == "B":
                                        print("")
                                        print("Je besluit om het te negeren want je hebt betere dingen te doen dan een interview, maar wat ga je doen?")
                                        print("")
                                        keuze27 = input("A: Zoek werk. B: Familie. Jouw keuze: ")
                                        if keuze26 == "A":
                                            werk2()
                                        elif keuze26 == "B":
                                            fam052()
                                elif keuze25 == "B":
                                    werk2()
                                elif keuze25 == "C":
                                    fam052()
                            elif keuze24 == "C":
                                fam05()
                        elif keuze23 == "C":
                            fam05()
                    elif keuze22 == "C":
                        fam05()
    elif keuze18 == "C":
        fam0()



def werk1():
    print("")
    print("Je zoekt voor werk en je vind veel plekken die werk zoeken, je soliciteerd bij ze allemaal maar niemand wilt je behalve een snackbar. Ook wel te verwachten, je kan bijna geen Nederlands, je hebt geen opleiding af en je hebt geen werk ervaring. Maar hey, je hebt teminsten iets")
    print("")
    werk11 = input("A: Werk normaal. B: Werk hard. Jouw keuze: ")
    if werk11 == "A":
        print("")
        print("Je werkt normaal, maar de baas vindt dat niet genoeg. Hij heeft een grote risico genomen door iemand met zo weinig skills als jou aan te nemen en dan werk je niet eens hard. Je word ontslagen en na weken dakloos zijn zonder geld ga je dood vanwegen eten te kort")
        print("")
        print("")
        print("Je bent zo ver gekomen en dan maak je de verkeerde keuze... Misschien kan je een beter einde krijgen als je het opnieuw speelt..?")
        print("")
        restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
        if restart == "ja":
            verhaal()
        else:
            exit()
    elif werk11 == "B":
        print("")
        print("Je werkt erg hard voor maanden achter elkaar, je krijgt promotie tot promotie tot je uiteindelijk niet alleen de manager wordt bij de snackbar in je buurt, Almere, maar je bent ook nog eens 1 van de hoogste mensen in het snackbar bedrijf over heel Benelux.")
        print("")
        werk12 = input("A: Koop een huis. B: Familie. Jouw keuze: ")
        if werk12 == "A":
            print("")
            huis1()
        elif werk12 == "B":
            print("")
            fam1()

def werk2():
    print("")
    print("Je soliciteerd je bij meerdere plekken en ze willen je graag hebben, iemand met die diploma betekent natuurlijk een slim en strak persoon. Je hebt uiteindelijk besloten om te werken in Almere")
    print("")
    werk21 = input("A: Koop een huis. B: Familie. Jouw keuze: ")
    if werk21 == "A":
        print("")
        huis1()
    elif werk21 == "B":
        print("")
        fam1()

def fam0():
    print("")
    print("Je probeert te regelen dat je familie hier mag komen, maar het wordt geweigerd. Ze vinden dat je veelste nieuw bent en omdat je familie veilig is zien ze niet in waarom ze hier zouden moeten komen")
    print("")
    print("Hoofdstuk 4: De toekomst")
    print("")
    print("")
    print("Nadat je zonder te leren of te werken je familie probeerde te regelen en daarna afgewezen werd had je alle hoop verloren, je wilde niks meer proberen en gaf het gewoon op. Je was dakloos en probeerde te overleven door te bedelen. Maksim is uiteindelijk dood gegaan op 65 jarige leeftijd.")
    print("")
    print("Je ging zo goed... En toen maakte je de verkeerde keuze... Misschien kan je een beter einde krijgen als je het opnieuw probeert? Ik geef je zelf een tip! Probeer eerst werk of een diploma te krijgen zodat je kans groter is dat je familie hier naar toe mag komen!")
    print("")
    restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
    if restart == "ja":
        verhaal()
    else:
        exit()

def fam05():
    print("")
    print("Je probeert te regelen dat je familie hier naar toe mag komen maar het wordt geweigerd, ze zeggen dat het heel knap is dat je een opleiding hebt gedaan maar je hebt nog steeds geen werk en je woont nog steeds in een tijdelijk stichting voor asielzoekers.")
    print("")
    fam051 = input("A: Zoek werk. B: Leer verder. Jouw keuze: ")
    if fam051 == "A":
        print("")
        werk2()
    elif fam051 == "B":
        print("")

def fam052():
    print("")
    print("Je probeert te regelen dat je familie hier naar toe mag komen maar het wordt geweigerd, ze zeggen dat het heel knap is dat je een opleiding hebt gedaan maar je hebt nog steeds geen werk en je woont nog steeds in een tijdelijk stichting voor asielzoekers.")
    print("")
    print("")
    print("Je besluit werk te zoeken")
    print("")
    werk2()

def fam1():
    print("")
    print("Je probeert te regelen dat je familie hier mag komen en na veel papier werk en lang wachten hebben ze toestemming gegeven, na nog 2 weken wachten komen ze eindelijk aan. Je kleinkinderen zijn flink gegroeid, het is ook al vele jaren geleden dat je ze voor het laatst heb gezien.")
    print("")
    print("Hoofdstuk 4: De toekomst")
    print("")
    print("")
    print("Nadat je hebt geregeld dat je familie hier mocht komen heb je een mooi groot huis gekocht waar iedereen in kon leven, daarna heb je betaald voor een simpele studie voor al je kleinkinderen. Maksim is uiteindelijk dood gegaan op 84 jarige leeftijd, Maksim heeft redelijk veel berijkt in zijn leven en hij heeft er voor gezorgd dat zijn kleinkinderen een studie hebben!")
    print("")
    print("Redelijk mooi einde! Niet de beste maar wel 1 van de beste! veel beter dan dood gaan bij je eerste keuze...")

def fam2():
    print("")
    print("Je probeert te regelen dat je familie hier kan komen en je krijg zo wel meteen te horen dat ze mogen komen, nog geen 3 dagen later en ze zijn hier. je kleinkinderen zijn veel gegroeid sinds de laatste keer dat je ze zag.")
    print("")
    print("Hoofdstuk 4: De toekomst")
    print("")
    print("")
    print("Ah, het einde. Al je keuzes zijn gemaakt en alles wat je nog kan doen is de toekomst kijken. Ik moet wel zeggen, je hebt goede keuzes gemaakt!")
    print("")
    print("Nadat je familie naar Nederland kwam had je 4 grote huize gekocht, 1 voor jij en je vrouw en 1 per kind. De huizen staan rechts naast elkaar dus je kan je kleinkinderen elke dag zien. Je hebt ook betaald voor je kleinkinderen hun studie en ze studeren nu alle 4 op de beste school in een Nederland, ze bestuderen: Psychologie, coderen, menselijke rechten en marine biologie. En je 3 kinderen hebben samen een eigen bedrijf geopend voor asielzoekers, het leven kon niet beter.")
    print("")
    print("Maksim is uiteindelijk op zijn 93ste vredig dood gegaan in zijn slaap, hij heeft heel de wereld veranderd, heeft zijn familie zien opgroeien, is rijk geworden en heeft er voor gezorgd dat zijn kleinkinderen een hele goede diploma hebben gehaald. Zijn kleinkinderen zijn nu al volwassen en 1 van hun heeft zelf ook nog kinderen. Alle 4 de kleinkinderen zijn ook redelijk beroemd geworden en allemaal vanwegen andere redenen. De oudste is de beste psycholoog van Europa, de op 1 na oudste heeft een van de meest gespeelde games ooit gemaakt, de op 1 na jongste heeft veel mensen zoals Maksim een beter leven gegeven en de jongste heeft bijna al het coraal over heel de wereld gered.")
    print("")
    print("Dit is de beste einde die je kan krijgen, goed gedaan! Heb je dit in 1 keer behaald of heb je het meerdere keren gespeeld?")
    print("")
    print("Hoe dan ook, bedankt voor het spelen!")

def huis1():
    print("")
    print("Je koopt een redelijk mooi huisje in Almere, je huis is precies groot genoeg voor 1 iemand. Je hebt ook nog eens een goed betaalde baan en je helpt ook veel mensen met jou skills. ")
    print("")
    print("Hoofdstuk 4: De toekomst")
    print("")
    print("")
    print("Nadat je een huis hebt gekocht blijf je nog steeds werken, een man zoals jij heeft geen pensioen nodig. En je wilt ook helemaal geen pensioen want je hebt niks beters te doen met je tijd. Maksim is uiteindelijk dood gegaan op 84 jarige leeftijd, hij heeft veel berijkt en ook veel mensen geholpen met zijn werk. Alleen jammer dat hij zijn familie nooit meer heeft gezien...")
    print("")
    print("")
    print("Mooi einde... Alleen wel een beetje eenzaam... Misschien kan je een ander einde krijgen?")
    print("")
    restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
    if restart == "ja":
        verhaal()
    else:
        exit()

def huis2():
    print("")
    print("Je koopt een groot mooi huis in Rotterdam, je huis is veelste groot voor 1 iemand maar ja. Je hoeft nooit meer te werken. ")
    print("")
    print("Hoofdstuk 4: De toekomst")
    print("")
    print("")
    print("Maksim is uiteindelijk dood gegaan op 89 jarige leeftijd, hij heeft veel berijkt en ook veel mensen geholpen met zijn booek. Alleen jammer dat hij zijn familie nooit meer heeft gezien...")
    print("")
    print("")
    print("Mooi einde... Alleen wel een beetje eenzaam... Misschien kan je een ander einde krijgen?")
    print("")
    restart = input("Wil je het opnieuw spelen? Typ ja als je het opnieuw wilt proberen: ")
    if restart == "ja":
        verhaal()
    else:
        exit()

def kelder():
        print("Je gaat me de schuilkelder in en je gaat samen met je kleinkinderen via de geheime vlucht tunnel naar buiten, terwijl jullie wegrennen pak je je mobiel en stuur je '678' naar je vrouw. 678 betekende dat het niet meer veilig was en dat zijn vrouw de kinderen/kleinkinderen moest halen en vluchten naar je schoonmoeder terwijl jij het probeerde op te lossen")
        print("")
        print("je brengt je kleinkinderen naar de geheime plek en terwijl je wacht op je vrouw kijk je goed naar je kleinkinderen, want misschien was dit wel de laatste keer dat je ze zou zien..")
        print("")
        print("Na 11 minuten wachten komen er 2 auto's aan, je vrouw, je 3 kinderen en de andere 2 kleinkinderen stappen uit. Iedereen kijkt heel verdrietig omdat ze weten dat er een kans is dat ze je nooit meer zullen zien, je geeft iedereen een knuffel en je vrouw nog 1 laatste grote zoen. Je vrouw geeft je een klein boekje, 'wat is dit' vraag je. 'Een boekje met allemaal foto's van ons, voor als we je nooit meer zien' zegt ze terwijl jij een traan uit haar oog ziet gaan. Terwijl je gaat vraagt je jongste kleinkind of ze je ooit nog zullen zien. Wat doe je?")
        print("")
        #Keuze2 Liegen eerlijk
        keuze2 = input("A: Je bent eerlijk. B: Je liegt. Jouw keuze: ")
        if keuze2 == "A":
            print("")
            print("'Ik weet het niet schat, er is een kans dat dit de laatste keer is dat we elkaar zien. Maar ik wil dat je weet dat ik van jullie allemaal hou en ik zal altijd hier zijn' zeg je terwijl je naar je hart wijst. Je begint weer verder te lopen")
            print("")
            print("Hoofdstuk 2: De reis")
            
            vliegtuig()
        elif keuze2 == "B":
            print("")
            print("'Natuurlijk zien wij elkaar nog schat, maak je geen zorgen.' Zeg je terwijl je weer begint met verder lopen.")
            print("")
            print("Hoofdstuk 2: De reis")
            print("")
            print("")
            print("Je loopt via een vrijwel verlaten route naar een oude kapotte huis, je klopt aan en niemand doet open. je klopt nog een keer aan meer nog maals, geen reactie. je schreeuwt 'Водка теплая' en de deur gaat plotseling open. 'Wat is je naam klootzak' schreeuwt iemand terwijl je het geluid van een geweer hoort. 'Ik ben het, Maksim'. Zeg je. De man doet zijn geweer weg, 'Maksie?! hoe leef jij nog vriend, iedereen van de maffia zoekt je!!' 'Dat weet ik, Gennadi, daarom ben ik hier. Ik moet het land uit ASAP.' zei je. Gennadi stond voor even stil naar de grond te kijken voordat hij diep zucht, 'oke dan, alleen omdat wij de enige waren die iets deden tegen de gestroven onschuldige. Er zijn 2 opties...' Zei Gennadi.")
            print("")
            #Nederland Ibiza
            keuze7 = input("A: Vliegtuig naar Nederland. B: Vliegtuig naar Ibiza. Jouw keuze: ")
            if keuze7 == "A":
                print("")
                print("Gennadi brengt je naar een verlaten vliegveld met een HELE oude, roestige kapotte vliegtuig. 'Is dat ding wel veilig?!' vraag je. 'Of je gaat 100 procent dood door de Russen of er is een kans dat je dood gaat tijdens het vliegen' Zegt Gennadi. Je zucht, stapt in het vliegtuig en je vliegt naar Nederland.")
                print("")
                print("Tijdens het vliegen wordt je opeens gebeld door Gennadi.")
                print("")
                #dead alive
                keuze8 = input("A: Neem op. B: Neem niet op. Jouw keuze: ")
                if keuze8 == "A":
                    print("")
                    print(neemop)
                    print("")
                    #good/bad ending bad ending
                    keuze10 = input("A: Blijf rustig. B: Wordt boos. Jouw keuze: ")
                    if keuze10 == "A":
                        print("")
                        print(rustig)
                        print("")
                        print("")
                        print("In tijden zoals dit is het niet verstandig om andere ex-maffias vertrouwen... Maar hey, je familie zal nooit meer problemen hebben, je beste vriend zal een goed leven hebben en geeft je familie de helft van wat hij gaat verdienen, je kleinkinderen gaan zelfs een studie doen! Het is misschien niet de beste einde maar het kon ook veel slechter gaan! Misschien kan je het opnieuw proberen en een beter einde krijgen..?")
                        print("")
                        restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                    elif keuze10 == "B":
                        print("")
                        print(boos)
                        print("")
                        print("")
                        print("Wat had je verwacht..? Je wordt gezocht door de grootste maffia groep van heel Rusland en jij denkt dat je naar een ex-maffia kan gaan en verwachten dat hun hem niks aanbieden? In tijden zoals dit is het beter om niemand te vertrouwen... Misschien kan je een beter einde krijgen als je het opnieuw probeert, nou, ik weet wel zeker dat je een beter einde kan krijgen. Alles is beter dan denken dat je veilig gaat zijn en dan verraden worden door je beste vriend.")
                        print("")
                        restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                elif keuze8 == "B":
                    print("")
                    print("")
            elif keuze7 == "B":
                print("")
                print("Gennadi brengt je naar een verlaten vliegveld met een HELE oude, roestige kapotte vliegtuig. 'Is dat ding wel veilig?!' vraag je. 'Of je gaat 100 procent dood door de Russen of er is een kans dat je dood gaat tijdens het vliegen' Zegt Gennadi. Je zucht, stapt in het vliegtuig en je vliegt naar Ibiza.")
                print("")
                print("Tijdens het vliegen wordt je opeens gebeld door Gennadi.")
                print("")
                #good/bad bad ending
                keuze9 = input("A: Neem op. B: Neem niet op. Jouw keuze: ")
                if keuze9 == "A":
                    print("")
                    print(neemop)
                    print("")
                    keuze10 = input("A: Blijf rustig. B: Wordt boos. Jouw keuze: ")
                    if keuze10 == "A":
                        print("")
                        print(rustig)
                        print("")
                        print("")
                        print("In tijden zoals dit is het niet verstandig om andere ex-maffias vertrouwen... Maar hey, je familie zal nooit meer problemen hebben, je beste vriend zal een goed leven hebben en geeft je familie de helft van wat hij gaat verdienen, je kleinkinderen gaan zelfs een studie doen! Het is misschien niet de beste einde maar het kon ook veel slechter gaan! Misschien kan je het opnieuw proberen en een beter einde krijgen..?")
                        print("")
                        restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                    elif keuze10 == "B":
                        print("")
                        print(boos)
                        print("")
                        print("")
                        print("Wat had je verwacht..? Je wordt gezocht door de grootste maffia groep van heel Rusland en jij denkt dat je naar een ex-maffia kan gaan en verwachten dat hun hem niks aanbieden? In tijden zoals dit is het beter om niemand te vertrouwen... Misschien kan je een beter einde krijgen als je het opnieuw probeert, nou, ik weet wel zeker dat je een beter einde kan krijgen. Alles is beter dan denken dat je veilig gaat zijn en dan verraden worden door je beste vriend.")
                        print("")
                        restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                elif keuze9 == "B":
                    print("")
                    print("Je neemt niet op en je vliegt naar Ibiza. Hier heb je eindelijk rust, leuke strand, mooie meide, aardige mensen, maar het belangrijkste, geen Russen. Maar is dit het waard? nooit meer of voor een HELE lange tijd je familie in het echt zien? ALtijd alleen maar via telefoon bellen met hun? 'Nou ja' denk je, 'Zolang hun veilig zijn en ik nog met hun kan praten is dat alles wat telt'")
                    print("")
                    print("")
                    print("Mooi einde, Maar dat kan toch wel beter?")
                    print("")
                    restart = input("Wil jet het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
                    if restart == "ja":
                        verhaal()
                    else:
                        exit()

def vliegtuig():
                print("")
                print("")
                print("Je loopt naar het vliegveld, constant je gezicht verbergen, constant om je heen kijken en constant bang zijn dat het elk moment over kan zijn. Maar je bent bij het vliegveld gekomen en tijdens de 2 lange uren lopen is er niks ergs gebeurt. Maar terwijl je naar binnen loopt zie je dat er heel veel beveileging is, 'natuurlijk' zei Maksim 'dit heb ik weer, alles dat ze kunnen vinden over mij is dat ik ex-maffia ben.'")
                print("")
                #Keuze3 Door terug
                keuze3 = input("A: Loop terug. B: Ga verder. Jouw keuze: ")
                if keuze3 == "A":
                    print("")
                    print("Je draait je om om weer weg te gaan maar een beveiliger stopt je, 'Waar gaan wij zo plotseling naar toe?' vraagt de man.")
                    print("")
                    #Keuze4 einde
                    keuze4 = input("A: 'Ik ben iets thuis vergeten'. B: 'Ik heb mijn vlucht gemist'. Jouw keuze: ")
                    if keuze4 == "A" or keuze4 == "B":
                        print("")
                        print("'Jaja' zegt de man, laat je ID maar zien. je laat je ID zien, de man herkent je meteen en denkt dat jij ook een van de ontsnapte maffia members bent, neit wetend dat je hun juist hebt opgesloten. Je wordt naar de gevangenis gebracht en omdat je het land probeerde te vluchten kom je in een max-security prison, Je mag niemand zien, geen phone calls, niks. 'Wat een kut manier op te gaan, rottend in een cel'. Zeg je...")
                        print("")
                        print("")
                        print("Tja.. Das idd een kut manier om te eindigen.. Misschien kan je het opnieuw spelen en een beter einde krijgen..?")
                        print("")
                        restart = input("Wil je het opnieuw spelen? typ ja als je het opnieuw wilt proberen. ")
                        if restart == "ja":
                            verhaal()
                        else:
                            exit()
                elif keuze3 == "B":
                    print("")
                    print("Je loopt verder langs de guard, je lacht vriendelijk naar hem en hij stopt je niet. Je gaat naar de balie.")
                    print("")
                    #Keuze5 Ibiza Nederland
                    keuze5 = input("A: Koop een ticket naar Ibiza. B: Koop een ticket naar Nederland. Jouw keuze: ")
                    if keuze5 == "A":
                        print("")
                        print("Je stapt in het vliegtuig en je vliegt naar Ibiza. Hier heb je eindelijk rust, leuke strand, mooie meide, aardige mensen, maar het belangrijkste, geen Russen. Maar is dit het waard? nooit meer of voor een HELE lange tijd je familie in het echt zien? ALtijd alleen maar via telefoon bellen met hun? 'Nou ja' denk je, 'Zolang hun veilig zijn en ik nog met hun kan praten is dat alles wat telt'")
                        print("")
                        print("")
                        print("Mooi einde, Maar het kan toch beter?")
                    elif keuze5 == "B":
                        print("")
                        print("Je koopt een ticket naar Nederland, stapt in het vliegtuig, en je vliegt weg.")
                        print("")
                        print("Je zit nog maar 20 minuten in het vliegtuig en je begint je nu al heel erg te vervelen, misschien kan je iets doen om het leuker te maken?")
                        print("")
                        #Keuze Dood Levend
                        keuze6 = input("A: Probeer te slapen. B: Kijk een film. C: Bel je familie op. Jouw Keuze: ")
                        if keuze6 == "A" or keuze6 == "B":
                            print("")
                            print("De tijd vliegt voorbij en voor je het weet ben je al in Nederland. 'Het is me gelukt.' Denk je")
                        elif keuze6 == "C":
                            print("")
                            print("Je belt je vrouw op en ze begint opeens te huilen, 'Maksim.' Hoor je iemand lachend zeggen. 'Jij bent wel echt fucking dom of niet soms? Je vrouw bellen? Echt waar? We hebben nu je locatie klootzak' Zegt de man. 'Oh? Je zit op een vliegtuig?' De man begint met lachen. 'Hoe voelt het bloed van zo veel onschuldige mensen op je handen te hebben?' Vraagt de man lachend. 'Wat bedoel je?!' Vraag je schreeuwend. Opeens hoor je een fighter jet achter je vliegen, 'Ik denk dat je al weet wat ik bedoel, fijne reis nog, rat' Zegt de man voordat hij ophangt...")
                            print("")
                            print("")
                            print("Om te overleven moet je slimme keuzes maken en er alles aan doen om niet in contact te komen met de maffia, misschien kan je een beter einde krijgen als je het opnieuw speelt..?")


verhaal()

neemop = "Je neemt op en Gennadi begint meteen met praten, geen groet, niks. 'Het spijt me Maksie...' 'Gen, wat heb je gedaan?' Vraag je met een tril in je stem. 'Je hebt het huis gezien waar ik in woon, ik kon geen nee zeggen...' 'WAAR HEB JE HET OVER' Schreeuw je. 'DE RUSSEN HEBBEN ME 5 MILJOEN PER JAAR BELOOFD MAKSIE' zegt Gennadi met een brok in zijn keel, je kan duidelijk horen dat hij hier moeite mee je denkt terug aan de tijden waar jullie samen bij de. Je gedachte wordt onderbroken door het geluid van een andere vliegtuig. 'Het spijt me Maksie, het spijt me echt heel erg' zegt Gennadi."
rustig = "'Het geeft niet Gen, beloof me 1 ding,' Zeg je. 'Geef 1.5 miljoen per jaar aan mijn familie zodat de meiden een studie kunnen doen en niet vies werk zoals ons moeten doen.''Ik beloof het Maksie, ik geef ze zelfs de helft van wat ik krijg per jaar.' Reageert Gennadi 'Dankje oude vriend.' Jullie eindigen het door samen jullie eigen geschreven lied te zingen"
boos = "'JIJ VUILE KANKER VERRADER!!' schreeuw je uit, zo boos dat je zelfs met het enige woord sheld waar je nooit mee zou schelden nadat je vader er aan is gestorven. Maar wat boeit het nog denk je, ik ga toch dood. je hoort dat Gennadi aan het huilen is, maar dat boeit je niet. '5 jaar Gen, we zijn waren al vrienden sinds we 5 fucking jaar waren. En dan doe je dit?! Gen, jij bent een vuile, vieze, pest rat en ik hoop dat je no-'"