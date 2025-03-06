# Trie approach --

# this class is created so at every char we can establish DS with required components
class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False


class Trie:

    def __init__(self):
        # establish DS
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # TC - O(n)
        # SC - O(n) - worst case since length of the word

        # initialize to root of the trie as curr node
        curr = self.root
        for i in range(len(word)):
            currChar = word[i]
            # check if char already present in trie, if not --
            if curr.children[ord(currChar) - ord('a')] == None:
                # add char to the trie
                curr.children[ord(currChar) - ord('a')] = TrieNode()
            # if present, continue to add remaining children till end of word
            curr = curr.children[ord(currChar) - ord('a')]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        # TC - O(n) - length of word
        # SC - O(1)

        # initialize to root of the trie as curr node
        curr = self.root
        for i in range(len(word)):
            currChar = word[i]
            if curr.children[ord(currChar) - ord('a')] == None:
                return False
            # if present check rest of the character of the word till end of string
            curr = curr.children[ord(currChar) - ord('a')]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        # TC - O(n) - length of prefix
        # SC - O(1)

        # initialize to root of the tries as curr node
        curr = self.root
        for i in range(len(prefix)):
            currChar = prefix[i]
            if curr.children[ord(currChar) - ord('a')] == None:
                return False
            curr = curr.children[ord(currChar) - ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)