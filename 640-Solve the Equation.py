class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # define the patterns
        co_p = re.compile('-?\d*x')
        num_p = re.compile('-?\d*')
        
        # split the 2 parts of the equation.
        lhs = equation.split('=')[0]
        rhs = equation.split('=')[1]
        
        # find the list of coefficients with x(in both lhs and rhs)
        lhs_co = co_p.findall(lhs)
        rhs_co = co_p.findall(rhs)
        
        # find the list of all signed numbers after removing the coefficient
        # Notice that, I replace the coeffiecients with an '*' symbol to extract the remaining numbers. 
        # And I retrieve the numbers with the sign.
        lhs_num_list = num_p.findall(re.sub('-?\d*x', '*', lhs))
        rhs_num_list = num_p.findall(re.sub('-?\d*x', '*', rhs))
        
        # Now, simply add the numbers on the LHS and RHS
        lhs_sum = 0
        rhs_sum = 0

        for i in lhs_num_list:
            if i:
                lhs_sum += int(i)

        for i in rhs_num_list:
            if i:
                rhs_sum += int(i)
                
        # Add the Coefficients on both LHS and RHS.
        lhs_coeff_sum = 0
        rhs_coeff_sum = 0
        
        # While adding coefficients, 'x' and '-x' wil be replaced by 1 and -1 respectively.
        for i in lhs_co:
                i = i.replace('x', '')
                if not i:
                    i = 1
                elif i == '-':
                    i = -1
                lhs_coeff_sum += int(i)

        for i in rhs_co:
                i = i.replace('x', '')
                if not i:
                    i = 1
                elif i == '-':
                    i = -1
                rhs_coeff_sum += int(i)
                
        # Now, this is simple math and check the conditions to handle the edge cases.
        if lhs_sum == rhs_sum and lhs_coeff_sum == rhs_coeff_sum:
            return "Infinite solutions"
        
        if lhs_coeff_sum == rhs_coeff_sum:
            return "No solution"
        result = (rhs_sum - lhs_sum) / (lhs_coeff_sum - rhs_coeff_sum)
        return "x=" + str(result)
        
