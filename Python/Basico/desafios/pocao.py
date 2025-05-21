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

# Se o personagem ainda está vivo, decremente ao usar poção veneno
    # Pode usar poção veneno
    # Pode usar poção saude
   
# Se a saude for <= 0  
    # personagem vivo=False
    # informe personagem está morto, foi de "arrasta"
    # cancele a possibilidade de incrementar ou decrementar saude