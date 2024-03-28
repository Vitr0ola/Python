#tipo de dado = dicionário

#API = é um conjunto de programas responsável por fazer a comunição entre elementos
#request = mostrar oque foi solicitado
#protocolo = http/  https quando o acesso é protegido, tem uma segurança maior
#API REST = internet
#JSON = modelo de arquivo
#serve para transportar informaçoes para um cliente de um lado para o outro

# viacep.com.br  = site para


#DICIONARIO =
#Sao coleçoes desordenadas de itens.
#Equanto outras coleçoes, como listas e tuplas, sao indexadas por uma faixa de numeros, os dicionarios sao indexados por CHAVES, que podem ser de qualquer tipo imultavel (Vai para memoria e nao sai)
#Cada par chave-valor em um dicionario é separado por virgulas e TODO CONJUNTO É COLOCADO ENTRE CHAVES {}

meu_dict = {'nome':'Alice','idade': 25}

#------------ chave----------chave------

#CRIANDO DICIONARIOS;

#A criaçao de um dicionario é simples, voce pode iniciar um dicionario vazio ou com alguns pares chave-valor Exemplo:

#DICIONARIO VAZIO;

dict_vazio = {}

#DICIONARIO COM DADOS INICIAIS;

dict_preenchido = {'nome': 'Carlos','idade':30}

#ACESSANDO ELEMENTOS EM UM DICIONARIO;

nome = dict_preenchido['nome'] #usa os conchetes para montras o valor dentro do dicionario e depois apenas dar o print para exibir o valor.
#print(nome) #saída : Carlos

#MÉTODO .get;

profissao = dict_preenchido.get('profissao','Nao especificado')


#ADICIONANDO E MODIFICANDO ELEMENTOS;

dict_preenchido {'profissao'} = 'engenheiro'

#REMOVER ELEMENTOS;

#utlizamos o comando POP
idade = dict_preenchido.pop('Idade')

del dict_preenchido


#METODOS UTEIS

#OBETENDO TODAS AS CHAVES;

chaves = (meu_dict.keys())

#OBETENDO TODOS OS VALUES;
values = (meu_dict.values())
