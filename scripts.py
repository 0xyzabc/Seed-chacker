from itertools import permutations
from mnemonic import Mnemonic

# Baca kata-kata dari file
with open("seed-words.txt", "r") as f:
    words = [line.strip() for line in f.readlines() if line.strip()]

if len(words) != 12:
    raise ValueError("File harus berisi tepat 12 kata.")

mnemo = Mnemonic("english")
checked = 0
found = 0

for perm in permutations(words):
    phrase = " ".join(perm)
    if mnemo.check(phrase):
        found += 1
        print(f"\n✅ Valid Seed Found: {phrase}")
    checked += 1
    if checked % 100000 == 0:
        print(f"Checked: {checked:,} permutations...")

#for perm in permutations(known_words[1:]):  # lock word[0] = "ripple"
#    phrase = "ripple " + " ".join(perm)


print(f"\nDone. Checked {checked:,} permutations. Found {found} valid seeds.")
