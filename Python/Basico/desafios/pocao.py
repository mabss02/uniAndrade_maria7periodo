class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 100
        self.vivo = True
       
    def usar_pocaoVerde(self, pocao):
        self.saude += pocao.potencia
        print(f"Personagem {self.nome} usou poção de {pocao.tipo}")
        print(f"Cura: {pocao.potencia} | Saúde: {self.saude}")
       
    def usar_pocaoRoxa(self, pocao):
        self.saude -= pocao.potencia
        print(f"Personagem {self.nome} usou poção de {pocao.tipo}")
        print(f"Dano: {pocao.potencia} | Saúde: {self.saude}")    
       
class PocaoVerde:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
       
class PocaoRoxa:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
       
# Instancia Jogador
p1 = Personagem("Chiquinha")

pocaoVerde = PocaoVerde("Cura", 15)
pocaoRoxa = PocaoRoxa("Dano", 15)

p1.usar_pocaoVerde(pocaoVerde)

p1.usar_pocaoRoxa(pocaoRoxa)

#del p1
print(pocao1)

class Player
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.vivo = True

    def usar_pocao(self, pocao):
        if not self.vivo:
            print("Game Over!")
            return
        
        efeito_pocao = pocao.usar() # Número + ou -
        nova_energia = efeito_pocao + self.energia

        # Tratar casos (0 e 100+)
        if nova_energia <=0;
            nova_energia = 0
            self.vivo = False

        if nova_energia >= 100;
            nova_energia = 100
            print("Impossivel usar cura!")

        self.energia = nova_energia
        self.status()

class Item:
    def __init__(self, efeito):
        self.tipo = tipo
        self.efeito = efeito

class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item (self, item: Item):
        if not item:
            print("Escolha um item para adicionar ao inventario")