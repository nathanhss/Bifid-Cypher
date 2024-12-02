import random
import sys


class BifidCipher:
    def __init__(self):
        self.definer = random.randint(11,99)
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

    def shift_array(self, original):
        if not original:
            return []
        
        shift = self.definer % len(original)
        return original[-shift:] + original[:-shift]

    def unshift_array(self, shifted):
        if not shifted:
            return []
        
        shift = self.definer % len(shifted)
        return shifted[shift:] + shifted[:shift]

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        coords = []

        for char in plaintext:
            if char in self.square:
                coords.append(self.square[char])

        rows = [coord[0] for coord in coords]
        cols = [coord[1] for coord in coords]

        merged = rows + cols
        merged_shifted = self.shift_array(merged)

        half = len(coords)
        encrypted_coords = [
            (merged_shifted[i], merged_shifted[i + half]) for i in range(half)
        ]

        encrypted_text = ''.join(self.reverse_square[coord] for coord in encrypted_coords)
        return encrypted_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
        coords = []

        for char in ciphertext:
            if char in self.square:
                coords.append(self.square[char])

        length = len(coords) * 2
        merged = [coord[0] for coord in coords] + [coord[1] for coord in coords]
        merged_unshifted = self.unshift_array(merged)
        
        half = length // 2
        rows = merged_unshifted[:half]
        cols = merged_unshifted[half:]

        original_coords = [(rows[i], cols[i]) for i in range(len(rows))]

        plaintext = ''.join(self.reverse_square[coord] for coord in original_coords)
        return plaintext
    

class cypher2:
    def __init__(self):
        print('cypher to implements')


class cypher3:
    def __init__(self):
        print('cypher to implements')

if __name__ == "__main__":
    cipher = BifidCipher()

    if len(sys.argv) < 2:
        print("Deve passar o nome do arquivo com o texto plano como argumento")
        exit(1)

    fileName = sys.argv[1]

    plaintextFile = open(fileName, "r")

    encryptedText = cipher.encrypt(plaintextFile.read())
    decryptedText = cipher.decrypt(encryptedText)
    plaintextFile.close()

    outputFile = open("output.txt", "w")
    outputFile.write(encryptedText + "\n")
    outputFile.write(decryptedText)
    outputFile.close()
