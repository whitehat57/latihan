hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert hex to bytes
byte_data = bytes.fromhex(hex_string)

# Decode bytes to string
flag = byte_data.decode()

print(flag)
