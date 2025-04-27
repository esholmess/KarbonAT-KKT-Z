import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import json
from downloadpdf import save_as_pdf
import datetime
from factors import emission_factors
from oneri_fonksiyonları import oneri_al
import random


st.set_page_config(page_title="KARBON-AT", page_icon="🌿", layout="wide") #sayfa ayarı
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, black 70%, rgb(5, 170, 100, 0.2));

        }


        p, h1, h2, h3, h4, h5, h6, ul {
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        [data-testid="stSidebar"]{
        background: linear-gradient(to top, rgb(5, 170, 100), #004619 70%); 
        color: #015551
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 14px;
            font-weight: 500;
            padding: 5px 7px;
            margin: 15px -10px 1px 0px;
            border-radius: 3px;
            border: 1px solid #4caf4f64; 
            min-width: 10vw;
        }
            
        .stTabs [aria-selected="true"] {
            color: white;
            border-color: red 
        }

        .hr {
        margin: 5px 0 0 0;}


    </style>
    <h2 style="margin-bottom: -40px; ">🌿KARBON<span style="color:#10e800">AT</span></h2>
    
""", unsafe_allow_html = True
)



with st.sidebar: #sidebar ayarları
    st.markdown("""
        <style>
            #sidebarh3{
            margin-top: -5px;
            }
            #sidebarul{
            margin-right:25px;
            text-align:left;
                
            </style>
        <h3>HAKKINDA</h3>
        <p>KarbonAT size daha sürdürülebilir bir işletme olma konusunda yol gösterir!</p>
        <h3 id="sidebarh3">KarbonAT'ı kullanmaya başla:</h3><p>
        <ul id="sidebarul">
        <li> 🌱 Sizden istenen verileri günlük harcama raporlarınıza dayanarak girin.</li>
        <li> 🚀 Hesapla butonuna tıklayın.</li>
        <li> 📜 "Raporlar ve Öneriler" sekmesinde yol haritanızı alın.</li>
        <li> 🧠 Dilerseniz yapay zekadan öneriler alın.</li>
        <li> 🏆 "Scoreboard" sekmesinde yerinizi alın!</li>
        </ul>
        </p>
        </div>
        </div>

    """,unsafe_allow_html=True)

if 'scoreboard' not in st.session_state:
    st.session_state.scoreboard = []


tab1, tab2, tab3, tab4 = st.tabs(["🏠", "Hesap Makinesi", "Rapor & Öneriler", "🏆"]) #sekmeler

with tab1: #ana sayfa
   

    st.markdown("""
    <style>
        .stMarkdown div {
            border-radius: 5px;
            margin-bottom: 1rem;
            transition: transform 0.2s ease-in-out;
            color: white;  
            margin-top: 0.7rem;
            
        }
        .stMarkdown div:hover {
            transform: translateY(-1px);
        }
        .banner-container{
            display:flex;
            flex-direction: column;
            justify-content:center;
            align-items:center;}
                
        .banner {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(45deg, #28a7462b, #11a0753d);  
            border: 1px solid #28a745;
            color: white;
            border-radius: 10px;
            display:flex;
            flex-direction: column;
            align-items:center;
            justify-content:center;
            font-size:10px;
            width:70vw;
            
            
        }
        .banner h1 {
                text-align: center;}
        .banner p {
                max-width: 700px}

        .stButton button {
            background: linear-gradient(45deg, #28a745, #20c997);
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        #guide{
                text-align: left;
                align-items: center;
                justify-content:center;
                display:flex;
                flex-direction: column;
                gap:-5px;
                
            }


        #guide h3{
                margin-bottom: -30px
                }

        .banner h3 {
                margin-bottom: -10px;
                margin-top: -10px;
                font-size: 22px;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;}
        #features p{
                color: #7cff80;
                font-weight: 500;}

    </style>
    <div class="banner-container">
    <div class="banner">
        <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@800&display=swap" rel="stylesheet">
        <h3 style = "font-family: 'Baloo 2', cursive; margin: -20px 0 -50px 0; text-align:center; font-weight:700; transform: scaleY(0.95); font-size: 80px; color: #10b838; "> 🌿 </h3>
        <h3 style = "font-family:'Baloo 2'; color: #10b838; text-align:center; margin:-15px 0 -15px 0; font-size: 30px"> KARBONUNU HESAPLA GELECEĞİNİ PLANLA</h3>
    </div>
    <div class="banner">
                <p style = " font-style:italic; color: #7cff80; text-align:center; font-size:15px; margin:-15px 0 -15px 0"> Türkiye'nin '2053 yılında net 0 emisyon' hedefine giden yolda bize katılın!</p>
           
    </div>
    <div class="banner">
                <p style = "color: #7cff80; text-align:center; font-size:15px; margin:-15px 0 -15px 0"> KarbonAT size daha sürdürülebilir bir işletme olma konusunda yol gösterir!</p>     
    </div>
    <div class="banner" id="features" style= "font-style:italic; font-size:15px; color: #7cff80; text-align:center;">
                <p>🚀 Turizm Sektörüne Özgü Çözüm</p>
                <p>🚀 Pratik, Hızlı ve Basit sistem</p>
                <p>🚀 Kategorize Veri </p>
                <p>🚀 Uygun Maaliyetli</p>
                <p>🚀 Web Tabanlı - Dijital</p>
                <p>🚀 Yapay Zekâ Temelli Öneri Sistemi</p>
    
    </div>
    </div>
    """, unsafe_allow_html=True)



with tab2: #hesap makinesi sekmesi
    st.markdown("""
        <style>
        h3 {
            margin-bottom: -1rem;
            margin-top: 0.5rem
        }
        .stNumberInput {
            margin-top: -0.5rem;
 
        }
        .stForm {
            background: linear-gradient(45deg, #28a7462b, #11a0753d); 
            margin: 0.4rem 1rem;             
        }
        .form_title {
                margin: 0rem 1rem;
        }
        #formp {
                margin-top: -0.7rem;
                margin-bottom: -0.5rem;
                }
        }
        #form {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                border-bottom: 1px solid pink;}

        </style>
        <div id= "form">
        <h3 class = "form_title" style= "margin-bottom: -20px">🌍 HARCAMA GİRİŞİ</h3>
        <p class="form_title" id="formp">Karbon ayakizi hesaplaması için aşağıdaki formda sizden istenen verileri giriniz. 🌱</p>
        </div>
                
                """, unsafe_allow_html=True)


    with st.form("carbon_form"): # şirket verisi ve hesaplama için harcama verileri girişleri

  
        with st.expander("🏢 İŞLETME BİLGİLERİ *"):
                company_name = st.text_input("İşletme Adı", placeholder="Örn. Teknofest Suit Otel")
                col1, col2 = st.columns(2)
                with col1:
                    date_input = st.date_input("Bulunduğunuz Ayı ve Yılı Girin", datetime.date.today())
                with col2:
                    customer_number = st.number_input("Verilerin ait olduğu tarihe ilişkin müşteri sayısını giriniz", min_value=1, step=1)

                col3, col4, col5 = st.columns(3)
                with col3:
                    metrekare_number = st.number_input("İşletmenizin toplam metrekare sayısını giriniz", min_value=1, step=1)
                with col4:
                    room_number =  st.number_input("İşletmenizin toplam oda sayısını giriniz", min_value=1, step=1)
                with col5:
                    personel_number =  st.number_input("İşletmenizdeki personel sayısını giriniz", min_value=1, step=1)
        
        with st.expander("🔌 Elektrik Tüketimi"):
                elektrik_total = 0
                user_inputs = {"Elektrik": {}}
                for item, factor in emission_factors["Elektrik"].items():
                    amount = st.number_input(f"{item} (kWh)", min_value=0.0, value=0.0, key="Elektrik_" + item)
                    footprint = amount * factor
                    user_inputs["Elektrik"][item] = footprint
                    elektrik_total += footprint

        with st.expander(" 🔥 Doğal Gaz Tüketimi"):
            gaz_total = 0
            user_inputs["Doğal Gaz"] = {}
            for item, factor in emission_factors["Doğal Gaz"].items():
                amount = st.number_input(f"{item} (m³)", min_value=0.0, value=0.0, key="Gaz_" + item)
                footprint = amount * factor
                user_inputs["Doğal Gaz"][item] = footprint
                gaz_total += footprint

        with st.expander("🚿 Su Kullanımı"):
            su_total = 0
            user_inputs["Su"] = {}
            for item, factor in emission_factors["Su"].items():
                amount = st.number_input(f"{item} (m³)", min_value=0.0, value=0.0, key="Su_" + item)
                footprint = amount * factor
                user_inputs["Su"][item] = footprint
                su_total += footprint

        with st.expander("🍽️ Gıda Tüketimi"):
            gida_total = 0
            user_inputs["Gıda Tüketimi"] = {}
            for item, factor in emission_factors["Gıda Tüketimi"].items():
                amount = st.number_input(f"{item} (kg)", min_value=0.0, value=0.0, key="Gida_" + item)
                footprint = amount * factor
                user_inputs["Gıda Tüketimi"][item] = footprint
                gida_total += footprint

        
        with st.expander("♻️ Atık Yönetimi"):
            atik_total = 0
            user_inputs["Atık Yönetimi"] = {}
            for item, factor in emission_factors["Atık Yönetimi"].items():
                amount = st.number_input(f"{item} (kg)", min_value=0.0, value=0.0, key="Atik_" + item)
                footprint = amount * factor
                user_inputs["Atık Yönetimi"][item] = footprint
                atik_total += footprint

                
        with st.expander("🧪 Kimyasal Tüketimi"):
            kimyasal_total = 0
            user_inputs["Kimyasal Tüketimi"] = {}
            for item, factor in emission_factors["Kimyasal Tüketimi"].items():
                amount = st.number_input(f"{item} (L)", min_value=0.0, value=0.0, key="Kimyasal_" + item)
                footprint = amount * factor
                user_inputs["Kimyasal Tüketimi"][item] = footprint
                kimyasal_total += footprint



        hesapla = st.form_submit_button("🌍 Karbon Ayak İzini Hesapla") # verileri gönderme (submitleme) butonu

    if hesapla and company_name:
        total_footprint = elektrik_total + gaz_total + su_total + atik_total + gida_total + kimyasal_total
        footprint_kisibasi =  total_footprint / (customer_number + personel_number)
        footprint_m2 = total_footprint / metrekare_number
        footprint_oda = total_footprint / room_number
        category_footprints = {
            "Elektrik": elektrik_total,
            "Doğal Gaz": gaz_total,
            "Su": su_total,
            "Atık Yönetimi": atik_total,
            "Gıda Tüketimi": gida_total,
            "Kimyasal Tüketimi": kimyasal_total
        }

        st.session_state.latest_result = {
            "Company": company_name,
            **category_footprints,
            "Toplam": total_footprint,
            "Kisi Basi" : footprint_kisibasi,
            "Metrekare Basi" : footprint_m2,
            "Oda Basi" : footprint_oda, 
            "Tarih": date_input
        }
        st.session_state.latest_inputs = user_inputs
        st.session_state.latest_categories = category_footprints
        st.session_state.scoreboard.append(st.session_state.latest_result)
        st.success("✅ Karbon ayak izi başarıyla hesaplandı! Raporlar ve Öneriler sekmesine geçerek raporunuzu görüntüleyin!.")

    elif hesapla and not company_name:
        st.error("İşletme Bilgilerini Giriniz")
    elif hesapla and not customer_number:
        st.error("Müşteri sayısını giriniz - Müşteri sayısı en az 1 olmalıdır.")
    


with tab3:
    st.subheader("📊 Raporlar ve Öneriler")
    if 'latest_result' in st.session_state:
        results = st.session_state.latest_result

        st.markdown(f"""
        <div>
            <h3>Hoşgeldiniz {results["Company"]} !</h3>
            <p style='font-size:18px; color: white;'>📅 {results["Tarih"]} Tarihli Karbon Ayak İzi Raporu</p>
        </div>
        """, unsafe_allow_html=True)
        emission = results["Toplam"]

        st.markdown("<hr style='border:1px solid #00e676;'>", unsafe_allow_html=True)

        st.markdown("<h3 style='color:#00e676;'>🧠 Özet Durum Analiziniz</h3>", unsafe_allow_html=True)
        summary, detailed_suggestion, general_plan = oneri_al(elektrik_total, gaz_total, su_total, atik_total, gida_total, kimyasal_total)
        st.success(summary)

        # Emisyon Özeti 
        st.markdown("<hr style='border:1px solid #00e676;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00e676;'>📌 Emisyon Özeti</h3>", unsafe_allow_html=True)

        col3, col4 = st.columns(2)
        with col3:
            st.metric("🌍 Toplam Karbon Ayak İzi", f"{results['Toplam']:.2f} kg CO2")
        with col4:
            st.metric("👥 Kişi Başına Düşen", f"{results['Kisi Basi']:.2f} kg CO2")

        col5, col6 = st.columns(2)
        with col5:
            st.metric("🏨 Oda Başına Düşen", f"{results['Oda Basi']:.2f} kg CO2")
        with col6:
            st.metric("🏢 Metrekare Başına Düşen", f"{results['Metrekare Basi']:.2f} kg CO2")

        # Detaylı Emisyon Verileri
        st.markdown("<hr style='border:1px solid #00e676;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00e676;'>📊 Detaylı Emisyon Verileri (Alt Tür Bazlı)</h3>", unsafe_allow_html=True)

        for category, items in st.session_state.latest_inputs.items():
            with st.expander(f"📁 {category}", expanded=False):
                df = pd.DataFrame(list(items.items()), columns=["Alt Tür", "Emisyon (kg CO2)"])
                st.dataframe(df, use_container_width=True)

                fig, ax = plt.subplots(figsize=(6, 3), facecolor='black')
                bars = ax.bar(df["Alt Tür"], df["Emisyon (kg CO2)"], color='#2ECC71')
                ax.set_facecolor('black')
                ax.set_ylabel("CO2 (kg)", color='white')
                ax.set_title(f"{category} - Alt Tür Emisyonları", color='white')
                ax.tick_params(axis='x', rotation=45, labelcolor='white')
                ax.tick_params(axis='y', labelcolor='white')
                ax.spines[:].set_color('white')
                st.pyplot(fig)

        # Kategori Bazlı Toplam Emisyon
        st.markdown("<hr style='border:1px solid #00e676;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00e676;'>🔎 Kategori Bazlı Toplam Emisyon</h3>", unsafe_allow_html=True)

        df_summary = pd.DataFrame({
            "Kategori": list(st.session_state.latest_categories.keys()),
            "Toplam Emisyon (kg CO2)": list(st.session_state.latest_categories.values())
        })

        st.dataframe(df_summary, use_container_width=True)

        fig, ax = plt.subplots(figsize=(6, 4), facecolor='black')
        ax.barh(df_summary["Kategori"], df_summary["Toplam Emisyon (kg CO2)"], color='#27AE60')
        ax.set_xlabel("CO2 (kg)", color='white')
        ax.set_title("Kategoriye Göre Karbon Ayak İzi", color='white')
        ax.tick_params(axis='x', labelcolor='white')
        ax.tick_params(axis='y', labelcolor='white')
        ax.set_facecolor('black')
        ax.spines[:].set_color('white')
        st.pyplot(fig)

        
        st.markdown("<hr style='border:1px solid #00e676;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00e676;'>📉 Detaylı Öneri Al</h3>", unsafe_allow_html=True)
        ai_rec= st.button("💡 Detaylı Öneri Al")
        if ai_rec:
                st.write(detailed_suggestion)
                st.write(general_plan)



        # PDF Raporu 
        st.markdown("<hr style='border:1px solid #00e676;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00e676;'>📄 Raporu PDF Olarak İndir</h3>", unsafe_allow_html=True)

        pdf_data = save_as_pdf(
            results=st.session_state.latest_result,
            category_footprints=st.session_state.latest_categories,
            recommendations=detailed_suggestion.split("\n") + general_plan.split("\n"),
            logo_path="logo.png"
        )

        st.download_button(
            label="📥 PDF İndir",
            data=pdf_data,
            file_name=f"{results['Company'].replace(' ', '_')}_karbon_raporu.pdf",
            mime="application/pdf"
        )

    else:
        st.info("📌 Önce hesaplama yapmanız gerekiyor.")


# Scoreboard Sekmesi

with tab4:
    st.subheader("🏆 Scoreboard")
    if st.session_state.scoreboard:
        df_scoreboard = pd.DataFrame(st.session_state.scoreboard)
        df_sorted = df_scoreboard.sort_values("Toplam").reset_index(drop=True)
        df_sorted.index += 1
        st.dataframe(df_sorted.rename_axis('Sıra'), use_container_width=True)
    else:
        st.info("Henüz hiçbir veri girilmedi.")
