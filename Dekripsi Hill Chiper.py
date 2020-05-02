he = ''
H = True
tabel = {1: 3,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}
alpa = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',
       14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
print("Dekripsi Hill Chiper")
print("Berikut gambaran dari program ini")
print(20*"+")
print('|','A','B','C','|')
print('|','D','E','F','|')
print('|','G','H','I','|')
print("Nilai Chiper adalah Angka alphabet dari karakter chipertext")


print("Pencari Matriks")
a = int(input(" Nilai A = "))
b = int(input(" Nilai B = "))
c = int(input(" Nilai C = "))
d = int(input(" Nilai D = "))
e = int(input(" Nilai E = "))
f = int(input(" Nilai F = "))
g = int(input(" Nilai G = "))
h = int(input(" Nilai H = "))
i = int(input(" Nilai I = "))

# Mencari Determinan
detA = (a * e * i) + (b * f * g) + (c * d * h) - (g * e * c) - (h * f * a) - (i * d * b)
print("\nMatriks A")
print("| ", a, " ", b, " ", c, " |")
print("| ", d, " ", e, " ", f, " |  ===> DetA = ", detA)
print("| ", g, " ", h, " ", i, " |")
print("--------------------------")

# Mencari Adjoin
a11 = (e * i) - (h * f)
a12 = (d * i) - (g * f)
a13 = (d * h) - (g * e)
a21 = (b * i) - (h * c)
a22 = (a * i) - (g * c)
a23 = (a * h) - (g * b)
a31 = (b * f) - (e * c)
a32 = (a * f) - (d * c)
a33 = (a * e) - (d * b)

# Menampilkan Adjoin
# print("------------------------------------------------------------------------------")
# print("Adj = | ", a11 * (1), "", a12 * (-1), "", a13 * (1), " |")
# print("      | ", a21 * (-1), "", a22 * (1), "", a23 * (-1), " |")
# print("      | ", a31 * (1), "", a32 * (-1), "", a33 * (1), " |")
# print("")

verifikasi = detA % 26
for key in list(tabel.keys()):
    if key == verifikasi:
        nilai = tabel.get(key)
        print(nilai)
        break
else:
    print('Matrik Anda Eroor')
# print("------------------------------------------------------------------------------")
# print("Adj = | ", (nilai*(a11 * (1))), "", (nilai*(a12 * (-1))), "", (nilai*(a13 * (1))), " |")
# print("      | ", (nilai*(a21 * (-1))), "", (nilai*(a22 * (1))), "", (nilai*(a23 * (-1))), " |")
# print("      | ", (nilai*(a31 * (1))), "", (nilai*(a32 * (-1))), "", (nilai*(a33 * (1))), " |")
# print("")

a1k = (nilai * (a11 * (1))) % 26
a2k = (nilai * (a12 * (-1))) % 26
a3k = (nilai * (a13 * (1))) % 26
a4k = (nilai * (a21 * (-1))) % 26
a5k = (nilai * (a22 * (1))) % 26
a6k = (nilai * (a23 * (-1))) % 26
a7k = (nilai * (a31 * (1))) % 26
a8k = (nilai * (a32 * (-1))) % 26
a9k = (nilai * (a33 * (1))) % 26

print("\nMatriks Akhir")
print("| ", a1k, " ", a4k, " ", a7k, " |")
print("| ", a2k, " ", a5k, " ", a8k, " |")
print("| ", a3k, " ", a6k, " ", a9k, " |")
print("--------------------------")


while H == True:

    angka1 = int(input("Masukan Nilai Chiper 1:"))
    angka2 = int(input("Masukan Nilai Chiper 2:"))
    angka3 = int(input("Masukan Nilai Chiper 3:"))
    matrik1 = (a1k * angka1) + (a4k * angka2) + (a7k * angka3)
    matrik2 = (a2k * angka1) + (a5k * angka2) + (a8k * angka3)
    matrik3 = (a3k * angka1) + (a6k * angka2) + (a9k * angka3)
    akhir1 = matrik1 % 26
    #print(akhir1)
    akhir2 = matrik2 % 26
    #print(akhir2)
    akhir3 = matrik3 % 26
    #print(akhir3)
    for key in list(alpa.keys()):
        if key == akhir1:
            huruf1 = alpa.get(key)
        if key == akhir2:
            huruf2 = alpa.get(key)
        if key == akhir3:
            huruf3 = alpa.get(key)

    satuan =str(huruf1+huruf2+huruf3)

    he +=satuan
    print(he)








