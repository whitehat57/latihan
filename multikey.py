from binascii import unhexlify
from pwn import xor

# Given values
KEY1 = unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_XOR_KEY1 = unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_XOR_KEY3 = unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FINAL_XOR = unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Step 1: Recover KEY2
KEY2 = xor(KEY1, KEY2_XOR_KEY1)

# Step 2: Recover KEY3
KEY3 = xor(KEY2_XOR_KEY3, KEY2)

# Step 3: XOR KEY1 ^ KEY2 ^ KEY3
COMBINED_KEYS = xor(KEY1, KEY2, KEY3)

# Step 4: FLAG = FINAL_XOR ^ COMBINED_KEYS
FLAG = xor(FINAL_XOR, COMBINED_KEYS)

print(f"crypto{{{FLAG.decode()}}}")
