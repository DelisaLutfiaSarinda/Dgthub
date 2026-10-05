tunai = False
qris = False

valid = tunai ^ qris

if valid:
    print("Pembayaran valid")
else:
    print("Pembayaran tidak valid")