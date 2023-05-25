from jinja2 import Environment, FileSystemLoader
import yaml
import os

yaml_path = 'dados/variaveis.yaml'
templates_pasta = './posts_templates'

# Carrega variáveis do yaml
with open(yaml_path, 'r') as arquivo:
    dados = yaml.safe_load(arquivo)

# Identifica pasta com templates e estabelece configurações para identação e quebra de linha dos trechos que usa Jinja
ambiente = Environment(loader=FileSystemLoader(templates_pasta), trim_blocks=True, lstrip_blocks=True)

# Aplica configurações do ambiente em cada template
for arquivo in os.listdir(templates_pasta):
    template = ambiente.get_template(arquivo)
    with open(f'./posts_prontos/{arquivo}', 'w') as post:
        post.write(template.render(dados)) # Aplica variáveis do yaml no template e salva o arquivo