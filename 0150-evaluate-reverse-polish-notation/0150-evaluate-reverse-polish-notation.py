class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        s=["+", "-", "*", "/"]

        for i in tokens:
            if i in s:
                b = int(st.pop())
                a = int(st.pop())
                if i == "+":
                    k = a + b
                elif i == "-":
                    k = a - b
                elif i == "/":
                    k = int(a / b)
                elif i == "*":
                    k = a * b
                st.append(str(k))
            else:
                st.append(i)
        return int(st[-1])