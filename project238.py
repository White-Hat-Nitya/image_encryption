import hashlib

image1 = "OIP.jpg"
result = hashlib.sha3_256(image1.encode())
print = ("The SHA256 of image1 is : ",result.hexdigest())
read() with open(filename,"rb") as f:
file_data = f.read()
