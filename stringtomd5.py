#Made with python3
import hashlib
str = input("Enter a word:") 
str = str.encode(encoding="utf-8")
str = hashlib.md5(str)
print("Hash of the entered string is ",end="")
print(str.hexdigest())

