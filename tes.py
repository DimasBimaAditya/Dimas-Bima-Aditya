nama = 'dimas bima aditya' #string
usia = 30 #integer
tinggi_badan = 170.5 #float

a = input('masukkan angka pertama')#output str
b = input('masukkan angka kedua')#output str 
c = int(a) / int(b) #syntax operator aritmatika /*+-

saldo_awal = input('berapa sadldo awalmu:')
deposit = input('berapa mau depositnya...')
saldo_akhir =  int(saldo_awal) + int(deposit)

punya_pacar = True#boolean
punya_pacar = False#boolean
Pacar = ['dwi', 'novira']#array of string

input_nama = input('Halo siapa kamu')#input

print('HALO...' + input_nama)
print('halo semua nama saya...'+ nama)
print('halo semua usia saya...' + str(usia))
print('halo tinggi saya...'+ str(tinggi_badan) + 'cm')
print('punya pacar...'+ str(punya_pacar))
print('hasil adalah...' + str(c))
print(saldo_akhir)
print(nama.find('a')) #mencari sebuah karakter di dalam sebuah kalimat string
print(len(nama)) #menghitung panjang karakter string
print('d' in (nama)) #mencari TRUE / FALSE dari sebuah string karakter
print(nama.count('d')) #menghitung jumlah karakter dalam sebuah string
print(Pacar[0]) #print sesuai indeks array

for cewe in Pacar:
     print(cewe) #print pisah line

if usia <= 20 and usia >= 20: #perbandingan == , >= , <= , !=
     print('yomann dah legal')
elif usia > 20 and usia <= 50:
     print('KETUAAN')
else:
     print('ASUUUU')
