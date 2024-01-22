import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    return max(text.split())

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

############################################################
# Problem 3c

def mutateSentences(sentence):
    words = sentence.split()
    pairs = {(words[i], words[i + 1]) for i in range(len(words) - 1)}

    def generate_sentences(start_word, current_sentence):
        if len(current_sentence) == len(words):
            return [current_sentence]
        sentences = []
        for pair in pairs:
            if pair[0] == start_word:
                sentences.extend(generate_sentences(pair[1], current_sentence + ' ' + pair[1]))
        return sentences

    generated_sentences = set()
    for word in set(words):
        for sentence in generate_sentences(word, word):
            generated_sentences.add(sentence)

    return list(generated_sentences)


############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    return sum(v1[key] * v2.get(key, 0) for key in v1)

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    for key, value in v2.items():
        v1[key] += value * scale

############################################################
# Problem 3f

def findSingletonWords(text):
    word_count = collections.defaultdict(int)
    for word in text.split():
        word_count[word] += 1
    return {word for word, count in word_count.items() if count == 1}

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    n = len(text)
    if n == 0:
        return 0

    # dp[i][j]는 text[i]부터 text[j]까지의 부분 문자열이 팰린드롬일 때의 길이를 저장합니다.
    dp = [[0] * n for _ in range(n)]

    # 모든 단일 문자는 팰린드롬입니다.
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if text[i] == text[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
