from hashlib import sha256

a_string = 'this string holds important and private information'


image_file = input("Enter file location :")

def image_hash(image_file):
    try:
        with open(image_file,"rb") as f:
            bytes = f.read() # read entire file as bytes
            readable_hash = sha256(bytes).hexdigest();
            print(readable_hash)
    except FileNotFoundError:
        print("File Not Found🤦")            

image_hash(image_file)