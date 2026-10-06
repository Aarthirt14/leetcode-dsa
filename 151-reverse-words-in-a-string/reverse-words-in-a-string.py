class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        word=[]
        for i in range(len(words)-1,-1,-1):
            word.append(words[i])
        return " ".join(word)
        