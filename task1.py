
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for i in "!?',;.":
        sentence = sentence.replace(i, ' ')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)

print(solution(sentence1))
print(solution(sentence2))