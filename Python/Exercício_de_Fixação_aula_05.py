# Criaçao OOP Python;

#Utilizaçao do comando class para criar uma instancia da classe

# def modulo(self) criaçao de uma funçao neste caso metodos selfVarA / utiliza a variavel 'recebida' pela classe (objeto)

#class_nome_classe:
  #def__init__(self,variavelA,varialvelB): #construtor = CRIAR, INSTANCIAR COM O INIT
  #selfVarA = variavelA
  #selfVarB = variavelB


#CRIANDO UMA CLASSE TV:

#PRIMEIRO TEMOS QUE CRIAR A CLASSE (Class)
#DEPOIS COLOCAMOS ATRIBUTOS (COR, MODELO, TAMANHO...)


class TV:
  def __init__(self, t=55,marca= 'Samsumg'): # iniciar a construçao
    self.marca = marca
    self.modelo = '4G' #caracteristicas
    self.cor = 'Preto' #caracteristicas
    self.tamanho = t
    self.canal = 'Netflix'


  def muda_canal(self,novo_canal = ''):
    if novo_canal == '':
      pass
    else:
      self.canal = novo_canal


tv_sala = TV() #criou o objeto
tv_quarto = TV() #criou o objeto
tv_cozinha = TV(40,'LG')
tv_sala.muda_canal()

print(tv_sala.canal)
print(tv_sala.tamanho)
print(tv_quarto.marca)
print(tv_cozinha.marca)



 #criando um novo objeto
Tv_quarto2 = TV() #objeto
print(Tv_quarto2.canal)
