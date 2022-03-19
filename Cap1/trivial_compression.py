class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.compress(gene)


def compress(self, gene:str) -> None:
    self.bit_string: int = 1 # começa com uma sentinela
    for nucloide in gene.upper():
        self.bit_string <<= 2 #Desloca dois bits para a esquerda
        if nucloide == "A":
            self.bit_string |= 0b00
        elif nucloide == "C":
            self.bit_string |= 0b01
        elif nucloide == "G":
            self.bit_string |= 0b10
        elif nucloide == "T":
            self.bit_string |= 0b11
        else:
            raise ValueError("Invalid Nucleoid:{}".format(nucloide))