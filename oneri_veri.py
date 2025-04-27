# oneri_veri.py

# Kısa alan özetleri
summaries = {
    "Elektrik": "İşletmenizin karbon ayak izinin büyük bölümü elektrik tüketiminden kaynaklanıyor.",
    "Doğal Gaz": "İşletmenizin karbon salınımı büyük ölçüde doğal gaz kullanımından kaynaklanıyor.",
    "Su": "İşletmenizin karbon ayak izinin önemli bir kısmı su tüketiminden oluşuyor.",
    "Atık Yönetimi": "İşletmenizin karbon salınımında atık yönetimi süreçleri belirgin rol oynuyor.",
    "Gıda Tüketimi": "İşletmenizin karbon ayak izi büyük oranda gıda tüketiminden kaynaklanıyor.",
    "Kimyasal Tüketimi": "İşletmenizin karbon salımında kimyasal madde tüketimi önemli bir yer tutuyor."
}

# Alan bazlı 5 cümlelik öneriler
detailed_recommendations = {
    "Elektrik": (
        "LED aydınlatmalara geçiş yaparak elektrik tüketiminizi azaltabilirsiniz. "
        "Enerji verimliliği yüksek cihazlar kullanarak elektrik kullanımını optimize edebilirsiniz. "
        "Ofislerde hareket sensörlü aydınlatmalarla gereksiz enerji tüketimini önleyebilirsiniz. "
        "Güneş panelleri gibi yenilenebilir enerji kaynaklarına yatırım yapabilirsiniz. "
        "Çalışanlar arasında enerji tasarrufu bilincini artırmak için eğitimler düzenleyebilirsiniz."
    ),
    "Doğal Gaz": (
        "Bina yalıtımını iyileştirerek doğal gaz tüketimini önemli ölçüde azaltabilirsiniz. "
        "Yüksek verimli ısıtma sistemleri kullanarak enerji tasarrufu sağlayabilirsiniz. "
        "İdeal sıcaklık ayarları ile gereksiz doğal gaz tüketimini önleyebilirsiniz. "
        "Enerji yönetim sistemleriyle doğal gaz kullanımını izleyip optimize edebilirsiniz. "
        "Yenilenebilir enerji destekli ısıtma sistemlerine geçiş yapabilirsiniz."
    ),
    "Su": (
        "Su kaçaklarını önlemek için düzenli bakım ve denetimler yapabilirsiniz. "
        "Su tasarruflu musluklar ve duş başlıkları kullanarak tüketimi azaltabilirsiniz. "
        "Yağmur suyu toplama sistemleri kurarak doğal kaynaklardan yararlanabilirsiniz. "
        "Gri su geri dönüşüm sistemleriyle su kullanımınızı optimize edebilirsiniz. "
        "Personelin su tasarrufu bilincini artırmak için eğitimler düzenleyebilirsiniz."
    ),
    "Atık Yönetimi": (
        "Atıkları kaynağında ayrıştırarak geri dönüşüm oranlarınızı artırabilirsiniz. "
        "Organik atıkları kompostlama ile doğaya kazandırabilirsiniz. "
        "Tek kullanımlık ürünlerin kullanımını azaltarak atık üretimini düşürebilirsiniz. "
        "Geri dönüştürülmüş ve sürdürülebilir malzemeleri tercih edebilirsiniz. "
        "Atık verilerini düzenli izleyerek sürekli iyileştirme hedefleri belirleyebilirsiniz."
    ),
    "Gıda Tüketimi": (
        "Gıda israfını azaltmak için porsiyon kontrolü uygulayabilirsiniz. "
        "Yerel ve mevsimsel ürünler kullanarak karbon ayak izinizi düşürebilirsiniz. "
        "Artan gıdalar için bağış veya yeniden kullanım mekanizmaları oluşturabilirsiniz. "
        "Sürdürülebilir tarım tedarikçilerini tercih edebilirsiniz. "
        "Çalışanlara gıda israfı hakkında eğitim vererek farkındalık artırabilirsiniz."
    ),
    "Kimyasal Tüketimi": (
        "Daha çevreci alternatif kimyasallar kullanarak çevreye olan etkiyi azaltabilirsiniz. "
        "Kimyasal tüketimini azaltmak için optimize edilmiş kullanım planları geliştirebilirsiniz. "
        "Güvenli ve uygun depolama sistemleri kurarak sızıntı ve kayıpları önleyebilirsiniz. "
        "Kimyasal atıkları düzenli şekilde toplayıp bertaraf edebilirsiniz. "
        "Çalışanlara güvenli kimyasal kullanım eğitimi vererek riskleri minimize edebilirsiniz."
    )
}

# Genel iyileşme planı (her rapora eklenir)
general_plan = (
    "İşletme genelinde düzenli karbon ayak izi ölçümleri yapılmalıdır. "
    "Sürdürülebilirlik hedefleri için yıllık azaltım planları oluşturulmalıdır. "
    "Tedarik zinciri süreçleri karbon nötr firmalarla güçlendirilmelidir. "
    "Çalışan eğitimleri ile çevre bilinci artırılmalıdır. "
    "Enerji, su, atık ve hammadde yönetiminde yıllık performans raporları hazırlanmalıdır."
)
