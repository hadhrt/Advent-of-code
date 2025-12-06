from collections import deque

def p1(lines):
    match = {'(':')','[':']','{':'}','<':'>'}
    score = {')':3,']':57,'}':1197,'>':25137}
    ill_chars = []
    for line in lines:
        stack = deque([])
        for c in line:
            if c in match: stack.append(c)
            else: 
                if c != match.get(stack.pop()): ill_chars.append(c)

        
    return sum(map(lambda x: score.get(x),ill_chars))


def p2(lines):
    match_b = {'(':')','[':']','{':'}','<':'>'}
    score_b = {')':1,']':2,'}':3,'>':4}
    scores = []

    for line in lines:
        stack = deque([])
        #get open brackets
        for c in line:
            if c in match_b: stack.append(c)
            else:
                if c != match_b.get(stack.pop()): 
                    stack.clear()
                    break
        #match brackets and reverse, then score
        score = 0
        for b in map(lambda x: match_b.get(x),reversed(stack)):
            score *= 5
            score += score_b.get(b)
        scores.append(score)
    scores = [score for score in scores if score !=0]
    return sorted(scores)[len(scores)//2]
    #return scores


f = open("input10.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)))
print ("Part 2: " + str(p2(lines)))