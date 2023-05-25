from tratardados import TratarDados

if __name__ == "__main__":
    dados = TratarDados()
    dicionario = dados.converteCsvEmDicionario()
    atualiza_yaml = dados.insereDicionarioNoYaml(dicionario)
