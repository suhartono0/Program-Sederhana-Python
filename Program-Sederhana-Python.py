#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##bangun datar
d1 = int(input("Diameter 1 :"))
d2 = int(input("Diameter 2 :"))
sisi = int(input ("Sisi :"))

luas = (d1*d2)/2
keliling = 4 * sisi

print ("luas : ", luas)
print ("keliling :",keliling)


# In[7]:


bil1 = input("masukan angka pertama :")
bil2 = input("masukan angka kedua : ")

jumlah = float (bil1)+float (bil2)

print ('jumlah angka {0} + angka {1} adalah {2}'.format (bil1,bil2,jumlah))


# In[9]:


panjang = int (input("panjang : "))
lebar = int(input("lebar : "))
tinggi = int(input("tinggi : "))

luas = lebar*tinggi
keliling = (2*panjang)+(2*lebar)

print ("luas : ",luas)
print ("Keliling : ",keliling)


# In[18]:


panjang = int(input("Panjang : "))
lebar = int(input("Lebar : "))
d1 = int(input("Diameter 1 : "))
d2 = int(input("Diameter 2 : "))

luas = (d1*d2)/2
keliling = (2*panjang) + (2*lebar)

print("Luar = ", luas)
print("Keliling = ", keliling)


# In[17]:


jari = int(input("Jari-jari : "))
diameter = int(input("Diameter : "))

print("Luas = ", (3.14*jari)**2)
print("Keliling = ", 2*3.14*jari)


# In[16]:


sisi = int(input("Masukkan Sisi : "))

luas = sisi*sisi
keliling = 4*sisi

print("Luas Persegi = ", luas)
print("Luas Persegi = ", keliling)


# In[14]:


panjang = int(input("Panjang : "))
lebar = int(input("Lebar : "))

luas = panjang*lebar
keliling = (2*panjang) + (2*lebar)

print("Luas : ", luas)
print("Keliling", keliling)


# In[13]:


alas = int(input("Alas : "))
tinggi = int(input("Tinggi : "))
lebar = int(input("Lebar : "))

keliling = alas+tinggi+lebar
luas = (alas*tinggi)/2

print("Luas Segitiga Adalah : ", luas)
print("Keliling Segitiga Adalah : ", keliling)


# In[12]:


sisi1 = int(input("Sisi 1 : "))
sisi2 = int(input("Sisi 2 : "))
sisi3 = int(input("Sisi 3 : "))
tinggi = int(input("Tinggi : "))

luas = (sisi1+sisi2) * tinggi / 2
keliling = sisi1+sisi2+sisi3+tinggi

print("Luas = ", luas)
print("Keliling =", keliling)


# In[ ]:


# Bangun Ruang

lebar = int(input("Lebar : "))
luas = panjang * lebar
print("Luas = ", luas)


# In[11]:


rusuk = int(input("Rusuk  : "))

print("Luas = ", 6*(rusuk**2))
print("volume = ", rusuk*rusuk*rusuk)


# In[4]:


#fundametal
print("--selain itu jika--")

print("--contoh 1, negatif, nol dan bulat menggunakan elif--")
d = 0
if d<0:
    print("Negatif")
elif d >0:
    print("Positif")
else:
    print("Nol")


# In[5]:


print("--if berarti jika maka--")

a = 76
if a >= 75:
    print("Kamu Kompeten")
else:
    print("Kamu Belum Kompeten")


print("---Penggunaan IF----")
n = 10
if n == 1:
    print("Nilai Sama")
else:
    print("Tidak Sama")


# In[6]:


print("--selain itu/lawan dari if--")

print("--contoh 1, kompeten dan belum kompeten--")
a = 72
if a>=75:
    print("Kamu Kompeten")
else:
    print("Kamu Belum Kompeten")

print("--contoh 2, benar salah--")
b=0
if b==1:
    print("Benar")
if b==0:
    print("Salah")





print("--contoh 3, ganjil genap--")
c = 1
if c%2 == 0:
    print("Genap")
else:
    print("Ganjil")







print("--contoh 4, negatif, nol dan bulat--")
e = -3
if e<0:
    print("Negatif")
else:
    print("Positif")

d = -100
if d<0:
    print("Negatif")
if d==0:
    print("Nol")
if d>0:
    print("Positif")

print("--contoh 5, Libur dan Masuk--")
hari = "merah"
if hari == "merah":
    print("Libur")
else:
    print("Masuk")


# In[7]:


print("Selamat Datang")
"""komentar jg"""

"""kutip 3 juga sebagai komentar"""

print("Python")


# In[8]:


print("----For----")
for a in [1,2,3]:
    print(a)

print("----While----")
b = 1
while b < 10:
    print(b)
    b+=1


# In[9]:


