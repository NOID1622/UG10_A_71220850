print("=====selamat datang di toko andi tersenyum, selamat belanja!=====")
a = int(input("total belanja Rp:"))
if a < 100000:
    print("biaya yang dibayyar setelah diskon adalah: Rp",a)
elif a >= 100000:
    print("biaya yang dibayyar setelah diskon adalah: Rp",a-(a*0.02))
elif a >= 500000:
    print("biaya yang dibayyar setelah diskon adalah: Rp",a-(a*0.05))
elif a >= 1000000:
    print("biaya yang dibayyar setelah diskon adalah: Rp",a-(a*0.010))
else:
    print("beli apa oi")
