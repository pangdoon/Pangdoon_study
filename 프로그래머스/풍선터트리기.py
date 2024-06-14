def solution(a):
    def input_min(k):
        q = []
        t = k[0]
        for x in k:
            if t > x:
                t = x
            q.append(t)
        return q
    k = set(input_min(a) + input_min(list(reversed(a))))
    return len(k)

solution([9,-1,-5])