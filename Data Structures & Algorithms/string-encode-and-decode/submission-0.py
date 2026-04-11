class Solution:

    def encode(self, strs: List[str]) -> str:
        string = " ".join(word for word in strs)
        return string

    def decode(self, s: str) -> List[str]:
        l = s.split()
        return l
