class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def solve(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                solve(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                solve(openN, closedN+1)
                stack.pop()
        solve(0,0)
        return res