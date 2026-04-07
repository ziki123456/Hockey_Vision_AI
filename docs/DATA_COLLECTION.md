# DATA_COLLECTION

## Jaká data projekt používá

Projekt HockeyVision používá obrazová data, tedy fotografie a snímky obrázků.

Na obrázcích je buď:
- hokej
- nebo není hokej

Pokud je na obrázku hokej, data jsou dále ručně rozdělená podle konkrétní hokejové situace.

## Původ dat

Data nejsou převzatá jako hotový předpřipravený dataset.  
Obrázky byly získávány vlastním sběrem, vlastním výběrem a vlastním ručním tříděním.

Použité zdroje:
- vlastní ručně vybrané obrázky
- vlastní snímky získané ze záznamů hokejových zápasů
- vlastní ruční třídění do kategorií

Cílem bylo používat pouze reálná a pravdivá data.

## Jak probíhal sběr dat

Při sběru dat byl použit tento postup:

1. vybrat vhodný reálný obrázek
2. rozhodnout, jestli odpovídá některé třídě
3. uložit obrázek do správné složky
4. zkontrolovat, že není duplicitní nebo výrazně poškozený
5. průběžně dataset rozšiřovat a kontrolovat

Data byla sbírána tak, aby odpovídala reálnému použití projektu, tedy rozpoznávání hokeje a konkrétních hokejových situací z obrázků.

## Struktura datasetu

Finální dataset byl připraven v této struktuře:

- `neni_hokej`
- `vhazovani`
- `souboj_u_mantinelu`
- `jizda_s_pukem`
- `zakrok_brankare`
- `klidova_situace`

Tato struktura byla zvolená proto, aby bylo možné z jednoho datasetu vytvořit:

- binární model `hokej / neni_hokej`
- situační model pro 5 hokejových situací

## Binární část datasetu

Pro binární model se používají dvě výsledné třídy:

- `hokej`
- `neni_hokej`

Třída `hokej` vzniká sloučením těchto pěti složek:

- `vhazovani`
- `souboj_u_mantinelu`
- `jizda_s_pukem`
- `zakrok_brankare`
- `klidova_situace`

Třída `neni_hokej` zůstává samostatně.

Tato část slouží jako první filtr systému.

## Situační část datasetu

Pro druhý model se používají pouze hokejové obrázky a rozdělení do 5 tříd:

- `vhazovani`
- `souboj_u_mantinelu`
- `jizda_s_pukem`
- `zakrok_brankare`
- `klidova_situace`

Tato část slouží pro určení konkrétní hokejové situace.

## Kontrola kvality dat

Při přípravě datasetu bylo důležité:

- kontrolovat správné zařazení obrázků
- vyřazovat rozmazané nebo nepoužitelné snímky
- nepoužívat stejné obrázky vícekrát
- hlídat rozumnou vyváženost tříd
- vybírat obrázky z více různých zápasů a situací

Cílem bylo, aby se model neučil jen jeden konkrétní stadion nebo jednu konkrétní scénu, ale obecnější obrazové vzory.

## Předzpracování dat

Před trénováním modelů proběhlo předzpracování dat:

- kontrola složek a názvů tříd
- sjednocení vstupní velikosti obrázků při načítání na `224 x 224`
- rozdělení dat na trénovací a validační část
- lehká augmentace dat při trénování
- převod dat do formátu vhodného pro MobileNetV2

Předzpracování probíhalo v Google Colab notebooku.

## Splnění zadání

Projekt používá reálná data, která byla vlastním způsobem získána, vybrána a ručně roztříděna.  
Nebyl použit žádný hotový předpřipravený dataset a data nejsou vytvořená simulací.

Cílem finální verze projektu je mít dataset, který odpovídá požadavkům zadání a je obhajitelný jako vlastní reálná datová základna projektu.