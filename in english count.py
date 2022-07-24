"""
Python : while  undifined with undefined count
"""
book_count = 10
print(f'number of books {book_count}')#penambahan impropisasi
print('mom says, "read all books')
read_count = 0

amount_understood = 0
print(f'number of books read and understood {amount_understood}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if amount_understood  == 9 :
        print(f"book to {amount_understood + 1} not understand yet")
    else :
        amount_understood = amount_understood + 1
        print(f"book to {amount_understood} read and understood")

print(f'amount understood {amount_understood}')
if amount_understood == book_count :
    print('"Mom All Books Have been read and understood ')
else:
    print(f'"Mother Not all books can be understood. Only jordan can understand {amount_understood} Books')

## while : selama kondisi belum terpenuhi maka program berjalan sampai kondisi terpenuhi #



print("**note : An infinite number of while loops with variable stops")
