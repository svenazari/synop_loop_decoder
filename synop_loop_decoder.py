#Synop Loop Decoder
#MadeBy: SvenAzari
#Requirements: Python3

#Please read commented instruction in lines to properly set this script.

#imports
import sys
import math
import datetime
from datetime import timezone

#lists
#empty lists
bystations = [] #list of synop reports for stations
synop222 = [] #decond section of synop report
synop333 = [] #third section of synop report
decoded = [] #decoded values
decoded222 = [] #decoded values from second section
decoded333 = [] #decodec values from third section
#lists with data
hlis = ["je u sloju od 0 m do 50 m iznad meteorološke postaje.", "je u sloju od 50 m do 100 m iznad meteorološke postaje.", "je u sloju od 100 m do 200 m iznad meteorološke postaje.", "je u sloju od 200 m do 300 m iznad meteorološke postaje.", "je u sloju od 300 m do 600 m iznad meteorološke postaje.", "je u sloju od 600 m do 1000 m iznad meteorološke postaje.", "je u sloju od 1 km do 1.5 km iznad meteorološke postaje.", "je u sloju od 1.5 km do 2 km iznad meteorološke postaje.", "je u sloju od 2 km do 2.5 km iznad meteorološke postaje.", "je 2.5 km ili više iznad meteorološke postaje."] #cloud hight
wwlis = ["Razvoj oblaka nije opažan ili se nije mogao opažati", "Oblaci se općenito rasplinjuju ili postaju slabije razvijeni", "Stanje neba u cjelini je nepromjenjeno", "Oblaci se općenito stvaraju ili razvijaju", "Vidljivost smanjena dimom", "Suha mutnoća", "Raširena prašina lebdi u zraku - ne dignuta vjetrom - na postaji ili blizu postaje u vrijeme opažanja", "Prašina ili pijesak podignut vjetrom na ili blizu postaje u vrijeme opažanja, ali nema dobro razvijenih vrtloga prašine ili vrtloga pijeska niti se vidjela prašinska ili pješčana oluja", "Dobro razvijeni vrtlog ili vrtlozi prašine ili pijeska - na ili blizu postaje - tijekom prethodnog sata, ali ne i prašinska ili pješčana oluja", "Prašinska ili pješčana oluja u vidokrugu u vrijeme opažanja, ili na postaji tijekom prethodnog sata", "Sumaglica", "Niska ili ledena magla na postaji - bilo na kopnu ili na moru - ne deblja od 2 m na kopnu ili 10 m na moru (u krpama)", "Niska ili ledena magla na postaji - bilo na kopnu ili na moru - ne deblja od 2 m na kopnu ili 10 m na moru (više ili manje neprekidan sloj)", "Sijevanje (grmljavina se ne čuje)", "Virga", "Oborina u vidokrugu van kruga od 5 km - doseže tlo ili površinu mora", "Oborina u vidokrugu u krugu od 5 km, ali ne i na postaji - doseže tlo ili površinu mora", "Grmljavina (nema oborine u vidokrugu)", "Oluja u vidokrugu postaje tijekom prethodnog sata ili u vrijeme opažanja", "Tornado ili pijavica u vidokrugu postaje tijekom prethodnog sata ili u vrijeme opažanja", "Rosulja (ne smrzava se) ili zrnat snijeg tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Kiša (ne smrzava se) koja ne pada kao pljuskovi tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Snijeg tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Susnježica tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Prehladna rosulja ili prehladna kiša tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Pljusak kiše tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Pljusak snijega ili susnježice tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Pljusak tuče ili pljusak kiše i tuče tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Magla ili ledena magla tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Grmljavina (sa ili bez oborine) tijekom prethodnog sata, ali ne i u vrijeme opažanja", "Slaba ili umjerena prašinska ili pješčana oluja oslabila tijekom prethodnog sata", "Slaba ili umjerena prašinska ili pješčana oluja bez značajne promjene tijekom prethodnog sata", "Slaba ili umjerena prašinska ili pješčana oluja započela ili pojačala tijekom prethodnog sata", "Žestoka prašinska ili pješčana oluja oslabila tijekom prethodnog sata", "Žestoka prašinska ili pješčana oluja bez značajne promjene tijekom prethodnog sata", "Žestoka prašinska ili pješčana oluja započela ili pojačala tijekom prethodnog sata", "Slaba ili umjerena vijavica - niska (ispod razine oka)", "Jaka vijavica - niska (ispod razine oka)", "Slaba ili umjerena vijavica - visoka (iznad razine oka)", "Jaka vijavica - visoka (iznad razine oka)", "Magla ili ledena magla u daljini u vrijeme opažanja - ali ne na postaji tijekom prethodnog sata - nadvisuje motritelja", "Magla ili ledena magla u krpama", "Magla ili ledena magla, nebo vidljivo - razrijedila se tijekom prethodnog sata", "Magla ili ledena magla, nebo nevidljivo - razrijedila se tijekom prethodnog sata", "Magla ili ledena magla, nebo vidljivo - bez promjene tijekom prethodnog sata", "Magla ili ledena magla, nebo nevidljivo - bez promjene tijekom prethodnog sata", "Magla ili ledena magla, nebo vidljivo - započela ili postala gušćom tijekom prethodnog sata", "Magla ili ledena magla, nebo nevidljivo - započela ili postala guščom tijekom prethodnog sata", "Magla, stvara inje, nebo vidljivo", "Magla, stvara inje, nebo nevidljivo", "Rosulja s prekidima - ne smrzava se - slaba u vrijeme opažanja", "Rosulja neprekidna - ne smrzava se - slaba u vrijeme opažanja", "Rosulja s prekidima - ne smrzava se - umjerena u vrijeme opažanja", "Rosulja neprekidna - ne smrzava se - umjerena u vrijeme opažanja", "Rosulja s prekidima - ne smrzava se - jaka u vrijeme opažanja", "Rosulja neprekidna - ne smrzava se - jaka u vrijeme opažanja", "Rosulja - smrzava se - slaba", "Rosulja - smrzava se - umjerena ili jaka", "Rosulja i kiša - slaba", "Rosulja i kiša - umjerena ili jaka", "Kiša s prekidima - ne smrzava se - slaba u vrijeme opažanja", "Kiša neprekidna - ne smrzava se - slaba u vrijeme opažanja", "Kiša s prekidima - ne smrzava se - umjerena u vrijeme opažanja", "Kiša neprekidna - ne smrzava se - umjerena u vrijeme opažanja", "Kiša s prekidima - ne smrzava se - jaka u vrijeme opažanja", "Kiša neprekidna - ne smrzava se - jaka u vrijeme opažanja", "Kiša - smrzava se - slaba", "Kiša - smrzava se - umjerena ili jaka", "Kiša ili rosulja i snijega - slaba", "Kiša ili rosulja i snijeg - umjerena ili jaka", "Padanje snježnih pahuljica s prekidima - slabo u vrijeme opažanja", "Neprekidno padanje snježnih pahuljica - slabo u vrijeme opažanja", "Padanje snježnih pahuljica s prekidima - umjereno u vrijeme opažanja", "Neprekidno padanje snježnih pahuljica - umjereno u vrijeme opažanja", "Padanje snježnih pahuljica s prekidima - jako u vrijeme opažanja", "Neprekidno padanje snježnih pahuljica - jako u vrijeme opažanja", "Ledene iglice (sa ili bez magle)", "Zrnat snijeg (sa ili bez magle)", "Pojedinačni snježni kristali poput zvjezdica (sa ili bez magle)", "Ledena zrna ili solika", "Pljusak kiše - slab", "Pljusak kiše - umjeren ili jak", "Pljusak kiše - silan", "Pljusak susnježica - slab", "Pljusak susnježica - umjeren ili jak", "Pljusak snijega - slab", "Pljusak snijega - umjeren ili jak", "Pljusak ledenih zrna ili solike sa ili bez kiše ili susnježice - slab", "Pljusak ledenih zrna ili solike sa ili bez kiše ili susnježice - umjeren ili jak", "Pljusak tuče, sa ili bez kiše ili susnježice, bez grmljavine - slab", "Pljusak tuče, sa ili bez kiše ili susnježice, bez grmljavine - umjeren ili jak", "Slaba kiša u vrijeme opažanja - grmljavina tijekom prethodnog sata, ali ne u vrijeme opažanja", "Umjerena ili jaka kiša u vrijeme opažanja - grmljavina tijekom prethodnog sata, ali ne u vrijeme opažanja", "Slabi snijeg, susnježica ili tuča u vrijeme opažanja - grmljavina tijekom prethodnog sata, ali ne u vrijeme opažanja", "Umjereni ili jaki snijeg, susnježica ili tuča u vrijeme opažanja - grmljavina tijekom prethodnog sata, ali ne u vrijeme opažanja", "Grmljavina - slaba ili umjerena - bez tuče", "Grmljavina - slaba ili umjerena - s tučom", "Grmljavina - jaka - bez tuče, ali s kišom i/ili snijegom u vrijeme opažanja", "Grmljavina kombinirana s prašinskom ili pješćanom olujom u vrijeme opažanja", "Grmljavina - jaka - s tučom u vrijeme opažanja"] #current weather
wlis = ["N <= 5", "DIO N < 5 & DIO N > 5", "N > 5", "Pješčana ili prašinska oluja ili visoka vijavica", "Magla ili ledena magla ili gusta suha mutnoća", "Rosulja", "Kiša", "Snijeg ili susnježica", "Pljusak (pljuskovi)", "Grmljavina"] #previous weather
clow = ["NEMA", "Cu hum/fra", "Cu med/con", "Cb cal", "Sc cugen", "Sc NE cugen", "St neb/fra", "St fra (lošeg vremena)", "Sc i Cu ili Cu i Sc", "Cb cap"] #low level clouds
cmed = ["NEMA", "As tr", "As op/Ns", "Ac tr", "Ac tr len", "Ac tr/op NAPREDUJE", "Ac cugen ili cbgen", "2X Ac tr/op ili Ac tr/op + As/Ns", "Ac cas/flo", "Ac KAOTIČNOG NEBA"] #middle level clouds
chigh = ["NEMA", "Ci fib (unc)", "Ci spi (cas, flo)", "Ci spi cbgen", "Ci unc/fib NAPREDUJE", "Ci i/ili Cs ISPOD 45°", "Ci i/ili Cs IZNAD 45°", "Cs (N=8)", "Cs (N<8)", "Cc (DOMINIRA)"] #high level clouds
Ens = ["suho", "vlažno", "mokro", "poplavljeno", "smrznuto", "poledica", "djelomično prašina", "tanki sloj prašine", "debeli sloj prašine", "suho s pukotinama"] #condition of soil
Ews = ["uglavnom led", "zbijeni (mokri) snijeg prekriva manje od 50% tla", "zbijeni (mokri) snijeg prekriva između 50 i 100% tla", "zbijeni (mokri) snijeg u potpunosti prekiva tlo (ravno)", "zbijeni (mokri) snijeg u potpunosti prekiva tlo (neravno)", "pršić prekriva manje od 50% tla", "pršić prekriva između 50 i 100% tla", "pršić prekriva 100% tla (ravno)", "pršić prekriva 100% tla (neravno)", "pršić prekriva 100% tla (zapusi)"] #condition of soil with snow cover

