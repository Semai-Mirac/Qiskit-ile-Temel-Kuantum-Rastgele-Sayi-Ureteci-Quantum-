# Qiskit-ile-Temel-Kuantum-Rastgele-Sayi-Ureteci-Quantum-
IBM'in Quantum alanındaki Qiskit teknolojisini anlamak adına yapılmıştır.

## IBM_Qiskit.py kod dosyasının çalışma şekli
1. QuantumCircuit(num_bits, num_bits): Hem kuantum hesaplaması yapacağımız qubitleri, hem de okuma sonucunu kaydedeceğimiz klasik bitleri ayırıyoruz.

2. qc.h(i) (Hadamard Kapısı): Qubitleri %50 0, %50 1 olacağı rastgele bir faza (süperpozisyona) hapseder. Kuantum mekaniğinin asıl büyüsü buradadır!

3. qc.measure(...) (Ölçüm): Bu süperpozisyon çökertilir ve klasik evrendeki kesin hali (0 veya 1) olarak okunur.

4. AerSimulator & shots=1: Devremizi Qiskit'in Aer simülatöründe 1 kez çalıştırıyoruz çünkü tek bir atış, ihtiyacımız olan bir serilik rastgele rakam dizisini üretmek için yeterlidir.