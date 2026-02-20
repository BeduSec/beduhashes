# BeduSec/beduhashes

🔐 **MD5 and SHA256 Brute Force Decrypter**  
A multi-language tool to reverse password hashes using brute force — built for educational and security research purposes.

## 🚀 Features

- 🔁 Brute force decryption for **MD5** and **SHA256** hashes
- 🌐 **Web version** (HTML/JavaScript) for quick testing
- 🐍 **Python scripts** for more control and speed
- 🐘 **PHP version** for server-side implementation
- 📚 Includes `rockyou.txt` wordlist (commonly used passwords)

## 📁 Repository Structure

```

beduhashes/
├──web/
│├── index.html      # Main web interface
│└── index2.html      # Alternative version
├──python/
│├── md5_bruteforce.py
│└── sha256_bruteforce.py
├──php/
│├── md5_bruteforce.php
│└── sha256_bruteforce.php
├──wordlists/
│└── rockyou.txt      # Sample wordlist (common passwords)
├──.gitignore
└──README.md

```

> ⚠️ **Note:** Currently uploading Python, PHP, and organized web files. The structure above shows the planned organization.

## 🛠️ How It Works

1. You provide a hash (MD5 or SHA256)
2. The script generates possible passwords (brute force or using wordlist)
3. It compares the hash of each candidate with the target hash
4. If a match is found, the original password is revealed

## ▶️ Usage Examples

### 🌐 Web Version
Simply open `web/index.html` in any browser for client-side brute force demo.

### 🐍 Python

```bash
# Navigate to python folder first
cd python
python md5_bruteforce.py
```

🐘 PHP

```bash
php php/sha256_bruteforce.php
```

📚 Using rockyou.txt wordlist

The included rockyou.txt (truncated version) can be used with any script for dictionary attacks.

⚠️ Important Notes

· rockyou.txt is a sample wordlist (full version is too large for GitHub)
· Web versions run client-side (slower but no server needed)
· Python/PHP versions are faster and support larger wordlists

📚 Educational Purpose Only

This tool is intended for:

· Ethical hacking training
· Password strength analysis
· Academic research

❗ Do not use this tool for illegal or malicious purposes.

🛠️ Installation

```bash
git clone https://github.com/BeduSec/beduhashes.git
cd beduhashes
```

🤝 Contributing

Feel free to open issues or submit pull requests:

· Add new hash types
· Improve brute force algorithms
· Optimize wordlist handling

👤 Author

Icii White
Driven by a deep passion for technology — problem-solver and creator.

🔗 GitHub Profile

📜 License

MIT License — see the LICENSE file for details.

---

⭐ Star this repo if you find it useful!
💬 Questions? Open an issue or start a discussion.

```
