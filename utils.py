import hashlib

class Utils:

    @staticmethod
    def getTextAndKey(filePath, keyPath):
        textFile = open(filePath, "r")
        keyFile = open(keyPath, "r")

        encryptedText = textFile.read()
        key = Utils.handleKey(keyFile.read())

        textFile.close()
        keyFile.close()

        return encryptedText, key
        
    @staticmethod
    def handleKey(key):
        sha256 = hashlib.sha256()

        sha256.update((key).encode('utf8'))
        keyValue = sha256.hexdigest()

        keySum = 0
        for n in str(int(keyValue, 16)):
            keySum += int(n)

        return keySum