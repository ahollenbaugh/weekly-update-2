f = open('ingest_this.txt', 'r')
content = f.read()
f.close()

vowels = 'aeiouy'

for vowel in vowels:
    content = content.replace(vowel, "9").replace(vowel.upper(), "9")

print(content)