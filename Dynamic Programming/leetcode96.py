class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n + 1)
        self.table[0] = 1
        return self.numTreerec(n)

    def numTreerec(self, n):
        if self.table[n] != -1:
            return self.table[n]

        total = 0
        for m in range(n):
            total += self.numTreerec(m) * self.numTreerec(n - 1 - m)

        self.table[n] = total
        return total