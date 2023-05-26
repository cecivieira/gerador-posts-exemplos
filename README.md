# Gerador de posts - Exemplos
Esse repositório é destinado a armazenar exemplos do funcionamento do pacote [gerador-posts](https://pypi.org/project/gerador-posts/). Você também pode usá-lo para praticar a geração de novos textos.

O repositório da aplicação está disponibilizado [aqui](https://github.com/cecivieira/gerador-posts).

## Conteúdo

Aqui, cada pasta corresponde a um projeto diferente, então dentro delas tem os arquivos de dados utilizados, os templates e posts prontos.

## Como usar a aplicação

Para criar os seus textos, siga os passos abaixo: 

1. Crie um ambiente virtual;
1. Instale o pacote:
    ```bash
    pip install gerador-posts
    ```
1. Crie os arquivos de dados:
    1. Crie a pasta `./dados`;
    1. Dentro dessa pasta, crie dois arquivos de dados: `links.csv` e `variaveis.yaml` (os arquivos devem ter exatamente esses títulos).
1. Escreva os templates:
    1. Crie a pasta `./posts_templates`;
    1. Dentro dessa pasta você pode criar quantos templates desejar, em qualquer formato de arquivo. (para inserir os dados no template use a sintaxe do Jinja2).
1. Crie a pasta aonde os posts prontos serão armazenados: `./posts_prontos`;
1. Execute o pacote:
    ```bash
    (.venv) $ gerar-posts
    ```
1. Feito! Seus posts estão prontos e armazenados na pasta `./posts_prontos`.