print("--contoh 3, Nilai A, B, C--")
n = 55
if n >= 80: #80-100
    print("A")
elif n >=75: #75-79
    print("B")
elif n >=70: #70-74
    print("C")
else: #<=69
    print("D")


# In[15]:


nil =int(input("Masukkan Nilai : "))
if nil >= 80:
    print("A")
else:
    print("B")


# In[16]:


print("--Operator Matematika--")
print("Tambah (+)", 10+2)
print("Kali (*)", 12*2)
print("Bagi (/)", 8/5)
print("Kurang (-)", 14-1)
print("Pangkat (+)", 2**2)
print("Mod (%)", 6%2)

print("--Operator Pembanding--")
print("Sama Dengan (==)")
print("Lebih Besar (>)")
print("Lebih Kecil (<)")
print("Lebih Besar Sama Dengan (>=)")
print("Lebih Kecil Sama Dengan(<=)")
print("Tidak Sama Dengan(!=)")

print("--Operator Logika--")
print("Not (not=Bukan)")
print("And (and=Semua Kondisi Terpenuhi)")
print("Or (or=Salah Satu Kondisi Terpenuhi)")


# In[17]:


print ("Selamat Datang")
print ("Belajar Bahasa Pemrograman Python")

print ("hello !")


# In[18]:


print('Selamat Datang')
print("Selamat Datang")
print('Selamat Datang')
print("Selamat Datang")
print('Selamat Datang')
print("Selamat Datang")
print('Selamat Datang')
print("Selamat Datang")


# In[19]:


#BELAJAR PYTHON
"""BELAJAR PYTHON"""



a = 1
b = 2
c = 'Selamat Datang di'
d = "SMK Wikrama"
e = "Bogor"

#Selamat Datang di SMK Wikrama 2 Bogor
print(c, d, b, e)
#Hasil dari 1+2=3

print("Hasil dari", a, "+",  b, "=", a+b)















print(c, d, a*b)






#tipe data bilangan (bulat/integer dan float)
#bulat/integer
x = 7
print(x)

y = 7.0
print(y)
print(x+y)


#operator
print("-----------operator----------")
print(10+2)
print(12*2)
print(8/5)
print(14-1)
print(2**2)
print(5%2)

print("-----------operator menggunakan variabel----------")
a1 = 5
a2 = 6
print(a1+a2)
print(a1*a2)
print(a2-a1)
print(a1/a2)




print("-----------pengelompokan operasi----------")
print(2+2*4) #operasi perkalian akan di lakukan terlebih dahulu 10
print((2+2)*4) #tanda kurung menandakan operasi yang didahulukan
print((4/2)*5)






print("----pembulatan----")
b1 = 14.8
b2 = 18.4
print(int (b1))  #int pembulatan ke bawah
print(round(b2)) #round pembulatan ke atas jika > 5, ke bawah jika <= 5





print("---------tipe data string---------")
print('SMK Wikrama Bogor') #string menggunakan kutip 1 atau kutip 2
print("SMK Wikrama Bogor")







print("doesn't")
print('doesn\'t')
print('i cant wait')
print('i can\'t wait')
print("i can't wait")








print("""SMK Wikrama Bogor
Jl. Raya Wangun Kel. Sindangsari
Kec. Bogor Timur Kota Bogor""")   #kutip 3 bisa digunakan untuk string untuk kondisi beberapa baris

#print("SMK Wikrama Bogor
#Jl. Raya Wangun Kel. Sindangsari
#Kec. Bogor Timur Kota Bogor")



print("---menggabungkan string menggunakan (+)---")
c1 = "SMK"
c2 = "Wikrama"
c3 = "Bogor"
c4 = c1+c2+c3
c5 = c1+' '+c2+' '+c3
print(c4)
print(c5)
print(c1+' '+c2+' '+c3)







print("---menggabungkan angka menggunakan (+)---")
d1 = 1
d2 = 2
d3 = 3
d4 = d1+d2+d3

print(d4)
print(str(d1)+str(d2)+str(d3))
print(str(d1)+'+'+str(d2)+'+'+str(d3))
print(str(d1)+'+'+str(d2)+'+'+str(d3)+'='+str(d4))

print("---Array/List/Larik---")
a = [1,2,3,4,5]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[0],a[1],a[2],a[3],a[4])

e1 = ['Wikrama', 1, 'Bogor']
print(e1[0], e1[1], e1[2])

print("--menghitung jumlah elemen pada array--")
print("jumlah elemen pada array adalah", len(e1))


# In[20]:


#OPERATOR ARITMATIKA
a = 7
b = 2
print(a+b) #hasilnya 9
print(a*b) #hasilnya 14
print(a-b) #hasilnya 5
print(a/b) #hasilnya 3.5
print(a%b) #hasilnya 1
print(a**b) #hasilnya 49

