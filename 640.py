class Solution(object):
    def count(self, expression):
        n_of_x = 0
        const_val = 0
        positive = 1
        zero_char_val = ord('0')
        current_val = 0
        preceeding_zero = False
        for n in expression:
            if n == '-':
                const_val += current_val
                current_val = 0
                positive = -1
            elif n == '+':
                const_val += current_val
                current_val = 0
                positive = 1
            elif n == 'x':
                # print 'in x, c_v=' + str(current_val)
                if current_val == 0:
                    current_val = positive
                if preceeding_zero:
                    current_val = 0
                    preceeding_zero = False
                n_of_x += current_val
                current_val = 0
            else:
                # print "current n=" + str(n) + " c_v=" + str(const_val)
                current_val = current_val * 10 + (ord(n) - zero_char_val) * positive
                if current_val == 0:
                    preceeding_zero = True
                print current_val 
        if current_val != 0:
            const_val += current_val
        return [n_of_x, const_val]

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equ_list = equation.split('=')
        # print equ_list[0]
        # print equ_list[1]
        n_of_x = 0
        const_val = 0
        ret = self.count(equ_list[0])
        n_of_x += ret[0]
        const_val -= ret[1]

        print "nof_x="+str(n_of_x) + " c_v="+str(const_val)
        ret = self.count(equ_list[1])
        n_of_x -= ret[0]
        const_val += ret[1]
        print ret
        if n_of_x == 0 and const_val == 0:
            return "Infinite solutions"
        elif n_of_x == 0 and const_val != 0:
            return "No solution"
        else:
            return "x=" + str(const_val/n_of_x)
        

        # print "n of x=" + str(n_of_x) + " const_val=" + str(const_val)


sol = Solution()
# print sol.solveEquation("x+5-3+x=6+x-2")
# print sol.solveEquation("x=x")
# print sol.solveEquation("2x=x")
# print sol.solveEquation("2x+3x-6x=x+2")
# print sol.solveEquation("x=x+2")
# print sol.solveEquation("-x=-1")
print sol.solveEquation("x+5-3+18x+32-128=6+x-2-1085+4x")