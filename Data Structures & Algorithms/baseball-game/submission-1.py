class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for operation in operations:
            if operation == 'C':
                ans.pop()
            elif operation == 'D':
                ans.append(2 * ans[len(ans) - 1])
            elif operation == '+':
                ans.append(ans[len(ans) - 1] + ans[len(ans) - 2])
            else:
                ans.append(int(operation))
        return sum(ans)