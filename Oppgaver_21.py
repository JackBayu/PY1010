#%% Informasjon

"""
Oppgåve 2.1 Python som kalkulator

Oppgåve: Forbrukslån og rente 

Student: Jackson Bayubahe

Forfall: 2026-09-08
"""

#%% Data

L = 100000     # (Fobrukslån, kr-kroner)

r = 23.4/100   # (Rentesats, %-prosent pr. år)

mnd = 12       # (md-månadar i eitt år)

#%% Resultat

R = (L * r) / mnd # (Rente pr. månad = 1 950 kr)
print(R)

