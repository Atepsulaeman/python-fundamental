"""
Program Perulangan membaaca buku dengan while sampai paham undifined with undefined count
"""
jumlah_buku = 10
print(f'jumlah Buku {jumlah_buku}')#penambahan impropisasi
print('Ibu berkata, "baca semua buku')
total_jumlah_baca = 0

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9 :
        print(f"Buku Ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else :
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku Ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipaham")





## while : selama kondisi belum terpenuhi maka program berjalan sampai kondisi terpenuhi #


