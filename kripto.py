# Fungsi untuk mencari gcd (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Fungsi untuk mencari invers modular dari a modulo m
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk enkripsi Affine Cipher
def affine_encrypt(text, a, b):
    # Cek apakah a dan 26 adalah coprime (relatif prima)
    if gcd(a, 26) != 1:
        raise ValueError("a and 26 are not coprime, please choose a different a.")
    
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                # Enkripsi huruf kapital
                encrypted_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            else:
                # Enkripsi huruf kecil
                encrypted_text += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
        else:
            # Tambahkan karakter tanpa enkripsi
            encrypted_text += char
    return encrypted_text

# Fungsi untuk dekripsi Affine Cipher
def affine_decrypt(cipher, a, b):
    # Cek apakah a dan 26 adalah coprime (relatif prima)
    if gcd(a, 26) != 1:
        raise ValueError("a and 26 are not coprime, please choose a different a.")
    
    # Hitung invers modular dari a
    a_inv = mod_inverse(a, 26)
    decrypted_text = ''
    for char in cipher:
        if char.isalpha():
            if char.isupper():
                # Dekripsi huruf kapital
                decrypted_text += chr(((a_inv * ((ord(char) - ord('A') - b)) % 26) + 26) % 26 + ord('A'))
            else:
                # Dekripsi huruf kecil
                decrypted_text += chr(((a_inv * ((ord(char) - ord('a') - b)) % 26) + 26) % 26 + ord('a'))
        else:
            # Tambahkan karakter tanpa dekripsi
            decrypted_text += char
    return decrypted_text

# Fungsi untuk kriptoanalisis Affine Cipher (brute force)
def affine_cryptanalysis(cipher):
    possible_solutions = []
    for a in range(1, 26):
        if gcd(a, 26) == 1:
            for b in range(26):
                # Dekripsi dengan setiap kombinasi a dan b
                decrypted_text = affine_decrypt(cipher, a, b)
                # Simpan hasil dekripsi beserta nilai a dan b yang digunakan
                possible_solutions.append((a, b, decrypted_text))
    return possible_solutions

# Contoh penggunaan
if __name__ == "__main__":
    text = "MUHAMMAD RIZIQ SUSANTO"
    a = 5
    b = 8

    # Enkripsi teks
    encrypted = affine_encrypt(text, a, b)
    print(f"Encrypted: {encrypted}")

    # Dekripsi teks
    decrypted = affine_decrypt(encrypted, a, b)
    print(f"Decrypted: {decrypted}")

    # Kriptoanalisis dengan brute force
    cipher_text = encrypted
    solutions = affine_cryptanalysis(cipher_text)
    print("Possible solutions:")
    for sol in solutions:
        print(f"a = {sol[0]}, b = {sol[1]}, decrypted_text = {sol[2]}")