# DAFTAR_BUKU

daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
print('\n#.Tampilkan Variable daftar_buku' )
print(daftar_buku)


for buku in (daftar_buku):
    print(buku)

print('\n#.Tampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\n#.Tampilkan dengan for i range')
for i in range(0,len (daftar_buku)):
    print(daftar_buku[i])

daftar_buku =[ 1, 'Kenzi 2',313,-312]
print('\n#.Tampilkan dengan for i range, dimana tipe data tiap elemen berbeda2')
for i in range(0,len (daftar_buku)):
    print(daftar_buku[i])

print('\n#.Kembalikan Nilai awal daftar_buku')
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
for i in range(0,len (daftar_buku)):
    print(daftar_buku[i])

print('\n#.Tambahkan 1 Buku Baru')
daftar_buku.append ('Dasar Pemograman python')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n#.Clear List')   ## perintah clear untuk menghapus list
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n#.Ganti Elemen Pertama')
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
daftar_buku[0] = 'belajar Tazwid'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\n#.Ambil Elemen Ke-2')
buku = daftar_buku.pop(1)  # perintah pop mengambil elemen di bagian list ke ?
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n#.Pop artinya yang diambil')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\n#.Pop-1 artinya sisa yang diambil dari paling ujung')
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n#Perintah del')
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah'] # tambahkan nomer urut ke bawah gimana?
del daftar_buku[1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\n#.Perintah del dengan list comprehension') # Pertanyaan : Pengen ada keterangan BUKU SUDAH DIHAPUS gimana?
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\n#.Perintah del dengan list comprehension start') # Pertanyaan : Pengen ada keterangan BUKU SUDAH DIHAPUS gimana?
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
del daftar_buku[0:3] # note : index dihitung dari nol tetapi jumlah tetap dihitung dari satu
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i]) # penjelasan kodenya : Daftar Buku yang akan dihapus 1-3 menyisakan buku terakhir


