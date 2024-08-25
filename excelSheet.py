class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        columnNumber = 0
        charToValue = {chr(i + 65): i + 1 for i in range(26)}

        length = len(columnTitle)
        for index in range(length):
            currentChar = columnTitle[length - 1 - index]
            columnNumber += charToValue[currentChar] * (26**index)
        
        return columnNumber
