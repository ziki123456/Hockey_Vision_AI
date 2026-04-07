# HockeyVision

HockeyVision je školní software projekt zaměřený na rozpoznávání hokeje a hokejových situací z obrázků pomocí strojového učení. Uživatel nahraje obrázek do webové aplikace a systém nejdřív určí, jestli je na něm hokej nebo není hokej. Pokud je na obrázku hokej, druhý model určí konkrétní hokejovou situaci.

## Spuštění bez IDE

Projekt je možné spustit bez IDE pouze přes příkazový řádek nebo PowerShell.

### 1. Otevření projektu
Otevřete příkazový řádek nebo PowerShell ve složce projektu.

### 2. Vytvoření virtuálního prostředí
```bash
py -3.13 -m venv .venv
```

### 3. Aktivace virtuálního prostředí

PowerShell:
```bash
.\.venv\Scripts\Activate.ps1
```

Příkazový řádek:
```bash
.\.venv\Scripts\activate.bat
```

### 4. Instalace knihoven
```bash
python -m pip install -r requirements.txt
```

### 5. Kontrola modelů
Ve složce `model` musí být tyto soubory:

- `binary_hockey_model.keras`
- `hockey_situations_model.keras`

### 6. Spuštění aplikace
```bash
python app.py
```

### 7. Otevření webu
Po spuštění otevřete v prohlížeči:

```text
http://127.0.0.1:5000
```

---

## Účel projektu

Cílem projektu je vytvořit systém, který bude z jednoho obrázku umět:

1. určit, jestli je na obrázku hokej nebo není hokej
2. pokud je na obrázku hokej, určit konkrétní hokejovou situaci

Projekt má reálné využití například pro:

- automatické třídění fotografií ze zápasu
- základ pro budoucí řízení kamery na hokejových zápasech
- pomocné zpracování záznamů a snímků pro konkrétní tým

---

## Jak projekt funguje

Projekt používá dva samostatné modely strojového učení.

### 1. Binární model
První model rozhoduje mezi dvěma třídami:

- `HOKEJ`
- `NENI_HOKEJ`

Tento model slouží jako první filtr.

### 2. Situační model
Druhý model se použije jen tehdy, když první model určí, že je na obrázku hokej. Potom určuje jednu z těchto pěti situací:

- `VHAZOVANI`
- `SOUBOJ_U_MANTINELU`
- `JIZDA_S_PUKEM`
- `ZAKROK_BRANKARE`
- `KLIDOVA_SITUACE`

---

## Použité technologie

Projekt je vytvořen v jazyce Python a používá tyto hlavní technologie:

- Flask
- TensorFlow
- Keras
- Pillow
- NumPy
- HTML
- CSS
- JavaScript

### K čemu byly použity
- **Flask** slouží pro webovou aplikaci
- **TensorFlow a Keras** slouží pro načítání a používání modelů strojového učení
- **Pillow** slouží pro načítání a úpravu obrázků
- **NumPy** slouží pro práci s obrazovými daty
- **HTML CSS a JavaScript** slouží pro uživatelské rozhraní

---

## Architektura projektu

Projekt je rozdělen na dvě části:

### 1. Trénování modelů
Probíhá v Google Colab notebooku.

Notebooky obsahují:
- načtení dat
- kontrolu dat
- přípravu datasetu
- rozdělení dat
- trénování modelů
- vyhodnocení výsledků
- uložení modelů do `.keras`

### 2. Použití modelů
Probíhá v lokální Flask aplikaci.

Aplikace:
- přijme obrázek od uživatele
- zavolá binární model
- případně zavolá situační model
- vrátí výsledek do webového rozhraní

---

## Struktura projektu

```text
Hockey_Vision_AI/
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
├── DATA_COLLECTION.md
├── MODEL_INFO.md
├── TESTING.md
│
├── model/
│   ├── binary_hockey_model.keras
│   └── hockey_situations_model.keras
│
├── notebooks/
│   ├── HockeyVision_binary_model.ipynb
│   └── HockeyVision_situation_model.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── main.js
│
├── uploads/
│
└── .gitignore
```

---

## Vstup a výstup programu

### Vstup
- obrázek ve formátu png jpg jpeg nebo webp

### Výstup
- binární výsledek `HOKEJ` nebo `NENI_HOKEJ`
- pokud je výsledek `HOKEJ`, navíc i konkrétní hokejová situace

---

## Model strojového učení

V projektu byly použity dva modely klasifikace obrázků založené na konvoluční neuronové síti.

Jako základ byl použit přístup **transfer learning** s modelem **MobileNetV2**.

### Proč byl zvolen MobileNetV2
- je vhodný pro klasifikaci obrázků
- je relativně lehký a rychlý
- funguje dobře i na menším nebo středním datasetu
- je vhodný pro školní projekt
- je dobře obhajitelný

### Parametry modelů
- velikost obrázků: `224 x 224`
- trénování v Google Colab
- ukládání modelů do formátu `.keras`

---

## Předzpracování dat

Před trénováním proběhlo předzpracování dat.

Použité kroky:
- ruční třídění obrázků do tříd
- sjednocení vstupu na velikost `224 x 224`
- rozdělení dat na trénovací a validační část
- lehká augmentace dat při trénování
- převod obrázků do formátu vhodného pro MobileNetV2

