class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs:
            return "||||||||||".join(strs)
        else:
            return "[]"

    def decode(self, s: str) -> List[str]:
        
        if s == "[]":
            return []
        else:
            return s.split("||||||||||")
