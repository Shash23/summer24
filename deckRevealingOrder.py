from typing import List
from collections import deque

def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    
    # use the roman skipping problem
    
    n = len(deck)
    
    idx_deck = [0] * n
    
    queue = deque(range(n))
    
    deck.sort()
    
    for i in deck:        
        
        back = queue.popleft()
        idx_deck[back] = i
        if queue:
            queue.append(queue.popleft())
        
    return idx_deck
        
        
deck = [17,13,11,2,3,5,7]
print(deckRevealedIncreasing(deck))
    
    
    