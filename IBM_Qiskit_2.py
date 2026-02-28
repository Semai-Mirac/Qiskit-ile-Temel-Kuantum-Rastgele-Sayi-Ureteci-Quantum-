import os
from dotenv import load_dotenv

from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit_ibm_runtime import QiskitRuntimeService

def run_on_real_quantum_computer(num_bits):
    """
    Belirtilen bit sayısında gerçek bir Kuantum Bilgisayar ile rastgele sayı üretir.
    NOT: Çalışması simülatörden çok daha yavaş olacaktır ve kuyruk (queue) bekleyebilirsiniz.
    """
    print("IBM Quantum API'ye bağlanılıyor...")
    
    # 1. API Anahtarını al ve kimlik doğrulaması yap
    # Bu adım için IBM Quantum portalından bir API token almalısınız (https://quantum.ibm.com)
    api_token = os.getenv("IBM_QUANTUM_TOKEN")
    
    if not api_token:
        raise ValueError("Lütfen .env dosyasına IBM_QUANTUM_TOKEN değerini ekleyin.")

    # Service nesnesine bağlan
    service = QiskitRuntimeService(channel="ibm_quantum", token=api_token)
    print("Bağlantı başarılı!")

    # 2. Uygun bir gerçek kuantum makinesi seçelim
    # "least_busy" (en boş) mantıklı olanıdır, aksi halde günlerce bekleyebilirsiniz.
    print("En az meşgul olan kuantum bilgisayar aranıyor...")
    backend = service.least_busy(operational=True, simulator=False)
    print(f"Seçilen Cihaz: {backend.name}")

    # 3. Kuantum devresini oluştur
    qc = QuantumCircuit(num_bits, num_bits)

    # 4. Superpozisyon ve ölçüm adımları
    for i in range(num_bits):
        qc.h(i)
    
    qc.measure(range(num_bits), range(num_bits))

    # 5. Devreyi GERÇEK donanım (backend) için derle (transpile)
    print(f"Devre '{backend.name}' için derleniyor...")
    compiled_circuit = transpile(qc, backend=backend)

    # 6. Kodu IBM cihazına gönder ve çalıştır
    print("Görev cihaza gönderiliyor, kuyruk (queue) durumu sebebiyle bu işlem dakikalar sürebilir...")
    
    # Gerçek cihazda da tek atış (shot) yapıyoruz.
    job = backend.run(compiled_circuit, shots=1)
    
    # Kuyruktayken işin (job) durumunu yazırabilirsiniz
    print(f"Job ID: {job.job_id()}")
    
    # Sonucun tamamlanmasını bekle
    result = job.result()
    
    # 7. Sonuçları işle
    counts = result.get_counts()
    bit_string = list(counts.keys())[0]  
    random_number = int(bit_string, 2)

    return random_number, bit_string, backend.name

if __name__ == "__main__":
    # Çevre (environment) değişkenlerini .env dosyasından yükle
    load_dotenv()
    
    BIT_SAYISI = 4
    print(f"--- {BIT_SAYISI} Qubit Gerçek IBM Makinesi Üzerinde QRNG ---")
    
    try:
        sayi, bit_dizisi, cihaz_adi = run_on_real_quantum_computer(BIT_SAYISI)
        
        print("\n=== SONUÇLAR ===")
        print(f"Cihaz: {cihaz_adi}")
        print(f"Ölçülen Kuantum Durumu (İkili) : {bit_dizisi}")
        print(f"Üretilen Gerçek Rastgele Sayı (Ondalık): {sayi}")
        print("-" * 46)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")