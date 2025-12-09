sentence = input("Enter a Sentence: ")
words = sentence.lower().split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
    # count[word] += 1

for i in count:
    print(f"{i} : {count[i]}")