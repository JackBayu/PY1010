#%% Informasjon

"""
Arbeidskrav 1

Oppgåve: Årleg totalkostnadar for el-bil og for bensinbil, samt årleg kostnadsdiferranseorsikring_elbilranse.

Student: Jackson Bayubahe

Forfall: 2026-09-01
"""

#%% Data Elbil
forsikring_elbil = 5000  # (kr/år, forsikring el-bil)
forbruk_elbil    = 0.2   # (kWh/kilometerstand, forbruk)
strompris_elbil  = 2     # (kr/kWh, Straumpris)
bomavgift_elbil  = 0.1   # (kr/kilometerstand,  Bomavgift el-bil)

#%% Data Bensinbil
forsikring_bensinbil   = 7500  # (kr/år, forsikring bensinbil)
forbruk_bensinbil      = 1     # (kr/kilometerstand, sats for bensin)
bomavgift_bensinbil    = 0.3   # (kr/kilometerstand, bomavgift bensinbil)

#%% Fellesdata
kilometerstand           = 10000       # (kilometerstand/år, kilometerstand-stand)
dagar                    = 365         # (Dagar i løpet av året)
trafikkforsikringsavgift = 8.38*dagar  # (kr/dag*, trafikkforsikringsavgift)

#%% Totalkostnadar EL-bil
total_kostnadar_elbil = kilometerstand * (forbruk_elbil * strompris_elbil + bomavgift_elbil) + trafikkforsikringsavgift + forsikring_elbil

#%% Totalkostnadar Bensinbil
total_kostnadar_bensinbil = kilometerstand * (forbruk_bensinbil + bomavgift_bensinbil) + forsikring_bensinbil + trafikkforsikringsavgift

diferranse = total_kostnadar_bensinbil - total_kostnadar_elbil

#%% Utskriftar
print('SVAR PÅ OPPGÅVA\n')

print('Total kostnadar for elbil er  : ', total_kostnadar_elbil, 'kr')

print('Totale kostnadar for bensinbil: ', total_kostnadar_bensinbil, 'kr')

print('Differanse                    : ', diferranse, 'kr')

