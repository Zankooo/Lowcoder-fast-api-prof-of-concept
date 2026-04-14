# Uporabimo uradno Python sliko
FROM python:3.14-slim

# Nastavimo delovni direktorij znotraj kontejnerja
WORKDIR /app

# Najprej kopiramo requirements.txt, da izkoristimo Docker cache
COPY requirements.txt .

# Namestimo odvisnosti
RUN pip install --no-cache-dir -r requirements.txt

# Kopiramo preostalo kodo aplikacije (app mapo in vse ostalo)
COPY . .

# Poskrbimo, da mapa za podatke obstaja
RUN mkdir -p podatki

# Odpremo vrata 80
EXPOSE 80

# Zaženemo aplikacijo s pomočjo uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]