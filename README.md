# simple-rsa
Self made RSA scripts to generate keys, encrypt and decrypt data, and brute force the private key. Only integer values can be encrypted and decrypted using these codes. The public key counts as (n,e) and private keys count as (n,d) which are seperate values. 

# Generate Keys
[generate_rsa_keys](https://github.com/arpitaga04/simple-rsa/blob/master/generate_rsa_keys.py)

# Encrypt / Decrypt Data
[encrypt_decrypt_rsa](https://github.com/arpitaga04/simple-rsa/blob/master/encrypt_decrypt_rsa.py)

# Brute Force Private Key
NOTE : The keys generated by the code above are of a very short length. This can easily brute force. But in the actual scenario, it is almost impossible to brute the RSA keys.
[brute_force_rsa_privatekey](https://github.com/arpitaga04/simple-rsa/blob/master/brute_force_rsa_privatekey.py)
