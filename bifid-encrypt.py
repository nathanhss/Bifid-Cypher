import sys
from utils import Utils

class BifidCipher:
    def __init__(self):
        self.square, self.reverse_square = self.create_polybius_square()

    @staticmethod
    def create_polybius_square():
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        square = {}
        reverse_square = {}
        size = 5 
        for index, letter in enumerate(alphabet):
            row, col = divmod(index, size)
            square[letter] = (row + 1, col + 1)
            reverse_square[(row + 1, col + 1)] = letter

        return square, reverse_square
    
    @staticmethod
    def shift_array(definer, original):
        if not original:
            return []
        
        shift = definer % len(original)
        return original[-shift:] + original[:-shift]

    def encrypt(self, plaintext, definer):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        coords = []

        for char in plaintext:
            if char in self.square:
                coords.append(self.square[char])

        rows = [coord[0] for coord in coords]
        cols = [coord[1] for coord in coords]

        merged = rows + cols

        count = 0
        for n in str(definer):
            count += int(n)

        merged_shifted = self.shift_array(count, merged)

        half = len(coords)
        encrypted_coords = [
            (merged_shifted[i], merged_shifted[i + half]) for i in range(half)
        ]

        encrypted_text = ''.join(self.reverse_square[coord] for coord in encrypted_coords)
        return encrypted_text

if __name__ == "__main__":
    cipher = BifidCipher()

    if len(sys.argv) < 3:
        print("Erro de argumentos")
        print("Uso: python bifid-encrypt.py <texto plano> <chave>")
        exit(1)

    filePath = sys.argv[1]
    keyPath = sys.argv[2]

    plainText, keyValue = Utils.getTextAndKey(filePath, keyPath)

    encryptedText = cipher.encrypt(plainText, keyValue)

    outputFile = open("encrypted_text.txt", "w")
    outputFile.write(encryptedText)
    outputFile.close()
