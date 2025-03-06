# Trie BFS approach --
# TC - O(n*l) + O(n*l) = O2(n * l) = O(n * l) --> 1st n*l is for insert and second n * l is wor BFS
# SC - O(n * l)

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # initialize the root for curr
        curr = self.root

        for i in range(len(word)):
            currChar = word[i]
            # if node not present
            if curr.children[ord(currChar) - ord('a')] == None:
                curr.children[ord(currChar) - ord('a')] = TrieNode()
            # else
            curr = curr.children[ord(currChar) - ord('a')]
        # here we dont use isEnd. Instead we form the word. If the string is empty, it means its not the end
        # if its the end, then string will have a value
        curr.word = word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        if words is None or len(words) == 0: return ""

        # initialize trie
        trie = Trie()

        for word in words:
            trie.insert(word)

        # BFS based solution
        # initialize a queue containing Trie Nodes wotj Trie's root
        q = deque([trie.root])

        maxWord = None

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                maxWord = curr.word

                # we start from 25 since we need to return longest word with LOWEST lexicographical order
                # so we iterate in reverse
                for j in range(25, -1, -1):
                    if curr.children[j] is not None and curr.children[j].word is not None:
                        q.append(curr.children[j])
        if curr.word is None: return ""
        return maxWord