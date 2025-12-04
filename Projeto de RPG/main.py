import random
import json

#Criação do personagem
class Personagem:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.level = 1
        self.exp = 0
        self.exp_max = 100
        self.inventario = ["Poção", "Poção", "Poção"]
        self.exp_recebido = 0

    def to_dict(self):
        return {
            "nome": self.nome,
            "hp": self.hp,
            "hp_max": self.hp_max,
            "ataque máximo": self.ataque,
            "level": self.level,
            "exp": self.exp,
            "exp_maximo": self.exp_max,
            "inventario": self.inventario
        }
    
    
    
    #verificação se está vivo
    def esta_vivo(self):
        return self.hp > 0
    #mostrar seus status
    def mostrar_status(self):
        print(f"Nome: {self.nome} | Vida: {self.hp}/{self.hp_max}  | Atk máx: {self.ataque} | Level: {self.level} | Exp atual: {self.exp}")
        
    def curar(self):
        if "Poção" in self.inventario:
            self.inventario.remove("Poção")
            self.hp += 20
            print(f"Você usou a poção. Vida atual: {self.hp}/{self.hp_max}")
            if self.hp > self.hp_max:
                self.hp = self.hp_max
        else:
            print("Não há poções no inventário")
        
        

    #função de ataque
    def atacar(self, alvo):
        dano_minimo = int(self.ataque / 2)
        dano_maximo = self.ataque
        dano = random.randint(dano_minimo, dano_maximo)
        alvo.hp -= dano
        if alvo.hp < 0:
            alvo.hp = 0
        print(f"{self.nome} atacou {alvo.nome} e tirou {dano} de HP")
        if dano == dano_maximo:
            print("Acerto Crítico")

#sistema de ganho de xp
    def ganhar_xp(self, exp_recebido):   
        self.exp += exp_recebido
        print(f"Você ganhou {exp_recebido} de XP! (Total: {self.exp}/{self.exp_max})")
        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            self.hp_max += 20
            self.ataque += 5
            self.hp = self.hp_max
            print(f"""
            ================================
            UPGRADE! VOCÊ SUBIU PARA O LEVEL {self.level}
            ================================
            Novos status:
            Vida Máxima: {self.hp_max}
            Ataque Máximo: {self.ataque}
            XP Atual: {self.exp}/{self.exp_max}
            ================================
            """)


def gerar_inimigos(numero_inimigos):
    lista_inimigos = ["Orc", "Goblin", "Dragão", "Golem", "Mutante"]
    lista_todos_inimigos = []
    for x in range (numero_inimigos):
        nome_sorteado = random.choice(lista_inimigos)
        hp_sorteado = random.randint(100, 200)
        ataque_sorteado = random.randint(5, 25)
        novo_inimigo = Personagem(nome_sorteado, hp_sorteado, ataque_sorteado)
        lista_todos_inimigos.append(novo_inimigo)
    return lista_todos_inimigos

        

heroi = Personagem("Gustavo", 125, 25)
inimigos = gerar_inimigos(5)


print("----- ÍNICIO DA BATALHA -----")
heroi.mostrar_status()
print("-" *50)

#loop do combate

for inimigo in inimigos:
    
    if not heroi.esta_vivo():
        break
    
    print(f"\n Um {inimigo.nome} selvagem apareceu! (HP: {inimigo.hp})")

    while heroi.esta_vivo() and inimigo.esta_vivo():
        print(f"\nTurno de {heroi.nome}")

        try:
            ação = int(input("----> Atacar inimigo (1) | curar (2)? <---- "))
        except ValueError:
            print("Isso não é um número")
        
        if ação == 1:
            heroi.atacar(inimigo)
        elif ação == 2:
            heroi.curar()
        else:
            print("Digito inválido, escolha 1 ou 2.")
            continue
        

        if not inimigo.esta_vivo():
            print(f"\nVocê venceu a luta, você derrotou {inimigo.nome}")
            xp_ganho = 130
            heroi.ganhar_xp(xp_ganho)
            print(f"Status final: {heroi.nome} [Vida:{heroi.hp}] vs {inimigo.nome} [Vida:{inimigo.hp}]")
            break
        print("\nTurno do inimigo...")
        inimigo.atacar(heroi)
        if not heroi.esta_vivo():
            print(f"\nVocê perdeu a luta, {inimigo.nome} derrotou você")
            print(f"Status final: {heroi.nome} [Vida:{heroi.hp}] vs {inimigo.nome} [Vida:{inimigo.hp}]")
            break   
        print(f"Status: {heroi.nome} [Vida:{heroi.hp}] vs {inimigo.nome} [Vida:{inimigo.hp}]")
if heroi.esta_vivo():
    print("PARÁBENS! Você derrotou todos da masmorra e saiu vivo!")

else:
    print("\nFim de jogo. Você foi derrotado em batalha.")
    
        