class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not cur.children.get(char):
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endofword = True
        

    def search(self, word: str) -> bool:
        #why dfs
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                char = word[i]
                if char == '.': #recursively search for the next word after '.' in the children's values
                    for child in cur.children.values():
                        if dfs(1+i, child):
                            return True
                    return False
            
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.endofword

        return dfs(0, self.root)

