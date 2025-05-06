# 🔐 Affine Cipher Decryption using Frequency Analysis

## 📌 Overview
This project implements a decryption tool for the Affine Cipher using **brute-force key search** combined with **frequency analysis** to determine the most probable English plaintext. It uses statistical scoring to evaluate letter frequency patterns and identify the correct decryption key.

## 🛠 Tools & Technologies
- **Python** 🐍
- String Manipulation
- Frequency Analysis (Chi-Squared Scoring)

## 📖 How It Works
1. **Brute Force Key Search**: Tries all valid `(a, b)` pairs where `gcd(a, 26) = 1`.
2. **Frequency Comparison**: Analyzes the frequency of letters in the decrypted text.
3. **Chi-Squared Scoring**: Scores each decryption based on how closely it matches standard English letter frequencies.
4. **Best Match Selection**: The decryption with the lowest chi-squared score is chosen as the most likely plaintext.

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Affine-Cipher-Decryption.git
2.Navigate to the project directory:
 ```bash
cd Affine-Cipher-Decryption




