import streamlit as st

st.title("Net Plant Heat Rate (Kcal/kWh)")
st.write("Masukkan Data Pembangkit")

coal1 =  st.number_input("Flow Batubara 1 (t/h)", min_value=0.0, value=0.0)
coal2 =  st.number_input("Flow Batubara 2 (t/h)", min_value=0.0, value=0.0)
nilai_kalor_batubara =  st.number_input("Nilai Kalor Batubara (kkcal/kg)", min_value=0.0, value=0.0)
nilai_kalor_cofiring =  st.number_input("Nlai Kalor Cofiring (kkcal/kg)", min_value=0.0, value=0.0)
produksi_listrik = st.number_input("Produksi Listrik (MW)", min_value=0.0, value=0.0)
st.info("Produksi Listrik Masukkan dalam satuan MW, bukan kwh")
periode_jam = st.number_input ("Periode pengambilan data (jam)", min_value=1.0, value=2.0)
auxiliary_power_harian = st.number_input("Auxiliary Power", min_value=0.0, value=0.0)

if st.button("Hitung Net Plant Heat Rate"):
    total_coal =(coal1+coal2)*1000
    auxiliary_power = auxiliary_power_harian*(periode_jam/24)
    net_generation = produksi_listrik-auxiliary_power
    if net_generation > 0:
        if nilai_kalor_batubara > 0 and nilai_kalor_cofiring > 0:
            st.error("Isi salah satu nilai kalor (Batubara atau cofiring)")
        elif nilai_kalor_batubara >0:
            Net_Plant_Heat_Rate_Batubara = (total_coal*nilai_kalor_batubara)/net_generation
            st.success(f"NPHR Batubara = {Net_Plant_Heat_Rate_Batubara:.4f} Kcal/kWh")
        elif nilai_kalor_cofiring >0:
            Net_Plant_Heat_Rate_Cofiring = (total_coal*nilai_kalor_cofiring)/net_generation
            st.success(f"NPHR Cofiring = {Net_Plant_Heat_Rate_Cofiring:.4f} Kcal/kWh")
        else:
            st.error("Masukkan salah satu nilai kalor terlebih dahulu")