### Použitá augmentace
- horizontální otočení
- malé pootočení
- malé přiblížení nebo oddálení

Cílem bylo zlepšit schopnost modelu reagovat i na podobné obrázky z trochu jiného úhlu nebo kompozice.

---

## Data a jejich původ

Data použitá pro model byla vytvořena z reálných a pravdivých obrazových dat. Nejde o hotový veřejný dataset.

### Původ dat
- vlastní ručně vybrané obrázky
- vlastní snímky získané ze záznamů hokejových zápasů
- vlastní ruční třídění obrázků do kategorií

### Důležité
- nebyl použit žádný hotový předpřipravený dataset
- data byla ručně sesbírána a roztříděna
- k projektu je potřeba doložit způsob získání dat a jejich původ v samostatné dokumentaci

---

## Kategorie situačního modelu

Situační model rozlišuje těchto 5 tříd:

### Vhazovani
Situace, kdy dochází k vhazování puku a hráči jsou připraveni proti sobě.

### Souboj u mantinelu
Situace, kdy hráči bojují o puk v těsné blízkosti u sebe.

### Jizda s pukem
Běžná aktivní hra, kdy hráč vede puk a nejde o souboj ani zákrok brankáře.

### Zakrok brankare
Situace, kdy je hlavním prvkem zákrok nebo obranná akce brankáře.

### Klidova situace
Situace, kdy se hra aktivně nerozvíjí a hráči spíše stojí nebo čekají.

---

## Výsledky modelů

### Binární model
Binární model dosáhl velmi vysoké validační přesnosti a při testování na nových obrázcích správně rozlišoval hokej a není hokej.

### Situační model
Situační model dosáhl přibližně validační přesnosti kolem 75 %. To je vzhledem k obtížnosti pěti podobných tříd rozumný a použitelný výsledek pro školní projekt.

### Interpretace výsledků
- binární model je silná část systému
- situační model je obtížnější část systému
- projekt i tak vykazuje reálnou a užitečnou klasifikaci

---

## Ovládání aplikace

1. spusťte aplikaci
2. otevřete webovou stránku v prohlížeči
3. nahrajte obrázek
4. klikněte na tlačítko pro vyhodnocení
5. aplikace vrátí výsledek

### Možné výsledky
- `NENI_HOKEJ`
- `JIZDA_S_PUKEM`
- `KLIDOVA_SITUACE`
- `SOUBOJ_U_MANTINELU`
- `VHAZOVANI`
- `ZAKROK_BRANKARE`

---

## Jak byl projekt testován

Projekt byl testován:
- v Google Colab během trénování modelů
- lokálně v Pythonu samostatnou predikcí na testovacích obrázcích
- lokálně přes Flask webovou aplikaci

Bylo ověřeno:
- načtení obou modelů
- správná predikce hokej nebo není hokej
- správná predikce situace u hokejových obrázků
- fungování webového rozhraní

---

## Omezení projektu

Projekt má několik omezení:

- modely nejsou určeny pro video v reálném čase
- přesnost může být nižší na úplně odlišných obrázcích než na těch, na kterých byl model trénován
- situační model je obtížnější než binární model
- některé situace se mohou vizuálně podobat

Tato omezení jsou u školního projektu očekávatelná a budou dále řešitelná rozšířením datasetu a dalším trénováním.

---

## Co je autorský a co cizí kód

### Autorský kód
Za autorský kód je považováno hlavně:
- návrh projektu
- datová struktura
- logika aplikace
- logika predikce
- propojení modelů s webem
- příprava a třídění dat
- trénovací notebooky
- backend a frontend aplikace

### Kód třetích stran
Za kód třetích stran jsou považovány:
- knihovny Flask
- TensorFlow
- Keras
- Pillow
- NumPy
- další nainstalované balíčky z `requirements.txt`

Tyto knihovny nejsou součástí autorského kódu a jsou oddělené formou externích balíčků instalovaných přes `requirements.txt`.

---

## Soubory důležité pro odevzdání

Pro odevzdání a obhajobu je důležité přiložit:

- zdrojový kód projektu
- `README.md`
- `requirements.txt`
- oba `.keras` modely
- Google Colab notebook pro binární model
- Google Colab notebook pro situační model
- dokumentaci k původu dat
- dokumentaci k návrhu a postupu tvorby
- dokumentaci k testování

---

## Doporučený postup při obhajobě

Při obhajobě je vhodné ukázat:

1. proč byl projekt vytvořen
2. jaký má reálný smysl
3. jak vznikal dataset
4. jak probíhalo předzpracování dat
5. proč byly zvoleny právě tyto třídy
6. proč jsou použity dva modely
7. jak funguje webová aplikace
8. jak se projekt spouští bez IDE
9. jaké má projekt limity a možné další rozšíření

---

## Možné další rozšíření

- větší dataset
- přesnější situační model
- zpracování videa místo jednoho obrázku
- automatické ukládání a třídění výsledků
- základ pro budoucí řízení kamery podle situace na ledě

---

## Autor

Projekt vytvořen jako vlastní školní software projekt do předmětu PV.