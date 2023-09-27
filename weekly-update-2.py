f = open('ingest_this.txt', 'r')
content = f.read()
f.close()

vowels = 'aeiouy'
replace_with = "7"

for vowel in vowels:
    content = content.replace(vowel, replace_with).replace(vowel.upper(), replace_with)

print(content)