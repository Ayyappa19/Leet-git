class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression += '-'
        s = expression[0]
        n1 , d1 = 0 , 1

        for i in range(1,len(expression)):
            if expression[i] == '+' or expression[i] == '-':
                n2 , d2 = map(int,s.split('/'))
                lcm = math.lcm(d1,d2)

                n1 *= (lcm//d1)
                n2 *= (lcm//d2)
                n1 += n2
                d1 = lcm
                gcd = math.gcd(abs(n1),abs(d1))
                n1 //= gcd
                d1 //= gcd
                s = expression[i]
            else:
                s += expression[i]
                
        return f"{n1}/{d1}"        