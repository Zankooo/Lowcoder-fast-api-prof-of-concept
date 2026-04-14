# To je FastAPI (backend) namenjen za prof of concept za Lowcoder (frontend)

## Povzetek
To je repozitorij, ki je namenjen kot backend projekt za frontend ki je v Lowcoderju. Torej v Lowcoderju pridobimo informacije oziroma podatke od uporabnika, jih potem pošljemo na backend in jih procesiramo. Nato procesiranje podatke pošljemo spet nazaj na frontend kjer jih tudi prikažemo.

## Nastavitev za delovanje lokalno (MacOS)
- Na samem zacetku mores inicializirati python .venv environment - okolje v root mapi:
```python3 -m venv .venv```

- Aktiviraš python environment v root mapi:
```source .venv/bin/activate```

- Potem instaliraš vse requirementse iz mape iz root mape:
```pip install -r requirements.txt```

- Komanda s katero laufaš program iz root mape (kjer je ta README):
```uvicorn app.main:app --reload```

- Če ne dela je zelo verjetno problem z porti!

## Nastavitev za delovanje v Dockerju 
- Zgraditi image:
``` docker build -t fast-api-backend .```

- Nato image zaženeš z:
``` docker run -p 8080:80 fast-api-backend ```


## Use case (primeri uporabe)
Narejeno za naslednje 4 primere uporabe (usecase) -> predvideva se da so takšni tipi primerov uporabe najpogostejši:

- **prof of concept 1:** _Forma vpis podatkov uporabnika_ -> Uporabnik vpiše v formo svoje podatke (ime, telefonska številka in rojstni datum) in te podatki se zapišejo v datoteko "uporabniki.json" ki se nahaja na backendu.

- **prof of concept 2**:  _Izpis podatkov; iz baze recimo (v tem primeru json iz forme)_ -> Vse uporabnike (vnešene z formo) oziroma drugače, ve iz mape datoteke "uporabniki.json" prikažemo.

- **prof of concept 3**:  _Upload XML datotek, procesiranje in izpis rezultata_ -> Imamo 3 XML datoteke in vsaka ima sledečo obliko:
    ```
    <uporabnik>
        <telefonska_stevilka>041123456</telefonska_stevilka>
    </uporabnik>
    ```
    Razlikujejo le v telefonski številki. Vse tri naložimo (upload), jih pošljemo na backend kjer se iz XML-jev ven "poberejo" le telefonske številke. Se zapišejo v datoteko "telefonske_cifre.json" in se nato pođlje na frontend le izpis telefonskih številk.
    

- **prof of concept 4**:  _Upload XLSX datotek, procesiranje in izpis rezultata_ -> Podobno kot pri XML, vendar da imamo tokrat 3 XLSX datoteke. In takšenga formata:

    | Name | Phone | Birthday |
    |------|-------|----------|
    | Ana Novak | 031555101 | 1984-03-16 |
    | Marko Kranjc | 040777202 | 1991-07-22 |
    | Nina Zupan | 041888303 | 1988-11-05 |
    | Luka Horvat | 051666404 | 1995-01-19 |
    | Sara Mlakar | 070444505 | 1982-09-30 |
    | Tina Bizjak | 068123606 | 1990-12-14 |
    | Žan Potočnik | 030890707 | 1987-05-08 |
    | Eva Kovač | 041234808 | 1993-08-27 |
    | Maja Vidmar | 040345909 | 1986-02-11 |
    | Rok Kos | 031456010 | 1998-06-03 |

    Na frontendu naložimo (upload) 3 takšne XML, pošljemo na backend kjer se zgodi procesiranje in vse skupaj se nazaj pošlje na frontend le 
    imena in njihove telefonske številke. 
    
## Izzivi in problemi
Največ izzivov in problemov sem imel, oziroma nastane na strani Lowcoderja ko je potrebno pošiljati datoteke na backend. (XML,XLSX,CSV). Namreč pri navadnem programiranju oziroma če uporabljaš http client Postman, lahko brez problema pošiljaš na backend datoteke: 

Body -> form-data -> file -> naložiš in pošlješ na backend. 

Tukaj nastane težava ker Lowcoder zgleda ne podpira takšnega delovanja, ampak vsako uploadanje datotek pretvori v Base64 string. Kar pomeni da pošiljaš v omenjenem formatu na backend in je potem na backendu potrebno datoteke ponovno pretvoriti v bolj berljiv format da uspešno procesiraš. 




