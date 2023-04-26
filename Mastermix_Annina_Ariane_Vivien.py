# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:53:26 2023

@author: arian
"""

import streamlit as st

# Titel und Beschreibung anzeigen
st.title('PCR-Mastermix Step-by-Step Anleitung')
st.markdown('Dieses Programm führt dich Schritt für Schritt durch den Ablauf einer Herstellung des Mastermixes für PCR. Hast du einen Schritt ausgeführt, bestätige den Task mit einem Haken. Danach wird der nächste Schritt ersichtlich.')

# Funktion zur Berechnung der Ergebnisse
def calculate(x):
    # Berechnungen mit x durchführen
    result1 = x * 5
    result2 = x * 1
    result3 = x * 2
    result4 = x * 2
    result5 = x * 1
    result6 = x * 5
    result7 = x * 1 
    result8 = (max(x * 50 - (result1 + result2 + result3 + result4 + result5 + result6 + result7), 0))
    
    return result1, result2, result3, result4, result5, result6, result7, result8
   

# Anzahl der Proben eingeben
x = st.number_input("Gib deine Anzahl Proben ein (max. 96):", value=5, step=1)

# Anleitung für das Beschriften der Testtubes anzeigen
st.markdown("Für deinen Mastermix brauchst du für jede Probe ein eigenes Test-Tube. Stelle für jede deiner Proben ein Test-Tube bereit und beschrifte sie entsprechend.")

# Checkboxen für die einzelnen Schritte anzeigen
results = calculate(x)
# Schritt 1: PCR Puffer pipettieren
checkbox1 = st.checkbox("Schritt 1: PCR Puffer pipettieren")
st.write("Für deine Anzahl Proben werden insgesamt", results[0], "Mikroliter PCR Puffer benötigt. Davon pipettierst du je 5 Mikroliter in jedes Testtube.")
if checkbox1:
# Schritt 2: dNTP pipettieren
    checkbox2 = st.checkbox("Schritt 2: dNTP pipettieren")
    st.write("Für deine Anzahl Proben werden insgesamt", results[1], "Mikroliter dNTP benötigt. Davon pipettierst du je 1 Mikroliter in jedes Testtube.")
    if checkbox2:
        # Schritt 3: Vorwärtsprimer pipettieren
        checkbox3 = st.checkbox("Schritt 3: Vorwärtsprimer pipettieren")
        st.write("Für deine Anzahl Proben werden insgesamt", results[2], "Mikroliter Vorwärtsprimer benötigt. Davon pipettierst du je 2 Mikroliter in jedes Testtube.")

        if checkbox3:
            # Schritt 4: Rückwärtsprimer pipettieren
            checkbox4 = st.checkbox("Schritt 4: Rückwärtsprimer pipettieren")
            st.write("Für deine Anzahl Proben werden insgesamt", results[3], "Mikroliter Rückwärtsprimer benötigt. Davon pipettierst du je 2 Mikroliter in jedes Testtube.")

            if checkbox4:
                # Schritt 5: Taq-DNA-Polymerase pipettieren
                checkbox5 = st.checkbox("Schritt 5: Taq-DNA-Polymerase pipettieren")
                st.write("Für deine Anzahl Proben werden insgesamt", results[4], "Mikroliter Taq-DNA-Polymerase benötigt. Davon pipettierst du je 1 Mikroliter in jedes Testtube. ")
                
                if checkbox5:
                    # Schritt 6: Template DNA pipettieren
                    checkbox6 = st.checkbox("Schritt 6: Template DNA pipettieren")
                    st.write("Für deine Anzahl Proben werden insgesamt", results[5], "Mikroliter Template DNA benötigt. Davon pipettierst du je 5 Mikroliter in jedes Testtube.")
                    if checkbox6:
                        # Schritt 7: MgCl2 pipettieren
                        checkbox7 = st.checkbox("Schritt 7: MgCl2 pipettieren")
                        st.write("Für deine Anzahl Proben werden insgesamt", results[6], "Mikroliter MgCl2 benötigt. Davon pippetierst du je 1 Mikroliter in jedes Testtube.")
                        if checkbox7:
                            #Schritt 8: Wasser pipettieren 
                            checkbox8 = st.checkbox("Schritt 8: Wasser pipettieren.")
                            st.write("Für deine Anzahl Proben werden insgesamt", results[7], "Mikroliter Wasser benötigt. Davon pippetierst du eine variable Menge in jedes Testtube, sodass das Endvolumen 50 Mikroliter beträgt.")
                            if checkbox8:
                                st.write("Die Herstellung deines Mastermixes ist nun beendet")