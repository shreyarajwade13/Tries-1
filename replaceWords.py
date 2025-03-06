# TC: O(n * L) n is no. of words and L is max length of one word
# SC: O(n * L) max space occupied by the Trie; there is also space occupied by new sentence which is again
#                     O(n * L) and so total space complexity would be O(n * L)

class TrieNode:
    def __init__(self):
        # 26 since only lowercase alphabets - constraint
        self.children = [None for i in range(26)]
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # TC - O(nl) - where n is the number of words and l is avg length of each word
    def insert(self, word: str) -> None:
        # initialize the root as curr node
        curr = self.root

        for i in range(len(word)):
            currChar = word[i]
            # check if char present in trie
            if curr.children[ord(currChar) - ord('a')] == None:
                curr.children[ord(currChar) - ord('a')] = TrieNode()
            # if present, add the rest of the chars to form the word
            curr = curr.children[ord(currChar) - ord('a')]
        # mark the end of the word as True
        curr.word = word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if dictionary is None or len(dictionary) == 0: return sentence

        #   initialize a Trie
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        newWords = []

        # traverse through each char of the word to see if its prefix present in trie
        # TC - O(ml) - m words of avg length l for split
        for word in sentence.split():
            curr = trie.root
            # we travel over entire word worst case to find the prefix - TC - O(mk)
            for i in range(len(word)):
                currChar = word[i]
                # check if the char of the word present in trie
                if curr.children[ord(currChar) - ord('a')] == None or curr.word != None:
                    # let the word in the sentence be as it is
                    break
                # else check rest of the chars if present
                curr = curr.children[ord(currChar) - ord('a')]

            # form this prefix word -  take the new word to be the subword till we traversed
            prefix = curr.word

            # if prefix if found, we should've reach the last char marked as true
            if (prefix == None):  # if new word not a word, then append old word itself
                newWords.append(word)
            else:  # else append new word
                newWords.append(prefix)

        return ' '.join(newWords)