dt = datetime.datetime.now(timezone.utc) #utc time
yearutc = dt.year #utc year
monthutc = dt.month #utc month
dayutc = dt.day #utc day
hourutc = dt.hour #utc hour
hourutcp = str(hourutc).zfill(2)
time = str(dayutc) + "." + str(monthutc) + "." + str(yearutc) + "., " + str(hourutcp) + " UTC"

#read from file and save in list bystations
with open ("/home/azari/scripts/latest_synop.txt") as synop: #location of input file
    for line in synop:
        bystations.append(line)

length = len(bystations)

report = open("/home/azari/scripts/report.txt", "w+") #creating and opening file to write decoded reports into - location of output file needs to be set according to users needs
#izjave o odricanju od odgovornosti
report.write("Neobrađeni podaci u obliku synop izvještaja su preuzeti sa WEB stranice www.ogimet.com.")
report.write("\n")
report.write("Synop izvještaji su obrađeni skriptom Synop Loop Decoder.") 
report.write("\n")
report.write("Autor skripte ne odgovara za greške nastale zbog nedostatka podataka ili zbog netočnog unosa poslanih podataka sa meteoroloških postaja.")
report.write("\n")
report.write("Skripta i podaci dobiveni korištenjem skrite nisu namjenjeni za službenu upotrebu te autor skripte ne odgovara za štetu nastalu prilikom pokušaja korištenja skripte i/ili obrađenih podataka na takav način.")
report.write("\n")
report.write("\n")
report.write("###")
report.write("\n")
report.write("\n")
#početak txt datoteke
report.write("Synop izvještaj za: " + time)
report.write("\n")

