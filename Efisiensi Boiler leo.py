#Data 1: wood pellet kayu akasia
tekanan_steam = 4.85 #mpa
temperature_steam = 470.8 #°C
entalpi_steam = 804.67 #kcal/kg
total_steam = 960.6 #t/h
tekanan_air = 8.423 #mpa
temperature_air = 84.29 #°C
entalpi_air = 84.38 #kcal/kg
total_air = 1194.7 #t/h
totalflow_coal1 = 80.50 #t/h
totalflow_coal2 = 81.00 #t/h
total_produuksi_generator = 235482 #kWh
auxiliary_power_batubara = 36932
kalor_akasia = 4805 #kcal/kg
kalor_batubara = 5325 #kcal/kg
masa_batubara = 0.99 
masa_wood_pellet = 0.01 

#Data 2: wood pellet kayu puspa
tekanan_steam_cf2 = 4.80 #mpa
temperature_steam_cf2 = 474.3 #°C
entalpi_steam_cf2 = 807 #kcal/kg
total_steam_cf2 = 937.1 #t/h
tekanan_air_cf2 = 8.26 #mpa
temperature_air_cf2 = 85.28 #°C
entalpi_air_cf2 = 85.41 #kcal/kg
total_air_cf2 = 1352.7 #t/h
totalflow_coal1_cf2 = 83.30 #t/h
totalflow_coal2_cf2 = 84.70 #t/h
total_produuksi_generator_cf2 = 233481 #kWh
Kalor_Puspa = 4580 #kcal/kg
auxiliary_power_cf2 = 38094

#Data 3: wood pellet kayu pulai
tekanan_steam_cf5 = 4.82 #mpa
temperature_steam_cf5 = 480.1 #°C
entalpi_steam_cf5 = 810 #kcal/kg
total_steam_cf5 = 925.8 #t/h
tekanan_air_cf5 = 8.38 #mpa
temperature_air_cf5 = 82.36 #°C
entalpi_air_cf5 = 82.41 #kcal/kg
total_air_cf5 = 1155.9 #t/h
totalflow_coal1_cf5 = 87.70 #t/h
totalflow_coal2_cf5 = 88.60 #t/h
total_produuksi_generator_cf5 = 221159 #kWh
Kalor_pulai = 4068 #kcal/kg
auxiliary_power_cf5 = 44338

##Perhitungan
#Hitung nilai kalo co-firing
Nilai_Kalor_kayu_akasia = ((kalor_akasia*masa_wood_pellet)+(kalor_batubara*masa_batubara))
Nilai_Kalor_kayu_puspa = ((Kalor_Puspa*masa_wood_pellet)+(kalor_batubara*masa_batubara))
Nilai_Kalor_kayu_pulai = ((Kalor_pulai*masa_wood_pellet)+(kalor_batubara*masa_batubara))

#wood pellet akasia
#Efisiensi_boiler
Coal_total = ((totalflow_coal1+totalflow_coal2)*1000)
Boiler_efisiensi = (total_steam * 1000 * (entalpi_steam - entalpi_air))/((Coal_total*Nilai_Kalor_kayu_akasia)) *100

#wood pellet puspa
#Efisiensi_boiler
Coal_total_cf2 = (totalflow_coal1_cf2 + totalflow_coal2_cf2)*1000
Boiler_efisiensi_cf2 = (total_steam_cf2 * 1000 * (entalpi_steam_cf2 - entalpi_air_cf2))/((Coal_total_cf2*Nilai_Kalor_kayu_puspa)) *100

#wood pellet kayu pulai
#Efisiensi_boiler
Coal_total_cf5 = (totalflow_coal1_cf5 + totalflow_coal2_cf5)*1000
Boiler_efisiensi_cf5 = (total_steam_cf5 * 1000 * (entalpi_steam_cf5 - entalpi_air_cf5))/((Coal_total_cf5*Nilai_Kalor_kayu_pulai)) *100

print ("Hasil Pengolahan Data Efisiensi Boiler")
print("efisiensi kayu akasia")
print ("Efisiensi Boiler :", Boiler_efisiensi, "%\n") 

print("efisiensi boiler kayu puspa")
print ("Efisiensi Boiler :", Boiler_efisiensi_cf2, "%\n") 

print("efisiensi boiler kayu pulai")
print ("Efisiensi Boiler :", Boiler_efisiensi_cf5, "%\n") 

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
#Grafik Perbandingan % Efisiensi Boiler
#Rasio
Rasio = ["efisiensi kayu akasia", "efisiensi kayu puspa", "efisiensi kayu pulai"]

#Data
Efisiensi_Boiler = [Boiler_efisiensi,Boiler_efisiensi_cf2,Boiler_efisiensi_cf5]

#Grafik
plt.figure(figsize=(12,6))
plt.plot(Rasio, Efisiensi_Boiler, marker='o', linewidth=3)

#Nilai pada titik grafik
for i, value in enumerate (Efisiensi_Boiler):
    plt.text(i, value, f'{value}%', ha='center')

#Judul dan Label
plt.title ("Grafik Perbandingan Efisiensi Boiler")
plt.xlabel("Rasio Co-firing")
plt.ylabel("Efisiensi_Boiler (%)")
plt.ylim(min(Efisiensi_Boiler)-0.1, max(Efisiensi_Boiler)+0.1)
plt.yticks(np.arange(75, 91, 1))
ax=plt.gca()
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
