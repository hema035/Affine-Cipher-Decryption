import string
from collections import Counter

# Approximate letter frequencies in English text
LETTER_FREQ = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3,
    'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4,
    'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0,
    'K': 0.8, 'X': 0.2, 'J': 0.2, 'Q': 0.1, 'Z': 0.1
}

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No inverse exists

def decrypt_affine(text, a, b):
    """Applies Affine Cipher decryption."""
    a_inv = mod_inverse(a, 26)
    if not a_inv:
        return None

    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new_char = (a_inv * (ord(ch) - base - b) % 26) + base
            result.append(chr(new_char))
        else:
            result.append(ch)

    return ''.join(result)

def chi_squared(text):
    """Computes a chi-squared score to compare letter distribution."""
    text = text.upper()
    count = Counter(filter(str.isalpha, text))
    total = sum(count.values())

    if total == 0:
        return float('inf')  # Avoid division by zero

    score = 0
    for letter, expected in LETTER_FREQ.items():
        observed = (count.get(letter, 0) / total) * 100
        score += ((observed - expected) ** 2) / expected

    return score

def find_best_key(text):
    """Tries all valid (a, b) pairs to find the best decryption."""
    best_a, best_b = None, None
    best_text = None
    lowest_score = float('inf')

    for a in range(1, 26):
        if gcd(a, 26) == 1:
            for b in range(26):
                decrypted = decrypt_affine(text, a, b)
                if decrypted:
                    score = chi_squared(decrypted)
                    if score < lowest_score:
                        best_a, best_b = a, b
                        best_text = decrypted
                        lowest_score = score

    return best_a, best_b, best_text

if __name__ == "__main__":
    cipher = input("Enter ciphertext: ").strip()
    
    a, b, plaintext = find_best_key(cipher)
    
    if a is not None:
        print(f"Best key: a={a}, b={b}")
        print(f"Decrypted text:\n{plaintext}")
    else:
        print("No valid decryption found.")
