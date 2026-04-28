import sys

def caesar_encrypt(plaintext, shift):
    filtered = [ch for ch in plaintext.upper() if ch.isalpha()]
    
    encrypted = []
    for ch in filtered:
        shifted = ord(ch) + shift
        if shifted > ord('Z'):
            shifted -= 26
        encrypted.append(chr(shifted))

        encrypted_text = ''.join(encrypted)

        result_lines = []
        for i in range(0, len(encrypted_text), 5):
            block = encrypted_text[i:i+5]
            if len(result_lines) == 0 or len(result_lines[-1].split()) == 10:
                result_lines.append(block)
            else:
                result_lines[-1] += ' ' + block
        return '\n'.join(result_lines)
def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 mycipher.py <shift>\n")
        sys.exit(1)

    try:
        shift = int(sys.argv[1]) % 26
    except ValueError:
        sys.stderr.write("Shift must be an integer\n")
        sys.exit(1)
    plaintext = sys.stdin.read()

    encrypted_output = caesar_encrypt(plaintext, shift)
    print(encrypted_output)

if __name__ == "__main__":
    main() 