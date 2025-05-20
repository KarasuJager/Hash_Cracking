import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)

print("Algoritm acailabe: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

hash_type = str(input("What's the hash type?"))
wordlist_location = str(input("Enter wordlist location: "))
hash = str(input("Enter hash: "))

word_list = oppen(f"{wordlist_location}").read()
lists = word_list.splitliner()

for word in list:
        if hash_type == "MD5":
                hash_object = hashlib.md5(f"{word}".encode('utf-8'))
                hashes == hash_object.hexdigest()
                if hash == hashes:
                        print(f"\033[1;32m HASH FOUND: {word} \n]")
        elif hash_type == "SH1":
                hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
                hashes == hash_object.hexdigest()
                if hash == hashes:
                        print(f"\033[1;32m HASH FOUND: {word} \n]")
        elif hash_type == "SHA224":
                hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
                hashes == hash_object.hexdigest()
                if hash == hashes:
                        print(f"\033[1;32m HASH FOUND: {word} \n]")
        elif hash_type == "SHA512":
                hash_object = hashlib.sha512(f"{word}".encode('utf-8'))
                hashes == hash_object.hexdigest()
                if hash == hashes:
                        print(f"\033[1;32m HASH FOUND: {word} \n]")
        elif hash_type == "SHA384":
                hash_object = hashlib.sha384(f"{word}".encode('utf-8'))
                hashes == hash_object.hexdigest()
                if hash == hashes:
                        print(f"\033[1;32m HASH FOUND: {word} \n]")
        else:
                print("Please choose from the given option.")