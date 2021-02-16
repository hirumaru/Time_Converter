def timeconverter(Q):
    jam = Q//3600
    mod_jam=Q%3600
    menit=mod_jam//60
    mod_menit=mod_jam%60
    detik=mod_menit
    return "%02d:%02d:%02d" % (jam, menit, detik)
try:    
    Q=input("Masukkan detik :")
    Q=int(Q)
    if Q > 359999:
        print("Invalid Input!")
    elif Q < 0:
        print("Invalid Input!")
    else:
        print(timeconverter(Q))
except:
    print("Invalid Input!")

