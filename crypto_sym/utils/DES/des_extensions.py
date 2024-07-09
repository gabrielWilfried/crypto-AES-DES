class TripleDes:
    def __init__(self, des1, des2, des3):
        self.des1 = des1
        self.des2 = des2
        self.des3 = des3

    def encrypt(self, key1, key2,key3, text, padding=False):
        encrypted_text = self.des1.encrypt(key1, text, padding=padding)
        encrypted_text = self.des2.decrypt(key2, encrypted_text, padding=False)  # Decrypt with key2
        encrypted_text = self.des3.encrypt(key3, encrypted_text, padding=False)  # Encrypt with key1
        return encrypted_text

    def decrypt(self, key1, key2, key3, text, padding=False):
        decrypted_text = self.des1.decrypt(key3, text, padding=padding)
        decrypted_text = self.des2.encrypt(key2, decrypted_text, padding=False)  # Encrypt with key2
        decrypted_text = self.des3.decrypt(key1, decrypted_text, padding=False)  # Decrypt with key1
        return decrypted_text

class DoubleDes:
    def __init__(self, des1, des2):
        self.des1 = des1
        self.des2 = des2

    def encrypt(self, key1, key2, text, padding=False):
        encrypted_text = self.des1.encrypt(key1, text, padding=padding)
        encrypted_text = self.des2.decrypt(key2, encrypted_text, padding=False)  # Decrypt with key2
        encrypted_text = self.des1.encrypt(key1, encrypted_text, padding=False)  # Encrypt with key1
        return encrypted_text

    def decrypt(self, key1, key2, text, padding=False):
        decrypted_text = self.des1.decrypt(key1, text, padding=padding)
        decrypted_text = self.des2.encrypt(key2, decrypted_text, padding=False)  # Encrypt with key2
        decrypted_text = self.des1.decrypt(key1, decrypted_text, padding=False)  # Decrypt with key1
        return decrypted_text
