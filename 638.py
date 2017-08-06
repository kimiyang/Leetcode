class Solution(object):
    best_map = {}
    def DFS(self, price, special, needs):
        best = 0
        needs_str = ''
        best_with_offer = 0
        for i in range(0, len(needs)):
            best += price[i] * needs[i]
            needs_str += str(needs[i])
        if needs_str in self.best_map:
            return self.best_map[needs_str]
        for o in special:
            new_needs = []
            fit = True
            for i in range (0, len(needs)):
                rest = needs[i] - o[i]
                if rest < 0:
                    fit = False
                    break
                new_needs.append(rest)
            if fit:
                # print o
                # print new_needs
                # print o[len(needs)-1]
                best_with_offer = self.shoppingOffers(price, special, new_needs) + o[len(needs)]
                # print best_with_offer
                if best_with_offer < best:
                    best = best_with_offer
                    # print best
        self.best_map[needs_str] = best
        return best
        
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.best_map = {}
        return self.DFS(price, special, needs)
        
        
        