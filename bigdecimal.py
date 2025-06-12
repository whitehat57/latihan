from Crypto.Util.number import long_to_bytes

n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Konversi dari long integer ke byte string
byte_data = long_to_bytes(n)

# Decode ke ASCII
flag = byte_data.decode()

print(flag)
