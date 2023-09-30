import os
import hashlib

def get_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_directory(directory):
    """Scan a directory and its subdirectories for potential viruses."""
    virus_signatures = {
        # Add MD5 hashes of known virus files here.
        # Example: "e99a18c428cb38d5f260853678922e03": "Virus name"
    }

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)

            if file_hash in virus_signatures:
                print(f"Virus detected: {virus_signatures[file_hash]} - {file_path}")

if __name__ == "__main__":
    directory_to_scan = input("Enter the directory path to scan: ")
    scan_directory(directory_to_scan)
