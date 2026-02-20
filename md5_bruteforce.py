import hashlib
import os
import sys
import urllib.request

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def print_banner():
    # Using \u2800 (Braille Blank) for invisible spacing
    banner = f"""\n\n MD5  DECRYPTER PRO - by BeduSec Security Systems\n"""
    print("\033[96m" + banner + "\033[0m")
    print("\033[94m" + "—" * get_terminal_width() + "\033[0m")

def download_wordlist(url, dest):
    try:
        print(f"\033[93m[*] Fetching remote wordlist from: {url}\033[0m")
        urllib.request.urlretrieve(url, dest)
        print("\033[92m[+] Download complete.\033[0m")
        return True
    except Exception as e:
        print(f"\033[91m[!] Error fetching wordlist: {e}\033[0m")
        return False

def count_lines(filename):
    with open(filename, 'rb') as f:
        return sum(1 for _ in f)

def main():
    clear_screen()
    print_banner()
    
    target_hash = input("\033[95m[?] Enter MD5 Hash: \033[0m").strip().lower()
    if len(target_hash) != 32 or not all(c in '0123456789abcdef' for c in target_hash):
        print("\033[91m[!] Invalid MD5 hash format.\033[0m")
        return

    choice = input("\033[95m[?] Use rockyou.txt? (y/n): \033[0m").strip().lower()
    
    wordlist_path = "rockyou.txt"
    
    if choice == 'y':
        if not os.path.exists(wordlist_path):
            print("\033[93m[!] rockyou.txt not found locally.\033[0m")
            rockyou_url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
            if not download_wordlist(rockyou_url, wordlist_path):
                return
    else:
        wordlist_path = input("\033[95m[?] Enter local path or URL to wordlist: \033[0m").strip()
        if wordlist_path.startswith("http"):
            url_target = wordlist_path
            wordlist_path = "custom_list.txt"
            if not download_wordlist(url_target, wordlist_path):
                return
        elif not os.path.exists(wordlist_path):
            print(f"\033[91m[!] File {wordlist_path} not found.\033[0m")
            return

    print("\033[94m[*] Indexing wordlist...\033[0m")
    try:
        total_lines = count_lines(wordlist_path)
    except Exception as e:
        print(f"\033[91m[!] Error reading file: {e}\033[0m")
        return

    print(f"\033[92m[+] Loaded {total_lines:,} passwords.\033[0m")
    print("\033[94m[*] Cracking started...\033[0m")
    
    found = None
    tested = 0
    
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                pwd = line.strip()
                if not pwd:
                    continue
                
                tested += 1
                if hashlib.md5(pwd.encode()).hexdigest() == target_hash:
                    found = pwd
                    break
                
                if tested % 50000 == 0:
                    prog = (tested / total_lines) * 100
                    sys.stdout.write(f"\r\033[93m[*] Progress: {prog:.2f}% ({tested:,} / {total_lines:,})\033[0m")
                    sys.stdout.flush()

        sys.stdout.write("\r" + " " * 60 + "\r")
        print("\033[94m" + "—" * get_terminal_width() + "\033[0m")
        
        if found:
            print(f"\033[92mSUCCESS: Password found!\033[0m")
            print(f"\033[1m>> {found}\033[0m")
            print(f"\033[90mTested {tested:,} entries.\033[0m")
        else:
            print("\033[91mFAILURE: Password not found in wordlist.\033[0m")
            print(f"\033[90mTotal attempts: {tested:,}\033[0m")

    except KeyboardInterrupt:
        print("\n\033[91m[!] Session aborted by user.\033[0m")
    
    print("\033[94m" + "—" * get_terminal_width() + "\033[0m")

if __name__ == "__main__":
    main()