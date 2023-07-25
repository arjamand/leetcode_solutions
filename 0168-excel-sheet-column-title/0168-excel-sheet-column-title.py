class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        column_title = ""

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            column_title = letters[remainder] + column_title
            columnNumber //= 26

        return column_title