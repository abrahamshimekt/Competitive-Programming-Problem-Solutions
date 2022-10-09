class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new_order = list(order)
        s = list(s)
        i = 0
        while i < len(new_order):
            if new_order[i] not in s:
                new_order.pop(i)
            else:
                i += 1
        for c in new_order:
            if c in s:
                s.remove(c)
        for c in s:
            if c in new_order:
                new_order.insert(new_order.index(c),c)
            else:
                new_order.append(c)

        return "".join(new_order)
        
        