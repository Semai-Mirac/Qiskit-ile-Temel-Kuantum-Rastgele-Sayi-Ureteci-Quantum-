# Qiskit-ile-Temel-Kuantum-Rastgele-Sayi-Ureteci-Quantum-

### Açıklama:
IBM'in Quantum alanındaki Qiskit teknolojisini anlamak adına yapılmıştır. IBM'im sanal ve gerçek makineleri ayrı kod dosyalrında denenmiştir

### Kullanılan Teknolojiler:
Python, Qiskit


## IBM_Qiskit.py kod dosyasının çalışma şekli: Sanal Makine
1. QuantumCircuit(num_bits, num_bits): Hem kuantum hesaplaması yapacağımız qubitleri, hem de okuma sonucunu kaydedeceğimiz klasik bitleri ayırıyoruz.

2. qc.h(i) (Hadamard Kapısı): Qubitleri %50 0, %50 1 olacağı rastgele bir faza (süperpozisyona) hapseder. Kuantum mekaniğinin asıl büyüsü buradadır!

3. qc.measure(...) (Ölçüm): Bu süperpozisyon çökertilir ve klasik evrendeki kesin hali (0 veya 1) olarak okunur.

4. AerSimulator & shots=1: Devremizi Qiskit'in Aer simülatöründe 1 kez çalıştırıyoruz çünkü tek bir atış, ihtiyacımız olan bir serilik rastgele rakam dizisini üretmek için yeterlidir.

## IBM_Qiskit_2.py kod dosyasının Kurulum ve Çalıştırma Adımları: Gerçek Makine
1. Gerekli Kütüphaneler:
qiskit-ibm-runtime ve python-dotenv paketlerini sisteminize kurun.

2. .env Dosyası:
Proje ana dizinize (yani kod dosyasının yanına) .env adında bir dosya hazırda vardır ve içine IBM'den aldıgınız anahtarı girin:

3. API Anahtarı Nereden Alınır?:
Eğer henüz almadıysanız:

IBM Quantum Cloud sayfasına gidin.
Giriş yapın veya ücretsiz bir hesap açın.
Ana sayfada (Dashboard) sağ üstteki menüde veya profil kısmında "API Token" (Kopyala) bölümünü göreceksiniz. Bunu kopyalayıp .env dosyasına yapıştırın.


## Önemli Uyarılar:

Gerçek cihazlarda işlem yapıldığında bulut sistemine kuyruk (queue) sırasına girersiniz. Bu nedenle işlem saniyede değil de, makinenin boşluğuna göre dakikalar veya bazen 1-2 saat sonra sonuç dönebilir. Script tamamlanana kadar duracak (bekleyecektir).

# API jetonunuzu asla halka açık yerlerde ifşa (commit) etmeyin. Eğer repo'ya gönderiyorsanız .gitignore a .env i mutlaka ekleyin.