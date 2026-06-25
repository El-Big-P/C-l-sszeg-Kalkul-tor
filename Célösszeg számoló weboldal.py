import streamlit as st

st.title("Pénzügyi Célösszeg Kalkulátor")

#Beviteli mezőket teszünk a weboldalra
cel_osszeg = st.number_input("Mekkora összeget szeretnél elérni? (Ft)", value=50000000)
kamatlab = st.number_input("Mekkora éves kamatra számítasz? (%)", 1.0, 20.0, 8.0) / 100
evek_szama = st.number_input("Hány éved van összegyűjteni? (év)", value=10)

if st.button("Számolás"):
    szukseges_eves = cel_osszeg * (kamatlab / (((1 + kamatlab) ** evek_szama) - 1))
    st.success(f"Minden évben pontosan {szukseges_eves:,.2f} Ft-ot kell befektetned!")