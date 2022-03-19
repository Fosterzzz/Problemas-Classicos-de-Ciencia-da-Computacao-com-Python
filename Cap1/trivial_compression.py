class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.compress(gene)


    def compress(self, gene:str) -> None:
        self.bit_string: int = 1 # começa com uma sentinela
        for nucloide in gene.upper():
            self.bit_string <<= 2 #Desloca dois bits para a esquerda
            if nucloide == "A": #Muda os dois ultimos bits para 00
                self.bit_string |= 0b00
            elif nucloide == "C": #Muda os dois ultimos bits para 01
                self.bit_string |= 0b01
            elif nucloide == "G": #Muda os dois ultimos bits para 10
                self.bit_string |= 0b10
            elif nucloide == "T": #Muda os dois ultimmos bits para 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleoid:{}".format(nucloide))


    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string - 1, 2): #-1 para excluir a sentinela
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00: #A
                gene += "A"
            elif bits == 0b01: #C
                gene += "C"
            elif bits == 0b10: #G
                gene += "G"
            elif bits == 0b11: #T
                gene += "T"
            else:
                raise ValueErro("Invalid Nucleoid:{}".format(nucloide))
        return gene[::1] #[::-1] Inverte a string usando fatiamento de inversão


    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str="TAGGATTGACCGATCATGCATTCGATCGACCTACGCACTACGACTCACGCATAGACTACCTAGCTACGCTACA" * 100
    print(f'O valor original de bytes é {getsizeof(original)}')
    compressed: CompressedGene = CompressedGene(original) # compacta
    print(f'O valor comprimido de bytes é {getsizeof(compressed.bit_string)}')
    print(compressed) #Descompacta
    prit(f'O original e o descompactado são o mesmo: {original == compressed.decompress()}')


