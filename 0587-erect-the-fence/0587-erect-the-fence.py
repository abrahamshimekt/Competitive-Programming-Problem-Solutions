class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = sorted(trees)                             
        U, L = [], []
        
        def cross(B, A, T):
            Bx, By, Ax, Ay, Tx, Ty = chain(B, A, T)              
            return (Ty-By)*(Bx-Ax) - (By-Ay)*(Tx-Bx)
                
        for T in trees:                                        
            while len(U) >= 2 and cross(U[-1],U[-2],T) < 0:    
                U.pop()                                         
            U.append(T)
            while len(L) >= 2 and cross(L[-1],L[-2],T) > 0:      
                L.pop()                                       
            L.append(T)                                       
        return set(tuple(T) for T in (U+L))  