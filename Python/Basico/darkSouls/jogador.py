class Jogador:
    self.nome = nome
    self.dano = dano
    self.__saude = 100 #encapsulamento

    def get_saude(self):
        return self.__saude
    
    def set_saude(self, valor):
        self.saude += valor

    def atacar(self):
        print(f"{self.nome} atacou!")

    def defender(self):
        print(f"{self.nome} defendeu!")

if __name__ == '__main__':
    p1 = jogador("Jow", 50)
    p1.atacar()