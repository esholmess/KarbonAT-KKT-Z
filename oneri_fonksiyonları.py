# oneri_fonksiyonları.py

from oneri_veri import summaries, detailed_recommendations, general_plan

def oneri_al(elektrik_total, gaz_total, su_total, atik_total, gida_total, kimyasal_total):
    esik_deger = 500  # Kritik eşik

    emissions = {
        "Elektrik": elektrik_total,
        "Doğal Gaz": gaz_total,
        "Su": su_total,
        "Atık Yönetimi": atik_total,
        "Gıda Tüketimi": gida_total,
        "Kimyasal Tüketimi": kimyasal_total
    }

    sorted_emissions = sorted(emissions.items(), key=lambda x: x[1], reverse=True)

    if all(value < esik_deger for _, value in sorted_emissions):
        summary = "Tebrikler! İşletmenizin karbon ayak izi genel olarak düşük seviyede ve çevresel etkisi oldukça sınırlı."
        detailed_suggestions = (
            "Mevcut sürdürülebilirlik stratejilerinizi koruyarak çevreye olan katkınızı sürdürmelisiniz. "
            "Düzenli ölçümler yaparak performansınızı izlemeye devam edin. "
            "Küçük iyileştirmelerle daha da örnek bir çevre dostu işletme olabilirsiniz. "
            "Yenilikçi teknolojilere yatırım yaparak mevcut başarıyı artırabilirsiniz. "
            "Çalışanlarınızı çevresel farkındalık konusunda motive etmeye devam edin."
        )
    else:
        baskin_alan, baskin_deger = sorted_emissions[0]
        summary = f"İşletmenizin karbon ayak izi ağırlıklı olarak {baskin_alan} kaynaklıdır ({baskin_deger:.2f} kg CO₂)."

        detailed_suggestions = ""
        for alan, deger in sorted_emissions:
            if deger < esik_deger:
                continue

            alan_ozet = summaries.get(alan, f"{alan} alanında yüksek karbon salınımı gözlemlenmektedir.")
            alan_oneriler = detailed_recommendations.get(alan, "Bu alan için henüz özel bir öneri bulunmamaktadır.")

            detailed_suggestions += f"📌 **{alan}**\n\n"
            detailed_suggestions += f"{alan_ozet}\n\n"
            detailed_suggestions += f"{alan_oneriler}\n\n"
            detailed_suggestions += "---\n\n"

    return summary, detailed_suggestions, general_plan
