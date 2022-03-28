# DECIMAL TO BINER CONVERTER
class DecimalToBinary:
    def __init__(self, decimal):
        self.decimal = decimal
        self.binary = ""
        self.convert()

    def convert(self):
        while self.decimal > 0:
            self.binary = str(self.decimal % 2) + self.binary
            self.decimal = int(self.decimal / 2)
        return self.binary

# DECIMAL TO HEX CONVERTER
class DecimalToHex:
    def __init__(self, decimal):
        self.decimal = decimal
        self.hex = ""
        self.convert()

    def convert(self):
        while self.decimal > 0:
            self.hex = str(hex(self.decimal % 16))[2] + self.hex
            self.decimal = int(self.decimal / 16)
        return self.hex

# DECIMAL TO OCTAL CONVERTER
class DecimalToOctal:
    def __init__(self, decimal):
        self.decimal = decimal
        self.octal = ""
        self.convert()

    def convert(self):
        while self.decimal > 0:
            self.octal = str(self.decimal % 8) + self.octal
            self.decimal = int(self.decimal / 8)
        return self.octal

class DecimalConverter:
    def __init__(self, decimal):
        self.decimal = decimal
        self.convert()

    def convert(self):
        self.binary = DecimalToBinary(self.decimal)
        self.hex = DecimalToHex(self.decimal)
        self.octal = DecimalToOctal(self.decimal)
        return self.binary, self.hex, self.octal

decimal = 20
DecimalConverter(decimal).convert()
print(f'{decimal} in binary is {DecimalToBinary(decimal).convert()}')
print(f'{decimal} in hex is {DecimalToHex(decimal).convert()}')
print(f'{decimal} in octal is {DecimalToOctal(decimal).convert()}')



