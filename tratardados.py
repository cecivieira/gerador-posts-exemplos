import csv
import yaml

class TratarDados:
    def __init__(self):
        self.csv_path = 'dados/links.csv'
        self.yaml_path = 'dados/variaveis.yaml'
    
    def converteCsvEmDicionario(self):
        with open(self.csv_path, 'r') as arquivo:
            csv2dicionario = [item for item in csv.DictReader(arquivo)]
        return csv2dicionario

    def insereDicionarioNoYaml(self, lista_dicionarios):
        with open(self.yaml_path, 'r') as arquivo:
          yaml_arquivo = yaml.safe_load(arquivo)
          yaml_arquivo['links'] = lista_dicionarios
        if yaml_arquivo:
          with open(self.yaml_path, 'w') as arquivo:
            yaml.safe_dump(yaml_arquivo, arquivo)


if __name__ == "__main__":
    dados = TratarDados()
    dicionario = dados.converteCsvEmDicionario()
    atualiza_yaml = dados.insereDicionarioNoYaml(dicionario)