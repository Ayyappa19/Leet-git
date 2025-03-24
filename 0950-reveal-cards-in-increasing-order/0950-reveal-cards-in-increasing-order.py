class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        k = deque([deck.pop()])
        while deck:
            k.appendleft(k.pop())
            k.appendleft(deck.pop())
        return list(k)