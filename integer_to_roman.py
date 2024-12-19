class RomanConverter:
    def __init__(self,number):
        if not isinstance(number,int):
            raise ValueError("Input must be an Integer")
        if number < 1 or number > 3999:
            raise ValueError("Number must be between 1 and 3999")
        self.number = number

    def to_roman(self):
        roman_numerals = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",
                          50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        
        result = ""
        num = self.number

        for value, numeral in roman_numerals.items():
            while num >= value:
                result += numeral
                num -= value

        return result
    
try:
    number = int(input("Enter an integer between 1 to 3999: "))
    converter = RomanConverter(number)
    roman_numeral = converter.to_roman()
    print(f"The roman numeral for {number} is {roman_numeral}")
except ValueError as e:
    print(f"Error: {e}")