#%% Informasjon

"""
Arbeidskrav 1

Oppgåve: Årleg totalkostnadar for el-bil og for bensinbil, samt årleg kostnadsdiferanse.

Student: Jackson Bayubahe

Forfall: 2026-09-01
"""

#%% Data Elbil
FE  = 5000  # (kr/år, forsikring el-bil)
DSE = 0.2   # (kWh/km, forbruk)
NL  = 2     # (kr/kWh, Straumpris)
BAE = 0.1   # (kr/km,  Bomavgift el-bil)

#%% Data Bensinbil
FB  = 7500  # (kr/år, forsikring bensinbil)
DSB = 1     # (kr/km, sats for bensin)
BAB = 0.3   # (kr/km, bomavgift bensinbil)

#%% Fellesdata
KM  = 10000     # (Km/år, km-stand)

TF  = 8.38*365  # (kr/dag*, trafikkforsikringsavgift)

#%% Totalkostnadar EL-bil
TKE = KM * (DSE * NL + BAE) + TF + FE

#%% Totalkostnadar Bensinbil
TKB = KM * (DSB + BAB) + FB + TF

DIF = TKB - TKE

#%% Utskrifta
print('TKE =', TKE, 'og TKB =', TKB, 'og DIF =', DIF )

