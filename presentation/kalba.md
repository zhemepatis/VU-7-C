### Aktualumas

Dirbtiniai neuroniniai tinklai pastaruoju metu įgyja vis didesnį populiarumą dėl gebėjimo modeliuoti sudėtingus netiesinius ryšius. Šio mašininio mokymosi metodo modeliai yra naudojami objektų atpažinimo paveikslėliuose, natūraliosios kalbos apdorojimo, medicininės diagnostikos ir kitose srityse. Juo labiau skaičiavimo galios augimas bei didelių duomenų centrų vystymasis ir didėjantis jų prieinamumas taip pat skatina šios srities tobulėjimą. 

Nepaisant šių pasiekimų, dirbtinių neuroninių tinklų efektyvumas priklauso ne tik nuo modelio architektūros ar duomenų kiekio, bet ir nuo taikomų mokymo strategijų. Viena iš jų - triukšmo įterpimas mokymo metu. Tyrimai rodo, kad ši modelio apmokymo strategija leidžia pagerinti modelio atsparumą triukšmui ir apibendrinimo gebėjimus. Šios modelių savybės yra ypatingai svarbios kalbant apie modelių pritaikomumą realiuose uždaviniuose, kur duomenys dažnai yra netikslūs.

### DNT rezultatai

su švaria duomenų aibe:
* didžiąja dalimi, modelio daromos absoliutinės paklaidos vid. ir std. nuokrypio dydžiai, didinant taškų kiekį, mažėjo 
* visiems vid. mažėjimo atvejais jis sumažėjo daugmaž vienodai
* std. nuokrypis nepasižymi tom pačiom savybėm - sumažėjimo didumas svyravo kiek daugiau

su triukšminga duomenų aibe:
* kiek kitokie rezultatai - vid. didžiąją dalį atvejųb mažėjo, o std. nuokrypis mažėjo stabiliai
* abiejų rodiklių pamažėjimas, didinant duomenų aibę, kito nevienodai

triukšmo įtaka:
* nepastebėtas joks dėsningumas
* abiejų rodiklių pablogėjimas didinant duomenų aibę stipriai svyravo

### NN rezultatai
su švaria duomenų aibe:
* tiek vid., tiek standartinis nuokrypis nuosekliai mažėja
* vid. reikšmių pokytis didinant duomenų aibę yra vienodas
* std. nuokrypio atveju tendencija panaši, tačiau rodiklio sumažėjimas kiek labiau svyruoja

su triukšminga duomenų aibe:
* tiek vid., tiek standartinis nuokrypis nuosekliai mažėja
* didėjant duomenų aibei, vid. pokytis buvo vis mažesnis
* std. nuokrypio reikšmės šio dėsningumo neparodė, tačiau didžiausias ir mažiausias rodiklio pokytis buvo panašus, kaip vid.

### KNN rezultatai
su švaria duomenų aibe:
* abu rodikliai nuosekliai mažėja
* vid. rodiklio pokytis yra daugmaž vienodas
* std. nuokrypio atveju pokytis yra kiek didesnis

su triukšminga duomenų aibe:
* abu rodikliai nuosekliai mažėja
* vid. pokytis, didinant duomenų aibę, svyravo kiek daugiau nei su švaria duomenų aibe, bet išliko pakankamai stabilus
* std. nuokrypis pasižymėjo panašiomis tendencijomis, bei tuo, kad didėjant duomenų aibei pokytis buvo vis mažesnis


### NN + KNN triukšmo įtaka
triukšmo įtaka:
* abiem atvejais buvo pastebėta, kad vid. reikšmės prastėjo vis labiau didinant duomenų aibę
* std. nuokrypis tuo nepasižymėjo, tačiau pablogėjimo dydžiai svyravo labai panašiai