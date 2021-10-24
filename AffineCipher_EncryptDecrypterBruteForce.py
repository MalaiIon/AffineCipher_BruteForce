import math
import string

def Inverse(ai):
    a_inverse = [x for x in range(0, 26) if math.gcd(1, 26) == 1]
    for i in a_inverse:
        if (ai * i) % 26 == 1: return i

def AffineEncryption(message):
    output = []
    for i in range(len(message)):
        num = ((a * message[i]) + b) % 26
        if num == 0:
            num = 26
        output.append(num)
    return output

def AffineDecryption(encrypted_message, ai, b1):
    output = []
    for i in range(len(encrypted_message)):
        output.append(int(math.ceil((ai * (encrypted_message[i] + 26 - b1)) % 26)))
    return output

def ConvertLettersToNumbers(encrypted_message):
    input_message = encrypted_message.lower().replace(' ', '')
    output = []
    for i in input_message:
        output.append((ord(i) - 97))
    return output

def NumbersToLetters(encrypted_message):
    output = []
    for i in range(len(encrypted_message)):
        output.append(dict((enumerate(string.ascii_lowercase, 0)))[encrypted_message[i]])
    return ''.join(output)


if __name__ == '__main__':
    encrypted_msg, encrypted_msg_1, decrypted_msg, decrypted_msg_1 = 'ejjekiejnusr', 'tjowhkkdxojj', 'attackatdown', 'playfootball'

    # msg, a, b = input("Enter your message: "), int(input("Enter A: ")), int(input("Enter B: "))
    msg, a, b = 'attackatdown', 3, 4

    file = open('hacked.txt', 'w')
    file.write('####@@@@$$$$#### BruteForce Affine Cipher ####@@@@$$$$####\nEncrypted text is "%s", but decrypted text is "%s", where a = 3, b = 4\n'
               'Encrypted text is "%s", but decrypted text is "%s", where a = 9, b = 14\n' % (encrypted_msg, decrypted_msg, encrypted_msg_1, decrypted_msg_1))

    ciphertext = NumbersToLetters(AffineEncryption(ConvertLettersToNumbers(msg)))
    cleartext = NumbersToLetters(AffineDecryption(ConvertLettersToNumbers(ciphertext), Inverse(a), b))
    print('Encrypted message is - "%s", but decrypted "%s"' % (ciphertext, cleartext))

    # Bruteforce Decrypt
    for a in range(0, 26):
        for b in range(0, 25):
            if (a % 2 != 0) and (a != 13):
                file.write('\n# TRYING KEY <%d,%d>\n# MESSAGE : %s\n' % (a, b, NumbersToLetters(AffineDecryption(ConvertLettersToNumbers(encrypted_msg), Inverse(a), b))))
                file.write('\n# TRYING KEY <%d,%d>\n# MESSAGE : %s\n' % (a, b, NumbersToLetters(AffineDecryption(ConvertLettersToNumbers(encrypted_msg_1), Inverse(a), b))))
