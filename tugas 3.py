class Hewan:
    def __init__(self, nama, usia):
        if not nama.strip():
            raise ValueError("Kesalahan: Nama hewan tidak boleh kosong.")
        if not usia.strip():
            raise ValueError("Kesalahan: Usia tidak boleh kosong.")
        
        self.__nama = nama
        self.__usia = usia
    
    def bersuara(self):
        pass
    
    def get_nama(self):
        return self.__nama
    
    def get_usia(self):
        return self.__usia
    
    def set_nama(self, nama):
        if not nama.strip():
            raise ValueError("Kesalahan: Nama tidak boleh kosong.")
        self.__nama = nama
    
    def set_usia(self, usia):
        if not usia.strip():
            raise ValueError("Kesalahan: Usia tidak boleh kosong.")
        self.__usia = usia

class Kucing(Hewan):
    def bersuara(self):
        return "Meong!"

class Anjing(Hewan):
    def bersuara(self):
        return "Guk guk!"

class Gajah(Hewan):
    def bersuara(self):
        return "Uooooo!"

def utama():
    daftar_hewan = []
    while True:
        print("\nPilih aksi:")
        print("1. Tambah hewan")
        print("2. Tampilkan daftar hewan")
        print("3. Keluar")
        
        try:
            pilihan = input("Masukkan pilihan (1/2/3): ").strip()
            if pilihan not in {"1", "2", "3"}:
                raise ValueError("Kesalahan: Pilihan tidak valid.")
            
            if pilihan == "1":
                nama = input("Masukkan nama hewan: ")
                usia = input("Masukkan usia hewan : ")
                print("Jenis hewan: 1. Kucing, 2. Anjing, 3. Gajah")
                jenis = input("Masukkan nomor jenis hewan: ").strip()
                
                if jenis == "1":
                    hewan = Kucing(nama, usia)
                elif jenis == "2":
                    hewan = Anjing(nama, usia)
                elif jenis == "3":
                    hewan = Gajah(nama, usia)
                else:
                    raise ValueError("Kesalahan: Jenis hewan tidak valid.")
                
                daftar_hewan.append(hewan)
                print(f"Hewan {hewan.get_nama()} berhasil ditambahkan!")
            
            elif pilihan == "2":
                if not daftar_hewan:
                    print("Tidak ada hewan di dalam daftar.")
                else:
                    print("\nDaftar Hewan:")
                    for i, hewan in enumerate(daftar_hewan, 1):
                        print(f"{i}. {hewan.get_nama()} ({hewan.get_usia()}) - Suara: {hewan.bersuara()}")
            
            elif pilihan == "3":
                print("Keluar dari program.")
                break
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    utama()