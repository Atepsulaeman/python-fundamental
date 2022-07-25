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

print('\n#.Perintah del dengan list comprehension start : END') # Pertanyaan : Pengen ada keterangan BUKU SUDAH DIHAPUS gimana?
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
del daftar_buku[0:-2] # start : End # note : index dihitung dari nol tetapi jumlah tetap dihitung dari satu,# bisa juga diganti -1 dst = menyisakan paling ujung
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i]) # penjelasan kodenya : Daftar Buku yang akan dihapus 1 sampai 3, menyisakan buku terakhir 2 buku terakhir

print('\n#.Perintah del dengan list comprehension start : END : STEP') # Pertanyaan : Pengen ada keterangan BUKU SUDAH DIHAPUS gimana?
daftar_buku =['Quantum ikhlas','Jalan langit','Secret','Jalan Allah']
del daftar_buku[0: :2] # start : End : STEP # note : ( Menggunakan (: : ) Menghapus meloncati 1 step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

