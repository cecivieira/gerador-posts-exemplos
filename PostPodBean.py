import csv

class PostPodBean():
    def __init__(self):
        self.links_recados = input('Caminho para csv com links mencionados nos RECADOS: ')
        self.links_entrevista = input('Caminho para csv com links mencionados no EPISÓDIO: ')

    def descricao(self):
        texto_descricao = input('Descrição do episódio:')
        return texto_descricao
    
    def lerCsvLinks(self, links):
        lista_links = []
        with open(links) as arquivo_csv:
            conteudo = csv.reader(arquivo_csv)
            for linha in conteudo:
                lista_links.append(linha)
        return lista_links
    
    

    def linksRecados(self):
        links = self.links_recados
        self.lerCsvLinks(links)
    
    def linksEntrevista(self):
        links = self.links_entrevista
        self.lerCsvLinks(links)

PostPodBean().linksEntrevista()