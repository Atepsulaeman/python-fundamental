# DAFTAR_BUKU

daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
print('\nTampilkan Variable daftar_buku' )
print(daftar_buku)


for buku in (daftar_buku):
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for i range')
for i in range(0,len (daftar_buku)):
    print(daftar_buku[i])

daftar_buku =[ 1, 'Kenzi 2',313,-312]
print('\nTampilkan dengan for i range, dimana tipe data tiap elemen berbeda2')
for i in range(0,len (daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan Nilai awal daftar_buku')
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
print('\nTambahkan 1 Buku Baru')
daftar_buku.append ('Dasar Pemograman python')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
