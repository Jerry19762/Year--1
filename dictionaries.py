filename= "textfile.txt"
word_freq = {}

with open(filename, "r") as file:
    for line in file:
        words = line.lower().split()
        for word in words:
            word = word.strip(".,?!:()")
            word_freq[word]= word_freq.get(word,0) + 1
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True )[:5]
for word, freq in sorted_words:
    print(f"{word}:{freq}")

