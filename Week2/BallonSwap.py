import sys
from functools import cache

# Nødvendigt i Python, hvis listen af gæster er meget lang
sys.setrecursionlimit(2000) 

def max_balloon_score_recursive(balloons):
    n = len(balloons)
    
    # @cache gemmer resultatet af opt(color, i), 
    # så vi aldrig beregner den samme tilstand to gange.
    @cache
    def opt(color, i):
        # Basistilfælde (i = 0)
        if i == 0:
            return 0 if color == 'red' else float('-inf')
            
        # Bemærk: 'balloons' er 0-indekseret, så gæst 'i' er på plads 'i-1'
        guest_color = balloons[i - 1] 
        
        # Scenarie A: Gæsten har en anden farve
        if color != guest_color:
            return opt(color, i - 1)
            
        # Scenarie B: Gæsten har den farve, vi kigger på
        # Find max ved at bytte fra en anden farve
        max_diff_swap = max(opt(c, i - 1) - 1 for c in ['red', 'blue', 'green'] if c != color)
        
        # Returner max af at bytte med samme farve (+1) eller en anden farve (-1)
        return max(opt(color, i - 1) + 1, max_diff_swap)

    # Vi vil have det maksimale for alle tre farver efter at have besøgt alle n gæster
    return max(opt('red', n), opt('blue', n), opt('green', n))

# Kørsel af eksemplet:
C = ["red", "green", "green", "red", "blue", "blue", "green"]
print(f"Maksimal mulig score: {max_balloon_score_recursive(C)}")