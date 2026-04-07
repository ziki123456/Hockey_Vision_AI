# TESTING

## Cíl testování

Cílem testování bylo ověřit, že projekt funguje správně po datové, modelové i aplikační stránce.

Bylo potřeba ověřit hlavně:

- že se správně načítají data
- že se modely úspěšně natrénují
- že se uložené modely dají znovu načíst
- že predikce funguje i na nových obrázcích
- že webová aplikace vrací správný výsledek

## Testování binárního modelu

Binární model byl testován:

- během trénování v Google Colab
- pomocí validačních dat
- pomocí nových testovacích obrázků mimo dataset
- lokálně v Pythonu
- lokálně přes webovou aplikaci

### Výsledek
Binární model dosáhl velmi vysoké validační přesnosti a při testování na nových obrázcích správně rozlišoval hokej a není hokej.

## Testování situačního modelu

Situační model byl testován:

- během trénování v Google Colab
- pomocí validačních dat
- lokálně po načtení do aplikace
- přes webové rozhraní s hokejovými obrázky

### Výsledek
Situační model dosáhl přibližně validační přesnosti kolem 75 %.  
To je vzhledem k podobnosti tříd rozumný výsledek a model dává smysluplné výstupy.

## Testování webové aplikace

Bylo ověřeno:

- spuštění aplikace bez IDE
- načtení obou `.keras` modelů
- nahrání obrázku přes webové rozhraní
- vrácení výsledku binární klasifikace
- vrácení výsledku situační klasifikace u hokejových obrázků

## Testované scénáře

Byly testovány například tyto situace:

1. nehokejový obrázek  
   - očekávaný výsledek: `NENI_HOKEJ`

2. hokejový obrázek  
   - očekávaný výsledek: `HOKEJ`

3. hokejový obrázek se situací  
   - očekávaný výsledek: konkrétní třída situačního modelu

4. nepovolený formát souboru  
   - očekávaný výsledek: chybová hláška

5. prázdné odeslání bez obrázku  
   - očekávaný výsledek: chybová hláška

## Závěr testování

Testování ukázalo, že:

- projekt je spustitelný
- modely se správně načítají
- binární klasifikace funguje velmi dobře
- situační klasifikace funguje použitelně a dává smysl
- webová aplikace je schopná vracet výsledky uživateli

Projekt byl otestován jako funkční prototyp splňující hlavní cíl práce.