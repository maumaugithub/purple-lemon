from difflib import SequenceMatcher
from thefuzz import fuzz
import levenshtein

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

res = similar("Apple", "Appel")
print(res)

Str1 = "Apple"
Str2 = "Appel"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
print(Ratio)

dist = lev.distance(Str1.lower(),Str2.lower())
print(dist)