#alpa = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',
#        14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',}
print("Perkalian Matrrik 3x1 dan menentukan CHIPERTEXTnya per 3 kolom ")
print("Berikut gambaran dari program ini")
print(20*"+")
print('|','a','b','c','|','     |','j','|')
print('|','d','e','f','|',' X   |','k','|')
print('|','a','b','c','|','     |','l','|')

alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z']
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

d = int(input("d :"))
e = int(input("e :"))
f = int(input("f :"))

g = int(input("g :"))
h = int(input("h :"))
i = int(input("i :"))

selesai = False
while selesai is not True:
    j = int(input("Masukan J:"))
    k = int(input("Masukan K:"))
    l = int(input("Masukan L:"))
    matrik1 = (a * j) + (b * k) + (c * l)
    matrik2 = (d * j) + (e * k) + (f * l)
    matrik3 = (g * j) + (h * k) + (i * l)
    akhir1 = matrik1 % 26
    akhir2 = matrik2 % 26
    akhir3 = matrik3 % 26
    for indeks,data in enumerate(alpa):
        if indeks is akhir1:
            #aktifkan saat troubleshooting
            #print("Hasil", matrik2)
            akhir1a=indeks
            akhir1b = data
        if indeks is akhir2:
            # aktifkan saat troubleshooting
            #print("Hasil", matrik2
            akhir2a = indeks
            akhir2b = data
        if indeks is akhir3:
            # aktifkan saat troubleshooting
            #print("Hasil", matrik3)
            akhir3a = indeks
            akhir3b = data
    print("HASIL H adalah index ke:",akhir1a,"dengan huruf",akhir1b)
    print("HASIL I adalah index ke:", akhir2a, "dengan huruf", akhir2b)
    print("HASIL J adalah index ke:", akhir3a, "dengan huruf", akhir3b)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Ctrl+C untuk Mengakhiri")
    print("+++++++++++++++++++++++++++++++++++++++")



