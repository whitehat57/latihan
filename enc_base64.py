import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert hex to bytes
byte_data = bytes.fromhex(hex_string)

# Step 2: Encode bytes to base64
b64_encoded = base64.b64encode(byte_data)

# Step 3: Convert bytes to string (printable)
print(b64_encoded.decode())
