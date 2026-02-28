Qiskit ile Kuantum Rastgele Sayı Üreteci (QRNG)
Bu proje, IBM'in Qiskit kütüphanesini kullanarak kuantum mekaniğinin temel prensiplerinden biri olan süperpozisyon yardımıyla gerçek rastgele sayılar üretmeyi amaçlar. Proje kapsamında hem yerel simülatör (Aer) hem de gerçek kuantum donanımı (IBM Quantum) üzerinde testler gerçekleştirilmiştir.

🚀 Proje Hakkında
Klasik bilgisayarlar "sözde rastgele" (pseudo-random) sayılar üretirken, kuantum bilgisayarlar kuantum durumlarının ölçümündeki belirsizliği kullanarak "gerçek rastgele" (true-random) sayılar üretir. Bu projede:

Süperpozisyon: Hadamard (H) kapısı ile qubitlerin durumları belirsizleştirilir.

Ölçüm: Belirsizlik hali çöktürülerek klasik bit dizilerine (0 ve 1) dönüştürülür.

🛠️ Kullanılan Teknolojiler
Dil: Python

Kütüphaneler: qiskit, qiskit-aer, qiskit-ibm-runtime, python-dotenv

Platform: IBM Quantum Platform

📁 Dosya Yapısı ve Çalışma Mantığı
1. IBM_Qiskit.py (Yerel Simülasyon)
Bu dosya, kuantum devresini kendi işlemcinizde simüle etmek için tasarlanmıştır. Geliştirme ve hızlı test aşamaları için idealdir.

Süreç: 1. QuantumCircuit ile istenen bit sayısında devre oluşturulur.
2. Hadamard (H) Kapısı: Qubitler %50 olasılıkla 0 veya 1 olacak şekilde süperpozisyona alınır.
3. Ölçüm: qc.measure() ile kuantum durumu okunur ve klasik bitlere yazılır.
4. Simülatör: AerSimulator kullanılarak devre yerel olarak koşturulur.

2. IBM_Qiskit_2.py (Gerçek Kuantum Donanımı)
Bu dosya, oluşturulan devreyi internet üzerinden gerçek bir IBM kuantum bilgisayarına gönderir.

Süreç:

QiskitRuntimeService ile IBM bulut sistemine bağlanılır.

Backend Seçimi: least_busy metodu ile o an kuyruğu en az olan gerçek cihaz otomatik seçilir.

Transpile: Devre, seçilen cihazın fiziksel mimarisine göre optimize (derleme) edilir.

Job: İşlem bir "Job" (görev) olarak gönderilir ve sonuçlar dönene kadar kuyrukta beklenir.

⚙️ Kurulum ve Yapılandırma
1. Kütüphanelerin Kurulumu
Terminal üzerinden gerekli paketleri yükleyin:

Bash
pip install qiskit qiskit-aer qiskit-ibm-runtime python-dotenv
2. API Anahtarı (Token) Ayarı
Gerçek cihazı kullanabilmek için bir IBM Quantum hesabına ihtiyacınız vardır:

IBM Quantum adresine gidin.

Hesabınızdan API Token değerini kopyalayın.

Proje klasöründe .env isimli bir dosya oluşturun ve içine yapıştırın:

Kod snippet'i
IBM_QUANTUM_TOKEN=KOPYALADIĞINIZ_TOKEN_BURAYA
⚠️ Önemli Notlar ve Uyarılar
Kuyruk Bekleme: Gerçek kuantum bilgisayarları dünya genelinde ortak kullanıldığı için IBM_Qiskit_2.py dosyasını çalıştırdığınızda "kuyruk" (queue) durumuna göre sonuçların gelmesi birkaç dakikadan birkaç saate kadar sürebilir.

Güvenlik: .env dosyanızı ve API anahtarınızı asla GitHub gibi halka açık platformlarda paylaşmayın. Projenize .gitignore dosyasını ekleyerek .env dosyasını hariç tutun.

Hizmet Kesintisi: Kuantum cihazları bakımda olabilir; bu durumda kod least_busy aşamasında hata verebilir veya farklı bir cihaz seçebilir.

## Önemli Uyarılar:

Gerçek cihazlarda işlem yapıldığında bulut sistemine kuyruk (queue) sırasına girersiniz. Bu nedenle işlem saniyede değil de, makinenin boşluğuna göre dakikalar veya bazen 1-2 saat sonra sonuç dönebilir. Script tamamlanana kadar duracak (bekleyecektir).

# API jetonunuzu asla halka açık yerlerde ifşa (commit) etmeyin. Eğer repo'ya gönderiyorsanız .gitignore a .env i mutlaka ekleyin.