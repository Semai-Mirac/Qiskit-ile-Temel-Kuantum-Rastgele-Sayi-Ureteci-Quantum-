from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile

def generate_quantum_random_number(num_bits):
    """
    Belirtilen bit sayısında gerçek rastgele bir sayı üretir.
    num_bits: Üretilecek sayının kaç bitlik olacağı (Örn: 4 bit -> 0-15 arası sayı)
    """
    # 1. Kuantum devresini oluştur (qubitler ve klasik bitler)
    qc = QuantumCircuit(num_bits, num_bits)

    # 2. Her bir qubite Hadamard (H) kapısı uygula
    # Bu adımla qubitler süperpozisyon durumuna (aynı anda hem 0 hem 1) geçer
    for i in range(num_bits):
        qc.h(i)

    # 3. Kuantum durumunu ölç ve sonuçları klasik bitlere yazdır
    qc.measure(range(num_bits), range(num_bits))

    # 4. Aer simülatörünü başlat (Gerçek bir kuantum bilgisayar yerine yerel simülasyon)
    simulator = AerSimulator()

    # 5. Devreyi simülatör için derle (transpile)
    compiled_circuit = transpile(qc, simulator)

    # 6. Devreyi çalıştır (Rastgele bir sayı için sadece 1 shot(atış) yeterlidir)
    job = simulator.run(compiled_circuit, shots=1)
    result = job.result()
    
    # 7. Sonuçları al
    # get_counts() örneğin {'1011': 1} şeklinde bir sözlük döndürür
    counts = result.get_counts()
    bit_string = list(counts.keys())[0]  # Ölçülen bit dizisini (örn: '1011') al
    
    # 8. İkili (binary) diziyi ondalık (decimal) sayıya çevir
    random_number = int(bit_string, 2)

    return random_number, bit_string, qc

if __name__ == "__main__":
    print("--- Qiskit ile Kuantum Rastgele Sayı Üreteci ---")
    
    # Kaç bitlik bir rastgele sayı üretmek istiyoruz? (Örn: 5 bit -> 0 ile 31 arası)
    BIT_SAYISI = 4
    
    sayi, bit_dizisi, devre = generate_quantum_random_number(BIT_SAYISI)
    
    print(f"\nOluşturulan {BIT_SAYISI} Qubitlik Kuantum Devresi:")
    print(devre.draw(output='text'))  # Çizimi konsolda metin tabanlı olarak göster
    
    print("\nSonuçlar:")
    print(f"Ölçülen Kuantum Durumu (İkili) : {bit_dizisi}")
    print(f"Üretilen Rastgele Sayı (Ondalık): {sayi}")
    print("-" * 46)