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
    def unshift_array(definer, shifted):
        if not shifted:
            return []
        
        shift = definer % len(shifted)
        return shifted[shift:] + shifted[:shift]

    def decrypt(self, definer, ciphertext):
        ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
        coords = []

        for char in ciphertext:
            if char in self.square:
                coords.append(self.square[char])

        length = len(coords) * 2
        merged = [coord[0] for coord in coords] + [coord[1] for coord in coords]
        
        count = 0
        for n in str(definer):
            count += int(n)

        merged_unshifted = self.unshift_array(count, merged)
        
        half = length // 2
        rows = merged_unshifted[:half]
        cols = merged_unshifted[half:]

        original_coords = [(rows[i], cols[i]) for i in range(len(rows))]

        plaintext = ''.join(self.reverse_square[coord] for coord in original_coords)
        return plaintext

if __name__ == "__main__":
    cipher = BifidCipher()
    
    if len(sys.argv) < 3:
        print("Erro de argumentos")
        print("Uso: python bifid-decrypt.py <texto cifrado> <chave>")
        exit(1)

    filePath = sys.argv[1]
    keyPath = sys.argv[2]

    encryptedText, keyValue = Utils.getTextAndKey(filePath, keyPath)

    decryptedText = cipher.decrypt(keyValue, encryptedText)

    outputFile = open("output.txt", "w")
    outputFile.write(decryptedText)
    outputFile.close()
