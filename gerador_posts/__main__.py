from tratar_dados import TratarDados
from configuracao import Configuracao

if __name__ == "__main__":
    dados = TratarDados()
    dicionario = dados.converteCsvEmDicionario()
    atualiza_yaml = dados.insereDicionarioNoYaml(dicionario)

    configuracao = Configuracao()
    dados = configuracao.lerYaml()
    ambiente = configuracao.configurarAmbiente()
    renderizacao = configuracao.renderizarTemplate(dados, ambiente)
