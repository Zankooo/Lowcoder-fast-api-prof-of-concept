# To je fast api namenjen za prof of concept za lowcoder.


- Na samem zacetku mores inicializirati python .venv environment:
```python3 -m venv .venv```

- Potem instaliras vse requirementse iz mape:
```pip install -r requirements.txt```

- Komanda s katero laufaš program:
``` uvicorn main:app --reload```

- Če komanda ne dela, verjetno ne dela ker okolje .venv ni aktivirano. To nardiš:
```source .venv/bin/activate```







----
Zakaj moramo aktivirati okolje?
- izolacija podatkov -> vsak projekt uporablja različne knjižnice, en projekt vsebuje starejši fastapi drug mlajši... in če bi vse instaliral sistemsko bi prihajalo do sporov
- k das ukaz "source .venv/bin/activate" poves terminalu da naj ne isce sistemskega ampak titega ki je v nasi mapi .venv
- sistemski python je sumljiv, ker ga macos uporablja za svoja sistemska opravila. .venv je pa varen peskovnik kjer lahko eksperimentiras.

