from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 24 

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funconario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funconario_teste.calcular_bonus() # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then

    #TESTE ADICIONADO
    def test_quando_calcular_bonus_recebe_10000_deve_retornar_1000(self):
        entrada_salario = 10000  # Given
        esperado = 1000

        funcionario_teste = Funcionario('Vinicius Dias Valenca', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # Then

    #TESTE ADICIONADO
    def test_str(self):
        
        nome = "João Silva"
        data_nascimento = "15/08/1980"
        salario = 50000.00

        funcionario = Funcionario(nome, data_nascimento, salario)
        
        expected_str = f'Funcionario({nome}, {data_nascimento}, {salario})'
        
        assert str(funcionario) == expected_str

    #TESTE ADICIONADO
    def test_quando_calcular_bonus_excecao_mensagem_correta(self):
        salario = 10000000  # Valor que gerará exceção
        esperado_mensagem = 'O salário é muito alto para receber um bônus'

        funcionario_teste = Funcionario('Teste', '11/11/2000', salario)

        with pytest.raises(Exception) as excinfo:
            funcionario_teste.calcular_bonus()
        
        assert str(excinfo.value) == esperado_mensagem

    #TESTE ADICIONADO
    def test_quando_sobrenome_recebe_Vinicius_Dias_Valenca_deve_retornar_Valenca(self):
        entrada = 'Vinicius Dias Valenca'  # Given
        esperado = 'Valenca'

        vinicius = Funcionario(entrada, '05/12/2002', 1234)
        resultado = vinicius.sobrenome()  # When

        assert resultado == esperado  # Then

    #TESTE ADICIONADO
    def test_quando_calcular_bonus_recebe_10001_deve_retornar_exception(self):
        entrada_salario = 10001  # Given

        funcionario_teste = Funcionario('Vinicius Dias Valenca', '05/12/2002', entrada_salario)

        with pytest.raises(Exception):  # Then
            funcionario_teste.calcular_bonus()  # When

    #TESTE ADICIONADO
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funconario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funconario_teste.decrescimo_salario() # when
        resultado = funconario_teste.salario

        assert resultado == esperado  # then

    #TESTE ADICIONADO
    def test_quando_eh_socio_recebe_Vinicius_Dias_com_salario_100000_deve_retornar_False(self):
        entrada_nome = 'Vinicius Dias'
        entrada_salario = 100000  # Given
        esperado = False

        vinicius_dias = Funcionario(entrada_nome, '05/12/2002', entrada_salario)
        resultado = vinicius_dias._eh_socio()  # When

        assert resultado == esperado  # Then














