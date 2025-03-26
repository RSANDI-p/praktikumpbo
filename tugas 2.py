class ManajerTugas:
    def __init__(self):
        self.daftar_tugas = []
    
    def tambah_tugas(self, tugas):
        if not tugas.strip():
            raise ValueError("Kesalahan: Tugas tidak boleh kosong.")
        self.daftar_tugas.append(tugas)
        print("Tugas berhasil ditambahkan!")
    
    def hapus_tugas(self, nomor):
        if not self.daftar_tugas:
            raise IndexError("Kesalahan: Tidak ada tugas yang dapat dihapus.")
        if nomor < 1 or nomor > len(self.daftar_tugas):
            raise IndexError(f"Kesalahan: Tugas dengan nomor {nomor} tidak ditemukan.")
        tugas_dihapus = self.daftar_tugas.pop(nomor - 1)
        print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
    
    def tampilkan_tugas(self):
        if not self.daftar_tugas:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.daftar_tugas, 1):
                print(f"{i}. {tugas}")

def utama():
    manajer = ManajerTugas()
    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan not in {"1", "2", "3", "4"}:
                raise ValueError("Kesalahan: Pilihan tidak valid.")
            
            if pilihan == "1":
                tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                manajer.tambah_tugas(tugas)
            elif pilihan == "2":
                manajer.tampilkan_tugas()
                nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                manajer.hapus_tugas(nomor)
            elif pilihan == "3":
                manajer.tampilkan_tugas()
            elif pilihan == "4":
                print("Keluar dari program.")
                break
        except ValueError as ve:
            print(ve)
        except IndexError as ie:
            print(ie)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    utama()
