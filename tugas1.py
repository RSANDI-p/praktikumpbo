def akar(angka):
	return angka ** 0.5

def main():
	while True :
		try:
			angka = int(input("masukan angka : "))

			if angka < 0:
				print("input tidak valid, masukan bilangan positif")
			elif angka == 0:
				print("error: akar kuadrat 0 tidak diperbolehkan")
			else:
				hasil = akar(angka)
				print(f"Akar kuadrat dari {angka} adalah {hasil}")
				break

		except ValueError:
			print("input tidak valid. harap masukkan angka yang valid.")

if __name__ == "__main__":
	main()
