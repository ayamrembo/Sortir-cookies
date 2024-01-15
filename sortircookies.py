# Buka file.txt dan baca setiap baris
with open('file.txt', 'r') as file:
    lines = file.readlines()

# Ekstrak cookies dari setiap baris dan cetak dengan nomor urut
for idx, line in enumerate(lines):
    cookies = line.split('|')[2].strip()
    print(f"[{idx + 1}] {cookies}\n")