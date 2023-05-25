import tratardados

if __name__ == "__main__":
    dados = tratardados()
    dicionario = dados.converteCsvEmDicionario()
    atualiza_yaml = dados.insereDicionarioNoYaml(dicionario)
