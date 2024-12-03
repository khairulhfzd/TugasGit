data_panen = {
    'lokasil': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
        'padi': 1200,
        'jagung': 800,
        'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
        'padi': 1500,
        'jagung': 900,
        'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
        'padi': 1100,
        'jagung': 750,
        'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
        'padi': 1300,
        'jagung': 850,
        'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
        'padi': 1400,
        'jagung': 950,
        'kedelai': 480
        }
    }
}

#1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
for i in data_panen:
    print(i,data_panen[i])

print("="*50)

#2. Tampilkan jumlah hasil panen jagung dari lokasi2.
print("Jumlah hasil panen jagung dari lokasi2:", data_panen['lokasi2']['hasil_panen']['jagung'])

print("="*50)

#3. Tampilkan nama lokasi dari lokasi3.
print("Nama lokasi dari lokasi3:", data_panen['lokasi3']['nama_lokasi'])

print("="*50)


#4. Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda:
#5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
Hasil_Panen_Padi= {}
Hasil_Panen_Kedelai= {}

for i in data_panen:
    nama_lokasi = data_panen[i]['nama_lokasi']
    Hasil_Panen_Padi[nama_lokasi] = data_panen[i]['hasil_panen']['padi']
    Hasil_Panen_Kedelai[nama_lokasi] = data_panen[i]['hasil_panen']['kedelai']

print(f"Hasil Panen padi:{Hasil_Panen_Padi}")
print(f"Hasil Panen Kedelai:{Hasil_Panen_Kedelai}")

print("="*50)

#6. Buat Percabangan
for i in data_panen:
    nama_lokasi = data_panen[i]['nama_lokasi']
    Hasil_padi = data_panen[i]['hasil_panen']['padi']
    Hasil_kedelai = data_panen[i]['hasil_panen']['jagung']

    if Hasil_padi > 1300 or Hasil_kedelai > 800:
        print(f"Lokasi {nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {nama_lokasi} dalam kondisi baik.")