c = 0 #starting increment for bystations

while c < length:
    synstat = bystations[0+c] #read synop for each station
    synoplist = synstat.split(" ") #make list of synop groups for selected station
    synlen = len(synoplist) #number of groups in selected synop
    
    #removing unnecessary characters
    synretx = synoplist[synlen-1] #pick last group in selected synop
    synret = synretx[0:5]
    del synoplist[-1]
    synoplist.append(synret)
    
    lf = "333" #look for beginning of third section
    
    if lf in synoplist: 
        loc333 = synoplist.index("333")
        ran = int(loc333)
        for k in range (ran+1, synlen): #append third section to synop333
            synop333.append(synoplist[k])
    else:
        ran = int(synlen)
    
    d = 0 #starting increment for synoplist
    
    #decoding synop
    while d in range (0, ran):
        group = synoplist[0+d]
        if d == 0:
            decoded.append("SYNOP") #decoded[0]
        elif d == 1:
            iW = group[4:5]
            decoded.append(iW) #decoded[1]
        elif d == 2:
            postaja = group[2:5]
            if postaja == "216":
                postajaprint = "Rijeka - Kozala"
            elif postaja == "219":
                postajaprint = "Parg"
            elif postaja == "232":
                postajaprint = "Karlovac"
            elif postaja == "234":
                postajaprint = "Krapina"
            elif postaja == "235":
                postajaprint = "Puntijarka"
            elif postaja == "236":
                postajaprint = "Zagreb - Grič"
            elif postaja == "240":
                postajaprint = "Zagreb - Maksimir"
            elif postaja == "241":
                postajaprint = "Zagreb - Pleso"
            elif postaja == "244":
                postajaprint = "Sisak"
            elif postaja == "246":
                postajaprint = "Varaždin"
            elif postaja == "248":
                postajaprint = "Križevci"
            elif postaja == "253":
                postajaprint = "Bjelovar"
            elif postaja == "256":
                postajaprint = "Bilogora"
            elif postaja == "258":
                postajaprint = "Daruvar"
            elif postaja == "280":
                postajaprint = "Osijek - Čepin"
            elif postaja == "284":
                postajaprint = "Osijek - Klisa"
            elif postaja == "307":
                postajaprint = "Pula Aerodrom"
            elif postaja == "308":
                postajaprint = "Pazin"
            elif postaja == "314":
                postajaprint = "Mali Lošinj"
            elif postaja == "317":
                postajaprint = "Rijeka - Omišalj"
            elif postaja == "321":
                postajaprint = "Rab"
            elif postaja == "323":
                postajaprint = "Senj"
            elif postaja == "324":
                postajaprint = "Zavižan"
            elif postaja == "328":
                postajaprint = "Ogulin"
            elif postaja == "330":
                postajaprint = "Gospić"
            elif postaja == "365":
                postajaprint = "Gorice"
            elif postaja == "370":
                postajaprint = "Slavonski Brod"
            elif postaja == "382":
                postajaprint = "Gradište"
            elif postaja == "428":
                postajaprint = "Zadar - Puntamika"
            elif postaja == "431":
                postajaprint = "Zadar - Zemunik"
            elif postaja == "438":
                postajaprint = "Šibenik"
            elif postaja == "441":
                postajaprint = "Komiža"
            elif postaja == "442":
                postajaprint = "Knin"
            elif postaja == "443":
                postajaprint = "Palagruža"
            elif postaja == "444":
                postajaprint = "Split - Resnik"
            elif postaja == "445":
                postajaprint = "Split - Marijan"
            elif postaja == "447":
                postajaprint = "Hvar"
            elif postaja == "452":
                postajaprint = "Lastovo"
            elif postaja == "454":
                postajaprint = "Makarska"
            elif postaja == "462":
                postajaprint = "Ploče"
            elif postaja == "472":
                postajaprint = "Dubrovnik - Gorice"
            elif postaja == "474":
                postajaprint = "Dubrovnik - Ćilipi"
            else:
                postajaprint = str(postaja)
            decoded.append("Postaja: " + postajaprint + " (14" + postaja + ")") #decoded[2]
        elif d == 3:
            iR = group[0:1] #ir idicator
            decoded.append(iR) #decoded[3]
            iX = group[1:2] #ix indicator
            decoded.append(iX) #decoded[4]
            h = group[2:3] #hight od lowest clouds
            if h == "/":
                hprint = "Visinu podnice najnižih oblaka nije moguće odrediti."
            else:
                hint = int(h)
                hprint = "Visina podnice najnižih oblaka " + hlis[0+hint]
            decoded.append(hprint) #decoded[5]
            VV = group[3:5] #visibility
            if VV == "//":
                vvp = "nije poznata."
            else:
                VVf = float(VV)
                if VVf == 0:
                    vvp = "manja od 100."
                elif VVf >= 1 and VVf < 10:
                    vvx = str(VVf * 100)
                    vvp = vvx + " m."
                elif VVf >= 10 and VVf <= 50:
                    vvx = str(VVf / 10)
                    vvp = vvx + " km."
                elif VVf > 55 and VVf <= 80:
                    vvx = str(round(VVf - 50))
                    vvp = vvx + " km."
                elif VVf >= 81 and VVf <= 88:
                    vvx = str(round(5 * VVf - 370))
                    vvp = vvx + " km."
                elif VVf == 89:
                    vvp = "je veća od 70 km."
            decoded.append("Vidljivost: " + vvp) #decoded[6]
        elif d == 4:
            N = group[0:1] #total cloud cover (x/8)
            dd = group[1:3] #wind direction
            ff = group[3:5] #wind speed
            if ff == "//":
                vjx = "nepoznat"
            else:
                fff = int(ff)
            vjind = decoded[1] #wind speed indicator (saved in decoded)
            if N == "9":
                Nprint = "Ukupnu naoblaku nije moguće odrediti jer se oblaci ne vide."
            elif N == "/":
                Nprint = "Nije poznat podatak o ukupnoj naoblaci."
            else:
                N10 = int(round(int(N) * 10 / 8,0) * 10) #converting total cloud cover from x/8 to x/10
                Nprint = "Ukupna naoblaka: " + str(N10) + "%"
            decoded.append(Nprint) #decoded[7]
            if fff == 0:
                vjx = "Tišina"
            else:
                if dd == "//":
                    vjx =  "nepoznat"
                else:
                    if dd == "35" or dd == "36" or dd == "01": #wind direction from asimut to directon
                        vjetprint = "N"
                    if dd == "02" or dd == "03":
                        vjetprint = "NNE"
                    if dd == "04" or dd == "05":
                        vjetprint = "NE"
                    if dd == "06" or dd == "07":
                        vjetprint = "ENE"
                    elif dd == "08" or dd == "09" or dd == "10":
                        vjetprint = "E"
                    if dd == "11" or dd == "12":
                        vjetprint = "ESE"
                    if dd == "13" or dd == "14":
                        vjetprint = "SE"
                    if dd == "15" or dd == "16":
                        vjetprint = "SSE"
                    elif dd == "17" or dd == "18" or dd == "19":
                        vjetprint = "S"
                    if dd == "20" or dd == "21":
                        vjetprint = "SSW"
                    if dd == "22" or dd == "23":
                        vjetprint = "SW"
                    if dd == "24" or dd == "25":
                        vjetprint = "WSW"
                    elif dd == "26" or dd == "27" or dd == "28":
                        vjetprint = "W"
                    if dd == "29" or dd == "30":
                        vjetprint = "WNW"
                    if dd == "31" or dd == "32":
                        vjetprint = "NW"
                    if dd == "33" or dd == "34":
                        vjetprint = "NNW"
                    if vjind == "0" or vjind == "1": #decode wind speed unit indicator to wind speed unit
                        vjindp = "m/s"
                    elif vjind == "3" or vjind == "4":
                        vjindp = "kt"
                    vjx = vjetprint + ", " + str(fff) + " " + vjindp
            decoded.append("Vjetar: " + vjx) #decoded[8]
        elif d == 5:
            sns = group[1:2] #indicator if air temperature is positive or negative
            TTT = group[2:5] #air temperature (coded)
            if sns == "0":
                TS = float(TTT) / 10 #decoded air temperature
            else:
                TS = float(TTT) / -10
            decoded.append(TS) #decoded[9]
        elif d == 6:
            snd = group[1:2] #indicator if dew point is positive or negative
            TdTdTd = group[2:5] #dew point (coded)
            if snd == "0":
                TD = float(TdTdTd) / 10 #decoded dew point
            else:
                TD = float(TdTdTd) / -10
            decoded.append(TD) #decoded[10]
            #calculating relative air humidity
            Tt = float(decoded[9])
            #constants
            e = 2.718282
            #positive air temperature
            p1 = 6.10780
            p2 = 17.08085
            p3 = 234.175
            #negative air temperature
            pv1 = 6.10780
            pv2 = 17.84362
            pv3 = 245.425
            if (Tt < 0): #constants for air temperature
                ctt1 = pv1
                ctt2 = pv2
                ctt3 = pv3
            else:
                ctt1 = p1
                ctt2 = p2
                ctt3 = p3
            if (TD < 0): #constants for dew point
                ctd1 = pv1
                ctd2 = pv2
                ctd3 = pv3
            else:
                ctd1 = p1
                ctd2 = p2
                ctd3 = p3
            mitt = ctt2 * Tt / (ctt3 + Tt)
            SVPTT = ctt1 * math.pow(e,mitt) #water waper saturation pressure for air temperature
            mitd = ctd2 * TD / (ctd3 + TD)
            SVPTD = ctd1 * math.pow(e,mitd) #water waper saturation pressure for dew point
            U = round(SVPTD / SVPTT * 100) #calculation for relative air humidity
            decoded.append("Relativna vlažnost zraka: " + str(U) + "%") #decoded[11]
        elif d == 7:
            b = float(group[1:5]) #coded air pressure on station level
            bx = b / 10
            if bx < 100:
                ppp = 1000 + bx
            else:
                ppp = bx
            decoded.append("Tlak zraka na razni postaje: " + str(ppp) + " hPa") #decoded[12]
        elif d == 8:
            x = group[1:2]
            if x == "1": #1000 hPa
                hhh = float(group[2:5])
                hhhp = str(hhh)
                pr = str(1000)
                P0print = "Visina izobarne plohe od " + pr + " hPa: " + hhhp + " GPM"
            elif x == "2": #925 hPa
                hhh = float(group[2:5])
                if hhh < 300:
                     hhhp = str(round(hhh + 1000))
                else:
                    hhhp = str(round(hhh))
                    pr = str(925)
                P0print = "Visina izobarne plohe od " + pr + " hPa: " + hhhp + " GPM"
            elif x == "8": #850 hPa
                hhh = float(group[2:5])
                hhhp = str(round(1000 + hhh))
                pr = str(850)
                P0print = "Visina izobarne plohe od " + pr + " hPa: " + hhhp + " GPM"
            else:
                b0 = float(group[1:5]) #coded air pressure on mean see level
                b0x = b0 / 10
                if b0x < 100:
                    p0p0p0 = 1000 + b0x
                else:
                    p0p0p0 = b0x
                P0print = "Tlak zraka sveden na srednju morsku razinu: " + str(p0p0p0) + " hPa"
            decoded.append(P0print) #decoded[13]
        elif d == 9:
            ap = group[1:2]
            if ap == "/":
                decoded.append("Promjena tlaka zraka u zadnjih 3 sata nije poznata.")
            appp = group[2:5]
            if appp == "///":
                decoded.append("Promjena tlaka zraka u zadnjih 3 sata nije poznata.")
            else:
                if ap == "0" or ap == "1" or ap == "2" or ap == "3":
                    tpx = "raste"
                elif ap == "4":
                    tpx = "stagnira"
                if ap == "5" or ap == "6" or ap == "7" or ap == "8":
                    tpx = "pada"
                try:
                    apppx = float(appp) / 10
                except:
                    decoded.append("Promjena tlaka zraka u zadnjih 3 sata nije poznata.")
                else:
                    decoded.append("Promjena tlaka zraka u zadnjih 3 sata: " + str(apppx) + " hPa") #decoded[14]
                    decoded.append("Tlak zraka " + tpx) #decoded[15]
        elif d == 10:
            x = group[0:1]
            if x == "6":
                RRR = float(group[1:4])
                Rt = group[4:5]
                if RRR == 0:
                    rrrp = "0 mm (nije bilo oborine)"
                elif RRR == 990:
                    rrrp = "0 mm (oborina u tragovima)"
                elif RRR > 990 and RRR <= 999:
                    RRRx = (RRR - 990) / 10
                    rrrp = str(RRRx) + " mm"
                else:
                    RRRx = int(RRR)
                    rrrp = str(RRRx) + " mm"
                if Rt == "1":
                    Rtp = 6
                elif Rt == "2":
                    Rtp = 12
                Rprint = "Količna oborine u prethodnih " + str(Rtp) + " sati: " + str(rrrp)
                decoded.append(Rprint)
            elif x == "7": #weather phenomenas
                ww = int(group[1:3])
                WW1 = group[3:4]
                WW2 = group[4:5]
                wwp = wwlis[0+ww]
                if WW1 == "/" and WW2 == "/":
                    WWp = "nije poznato"
                elif WW1 == "/" and WW2 != "/":
                    WWp = wlis[0+int(WW2)]
                elif WW1 != "/" and WW2 == "/":
                    WWp = wlis[0+int(WW1)]
                elif WW1 == WW2:
                    WWp = wlis[0+int(WW1)]
                else:
                    WWp = wlis[0+int(WW1)] + " i " + wlis[0+int(WW2)]
                decoded.append("Sadašnje vrijeme: " + wwlis[0+ww])
                decoded.append("Prošlo vrijeme: " + WWp)
            elif x == "8":
                Nnis = group[1:2]
                Cnis = group[2:3]
                Csred = group[3:4]
                Cvis = group[4:5]
                Nnispos = int(round(int(Nnis) * 10 / 8,0) * 10)
                if Nnis == "9":
                    Nnisprint = "Nisku naoblaku nije moguće odrediti jer se oblaci ne vide."
                elif Cnis == "0" and Csred != "0":
                    Nnisprint = "Srednja naoblaka: " + str(Nnispos) + "%"
                elif Cnis == "0" and Csred == "0":
                    Nnisprint = "Nisu prisutni niski ni srednji oblaci."
                else:
                    Nnisprint = "Niska naoblaka: " + str(Nnispos) + "%"
                decoded.append(Nnisprint)
                if Cnis == "/":
                    Cnp = "nisu vidljivi"
                else:
                    Cnp = clow[0+int(Cnis)]
                decoded.append("Niski oblaci: " + Cnp)
                if Csred == "/":
                    Csp = "nisu vidljivi"
                else:
                    Csp = cmed[0+int(Csred)]
                decoded.append("Srednji oblaci: " + Csp)
                if Cvis == "/":
                    Cvp = "nisu vidljivi"
                else:
                    Cvp = chigh[0+int(Cvis)]
                decoded.append("Visoki oblaci: " + Cvp)
            elif x == "9":
                GG = group[1:3]
                gg = group[3:5]
                decoded.append("Izvještaj predan u: " + GG + ":" + gg + " UTC.")
        elif d == 11:
            x = group[0:1]
            if x == "7":
                ww = int(group[1:3])
                WW1 = group[3:4]
                WW2 = group[4:5]
                wwp = wwlis[0+ww]
                if WW1 == "/" and WW2 == "/":
                    WWp = "nije poznato"
                elif WW1 == "/" and WW2 != "/":
                    WWp = wlis[0+int(WW2)]
                elif WW1 != "/" and WW2 == "/":
                    WWp = wlis[0+int(WW1)]
                elif WW1 == WW2:
                    WWp = wlis[0+int(WW1)]
                else:
                    WWp = wlis[0+int(WW1)] + " i " + wlis[0+int(WW2)]
                decoded.append("Sadašnje vrijeme: " + wwlis[0+ww])
                decoded.append("Prošlo vrijeme: " + WWp)
            elif x == "8":
                Nnis = group[1:2]
                Cnis = group[2:3]
                Csred = group[3:4]
                Cvis = group[4:5]
                Nnispos = int(round(int(Nnis) * 10 / 8,0) * 10)
                if Nnis == "9":
                    Nnisprint = "Nisku naoblaku nije moguće odrediti jer se oblaci ne vide."
                elif Cnis == "0" and Csred != "0":
                    Nnisprint = "Srednja naoblaka: " + str(Nnispos) + "%"
                elif Cnis == "0" and Csred == "0":
                    Nnisprint = "Nisu prisutni niski ni srednji oblaci."
                else:
                    Nnisprint = "Niska naoblaka: " + str(Nnispos) + "%"
                decoded.append(Nnisprint)
                if Cnis == "/":
                    Cnp = "nisu vidljivi"
                else:
                    Cnp = clow[0+int(Cnis)]
                decoded.append("Niski oblaci: " + Cnp)
                if Csred == "/":
                    Csp = "nisu vidljivi"
                else:
                    Csp = cmed[0+int(Csred)]
                decoded.append("Srednji oblaci: " + Csp)
                if Cvis == "/":
                    Cvp = "nisu vidljivi"
                else:
                    Cvp = chigh[0+int(Cvis)]
                decoded.append("Visoki oblaci: " + Cvp)
            elif x == "9":
                GG = group[1:3]
                gg = group[3:5]
                decoded.append("Izvještaj predan u: " + GG + ":" + gg + " UTC.")
        elif d == 12:
            x = group[0:1]
            if x == "8":
                Nnis = group[1:2]
                Cnis = group[2:3]
                Csred = group[3:4]
                Cvis = group[4:5]
                Nnispos = int(round(int(Nnis) * 10 / 8,0) * 10)
                if Nnis == "9":
                    Nnisprint = "Nisku naoblaku nije moguće odrediti jer se oblaci ne vide."
                elif Cnis == "0" and Csred != "0":
                    Nnisprint = "Srednja naoblaka: " + str(Nnispos) + "%"
                elif Cnis == "0" and Csred == "0":
                    Nnisprint = "Nisu prisutni niski ni srednji oblaci."
                else:
                    Nnisprint = "Niska naoblaka: " + str(Nnispos) + "%"
                decoded.append(Nnisprint)
                if Cnis == "/":
                    Cnp = "nisu vidljivi"
                else:
                    Cnp = clow[0+int(Cnis)]
                decoded.append("Niski oblaci: " + Cnp)
                if Csred == "/":
                    Csp = "nisu vidljivi"
                else:
                    Csp = cmed[0+int(Csred)]
                decoded.append("Srednji oblaci: " + Csp)
                if Cvis == "/":
                    Cvp = "nisu vidljivi"
                else:
                    Cvp = chigh[0+int(Cvis)]
                decoded.append("Visoki oblaci: " + Cvp)
            elif x == "9":
                GG = group[1:3]
                gg = group[3:5]
                decoded.append("Izvještaj predan u: " + GG + ":" + gg + " UTC.")
        elif d == 13:
            x = group[0:1]
            if x =="9":
                GG = group[1:3]
                gg = group[3:5]
                decoded.append("Izvještaj predan u: " + GG + ":" + gg + " UTC.")

        d += 1
        continue
        
    len333 = len(synop333) #check length of synop333
    
    if len333 > 0: #if there are elements in synop333 start decodind third section of synop report
        for e in range (0, len333):
            group333 = synop333[e]
            a = group333[0:1] #group indicator
            if a == "1": #max air temperature during day
                txs = group333[1:2]
                txtx = group333[2:5] 
                if txtx == "///":
                    decoded333.append("Maksimalna dnevna temperatura zraka nije poznata.")
                else: 
                    if txs == "1":
                        TX = float(txtx) / -10
                    else:
                        TX = float(txtx) / 10
                    decoded333.append("Maksimalna dnevna temperatura zraka: " + str(TX) + "°C")
            elif a == "2": #min air temperature during night
                tns = group333[1:2]
                tntn = group333[2:5]
                if tntn == "///":
                    decoded333.append("Minimalna jutarnja temperatura zraka nije poznata.")
                else: 
                    if tns == "1":
                        TN = float(tntn) / -10
                    else:
                        TN = float(tntn) / 10
                    decoded333.append("Minimalna jutarnja temperatura zraka: " + str(TN) + "°C")
            elif a == "3":
                E = group333[1:2]
                t5s = group333[2:3]
                tn5r = group333[3:5]
                if E == "/": #soil condition without snow or ice
                    Eprint = "nije poznato"
                else:
                    Eint = int(E)
                    Eprint = Ens[Eint]
                decoded333.append("Stanje tla bez snijega i leda: " + Eprint)
                if t5s == "/" or tn5r == "//": #minimum air temperature 5 cm abow soil
                    TN5 = "nije poznata"
                else:
                    if t5s == "1":
                        TN5 = str(int(tn5r) / -1) + "°C"
                    else:
                        TN5 = str(int(tn5r)) + "°C"
                decoded333.append("Minimalna temperatura zraka 5 cm iznad tla: " + TN5)
            elif a == "4":
                Es = group333[1:2]
                snow = group333[2:5]
                if Es == "/": #snow condition with snow or ice
                    Esprint = "nije poznato"
                else:
                    Esint = int(Es)
                    Esprint = Ews[Esint]
                decoded333.append("Stanje tla sa snijegom i ledom: " + Esprint)
                if snow == "///":
                   decoded333.append("Visina snježnog pokrivača nije poznata.")
                elif snow == "999": #hight of snow cover
                    decoded333.append("Visinu snježnog pokrivača nije moguće izmeriti.")
                elif snow == "998":
                    decoded333.append("Snježni pokrivač je u krpama.")
                else:
                    if snow == "997":
                        snowprint = "< 0.5"
                    else:
                        snowprint = int(snow)
                    decoded333.append("Visina snježnog pokrivača: " + str(snowprint) + " cm")
            elif a == "5":
                pass
            elif a == "6":
                pass
            elif a == "7": #precipitation during last 24 hours
                RRRR = group333[1:5]
                if RRRR == "0000":
                    rainprint = "0 mm (nije bilo oborine)"
                elif RRRR == "9999":
                    rainprint = "0 mm (oborina u tragovima)"
                else:
                    Rf = float(RRRR) / 10
                    rainprint = str(Rf) + " mm"
                decoded333.append("Količina oborine u posljednjih 24 sata: " + rainprint)
            elif a == "8":
                pass
            elif a == "9":
                xx = group333[1:3]
                if xx == "11": #speed of max wind gust
                    fxfx = group333[3:5]
                    vjind = decoded[1]
                    if vjind == "0" or vjind == "1": #decode wind speed unit indicator to wind speed unit
                        vjindp = "m/s"
                    elif vjind == "3" or vjind == "4":
                        vjindp = "kt"
                    decoded333.append("Maksimalni udar vjetra: " + fxfx + " " + vjindp)
                elif xx == "15": #azimuth of max wind gust
                    dxdx = group333[3:5]
                    if dxdx == "35" or dxdx == "36" or dxdx == "01": #wind direction from asimut to directon
                        vjetxprint = "N"
                    if dxdx == "02" or dxdx == "03":
                        vjetxprint = "NNE"
                    if dxdx == "04" or dxdx == "05":
                        vjetxprint = "NE"
                    if dxdx == "06" or dxdx == "07":
                        vjetxprint = "ENE"
                    elif dxdx == "08" or dxdx == "09" or dxdx == "10":
                        vjetxprint = "E"
                    if dxdx == "11" or dxdx == "12":
                        vjetxprint = "ESE"
                    if dxdx == "13" or dxdx == "14":
                        vjetxprint = "SE"
                    if dxdx == "15" or dxdx == "16":
                        vjetxprint = "SSE"
                    elif dxdx == "17" or dxdx == "18" or dxdx == "19":
                        vjetxprint = "S"
                    if dxdx == "20" or dxdx == "21":
                        vjetxprint = "SSW"
                    if dxdx == "22" or dxdx == "23":
                        vjetxprint = "SW"
                    if dxdx == "24" or dxdx == "25":
                        vjetxprint = "WSW"
                    elif dxdx == "26" or dxdx == "27" or dxdx == "28":
                        vjetxprint = "W"
                    if dxdx == "29" or dxdx == "30":
                        vjetxprint = "WNW"
                    if dxdx == "31" or dxdx == "32":
                        vjetxprint = "NW"
                    if dxdx == "33" or dxdx == "34":
                        vjetxprint = "NNW"
                    decoded333.append("Smjer maksimalnog udara vjetra: " + vjetxprint)
                elif xx == "23": #sea condition
                    pass
                elif xx == "24":
                    pass
                elif xx == "31": #new snow
                    snownew = int(group333[3:5])
                    decoded333.append("Visina novog snijega: " + str(snownew) + " cm.")
                elif xx == "50": #clouds on mountian
                    pass
                elif xx == "51": #clouds and fog below station level
                    pass
                elif xx == "58": 
                    pass
                elif xx == "60":
                    pass
                elif xx == "66":
                    pass
            
            continue
    
    decl = len(decoded) #length of decoded

    iteration = 0

    while iteration < decl:
        if iteration == 1:
            report.write(" ")
            report.write("\n")
            report.write("###")
            report.write("\n")
            report.write(" ")
            report.write("\n")
        elif iteration == 2:
            report.write(decoded[2])
            report.write("\n")
        elif iteration == 5:
            report.write(decoded[5])
            report.write("\n")
        elif iteration == 6:
            report.write(decoded[6])
            report.write("\n")
        elif iteration == 7:
            report.write(decoded[7])
            report.write("\n")
        elif iteration == 8:
            report.write(decoded[8])
            report.write("\n")
        elif iteration == 9:
            report.write("Temperatura zraka: " + str(decoded[9]) + "°C")
            report.write("\n")
        elif iteration == 10:
            report.write("Temperatura rosišta: " + str(decoded[10]) + "°C")
            report.write("\n")
        elif iteration == 11:
            report.write(decoded[11])
            report.write("\n")
        elif iteration == 12:
            report.write(decoded[12])
            report.write("\n")
        elif iteration == 13:
            report.write(decoded[13])
            report.write("\n")
        elif iteration == 14:
            report.write(decoded[14])
            report.write("\n")
        elif iteration == 15:
            report.write(decoded[15])
            report.write("\n")
        elif iteration == 16:
            report.write(decoded[16])
            report.write("\n")
        elif iteration == 17:
            report.write(decoded[17])
            report.write("\n")
        elif iteration == 18:
            report.write(decoded[18])
            report.write("\n")
        elif iteration == 19:
            report.write(decoded[19])
            report.write("\n")
        elif iteration == 20:
            report.write(decoded[20])
            report.write("\n")
        elif iteration == 21:
            report.write(decoded[21])
            report.write("\n")
        elif iteration == 22:
            report.write(decoded[22])
            report.write("\n")
        elif iteration == 23:
            report.write(decoded[23])
            report.write("\n")
        
        iteration += 1
        continue
    if len(decoded333) > 0:
        for i333 in range (0, len(decoded333)):
            report.write(decoded333[i333])
            report.write("\n")

#    print (synoplist)
#    print (synlen)
#    print (decoded)
#    print (synop222)
#    print (decoded222)
#    print (synop333)
#    print (decoded333)
#    print (" ")
    synop333.clear()
    decoded.clear()
    decoded333.clear()
    
    c += 1
    continue

sys.exit (0)

