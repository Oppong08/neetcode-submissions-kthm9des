class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)   #{wildcard pattern : [wors]}
        wordList.append(beginWord)

        #adds words to their *wild card combinations in nei
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i:]
                nei[pattern].append(word)
        
        q = deque(beginWord)
        visit = set()  #keeps track of visited words
        visit.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:i] + "*" + word[i:]
                    #adds only valid words in patterns to the queue
                    for neiword in nei[pattern]:
                        if neiword not in visited:
                            visit.add(neiword)
                            q.append(neiword)
                res += 1

        return res































        # if endWord not in wordList:
        #     return 0

        # nei = collections.defaultdict(list)
        # wordList.append(beginWord)
        # for word in wordList:
        #     for j in range(len(word)):
        #         pattern = word[:j] + "*" + word[j + 1:]
        #         nei[pattern].append(word)

        # visit = set([beginWord])
        # q = deque([beginWord])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         word = q.popleft()
        #         if word == endWord:
        #             return res
        #         for j in range(len(word)):
        #             pattern = word[:j] + "*" + word[j + 1:]
        #             for neiWord in nei[pattern]:
        #                 if neiWord not in visit:
        #                     visit.add(neiWord)
        #                     q.append(neiWord)
        #     res+=1

        # return 0