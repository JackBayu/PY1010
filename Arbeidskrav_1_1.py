#%% Informasjon

"""
Arbeidskrav 1

Oppgåve: Årleg totalkostnadar for el-bil og for bensinbil, samt årleg kostnadsdiforsikring_elbilranse.

Student: Jackson Bayubahe

Forfall: 2026-09-01
test git
test 
"""

#%% Data Elbil
forsikring_elbil = 5000  # (kr/år, forsikring el-bil)
forbruk_elbil    = 0.2   # (kWh/km, forbruk)
netleige_elbil   = 2     # (kr/kWh, Straumpris)
bomavgift_elbil  = 0.1   # (kr/km,  Bomavgift el-bil)

#%% Data Bensinbil
forsikring_bensin  = 7500  # (kr/år, forsikring bensinbil)
DSB = 1     # (kr/km, sats for bensin)
BAB = 0.3   # (kr/km, bomavgift bensinbil)

#%% forsikring_elbilllesdata
KM  = 10000     # (Km/år, km-stand)
dagar = 365
TF  = 8.38*dagar  # (kr/dag*, trafikkforsikringsavgift)

#%% Totalkostnadar EL-bil
TKE = KM * (forbruk_elbil * netleige_elbil + bomavgift_elbil) + TF + forsikring_elbil

#%% Totalkostnadar Bensinbil
TKB = KM * (DSB + BAB) + forsikring_bensin + TF

DIF = TKB - TKE

#%% Utskrifta
print('TKE =', TKE, 'og TKB =', TKB, 'og DIF =', DIF )

