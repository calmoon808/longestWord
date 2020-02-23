S = "abppplee"
D = {
    "able", "ale", "apple", "bale", "kangaroo"
}

#initial solution
def longestWord(str, words):
    longest = ""
    for word in words:
        j = 0
        for i in range(len(str)):
            if j == len(word):
                if len(word) > len(longest):
                    longest = word
                break
            if word[j] == str[i]:
                j += 1
    print(longest)
    
longestWord(S, D);