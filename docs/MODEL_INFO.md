# MODEL_INFO

## Název projektu

HockeyVision

## Cíl modelu

Cílem projektu je rozpoznávání hokeje a hokejových situací z obrázků pomocí strojového učení.

Projekt používá dva modely:

1. binární model  
   - určuje, jestli je na obrázku hokej nebo není hokej

2. situační model  
   - pokud je na obrázku hokej, určuje konkrétní hokejovou situaci

## Proč jsou použity dva modely

Bylo zvoleno dvoustupňové řešení, protože je logické a dobře obhajitelné.

Výhody:
- první model řeší jednodušší problém
- druhý model se používá jen u hokejových obrázků
- systém je přehlednější
- webová aplikace se pak snadno propojí s oběma modely

## Typ modelu

Pro oba modely byl použit přístup klasifikace obrázků pomocí konvoluční neuronové sítě.

Jako základ byl použit:
- `MobileNetV2`

Model byl použit přes transfer learning.

## Proč byl zvolen MobileNetV2

MobileNetV2 byl zvolen proto, že:

- je vhodný pro klasifikaci obrázků
- je lehčí a rychlejší než některé jiné modely
- je dobře použitelný i na menším nebo středním datasetu
- je vhodný pro školní projekt
- je rozumný z hlediska kvality i složitosti

## Použité knihovny

Při tvorbě modelů byly použity hlavně tyto knihovny:

- TensorFlow
- Keras
- NumPy
- Pillow
- standardní knihovny Pythonu pro práci se soubory

## Binární model

### Úkol
Určit:
- `HOKEJ`
- `NENI_HOKEJ`

### Vstup
- obrázek převedený na velikost `224 x 224`

### Výstup
- jedna binární predikce

### Ztrátová funkce
- `binary_crossentropy`

### Metrika
- `accuracy`

## Situační model

### Úkol
Určit jednu z těchto tříd:

- `JIZDA_S_PUKEM`
- `KLIDOVA_SITUACE`
- `SOUBOJ_U_MANTINELU`
- `VHAZOVANI`
- `ZAKROK_BRANKARE`

### Vstup
- obrázek převedený na velikost `224 x 224`

### Výstup
- pravděpodobnosti pro 5 tříd
- výsledná třída s nejvyšší pravděpodobností

### Ztrátová funkce
- `categorical_crossentropy`

### Metrika
- `accuracy`

## Trénování modelu

Modely byly trénovány v Google Colab notebooku.

Při trénování bylo použito:
- načítání dat ze složek
- rozdělení dat na trénovací a validační část
- data augmentation
- Adam optimizer
- EarlyStopping
- ModelCheckpoint

## Předzpracování vstupu

Při načítání obrázků byly použity tyto kroky:

- převod na RGB
- změna velikosti na `224 x 224`
- rozdělení na trénovací a validační data
- augmentace při trénování
- předzpracování odpovídající modelu MobileNetV2

## Výsledné modely

Výsledkem jsou dva soubory:

- `binary_hockey_model.keras`
- `hockey_situations_model.keras`

Tyto modely jsou následně načítány ve Flask aplikaci.

## Použití v aplikaci

Aplikace funguje takto:

1. uživatel nahraje obrázek
2. binární model určí, jestli jde o hokej
3. pokud ano, situační model určí konkrétní hokejovou situaci
4. výsledek se zobrazí ve webové aplikaci

## Shrnutí

Modelová část projektu je založená na dvou samostatných klasifikačních modelech.  
Toto řešení je přehledné, technicky správné a odpovídá cíli projektu i požadavkům zadání.