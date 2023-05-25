from jinja2 import Environment, FileSystemLoader
import yaml
import os

yaml_path = 'dados/variaveis.yaml'
templates_pasta = './posts_templates'

with open(yaml_path, 'r') as arquivo:
    dados = yaml.safe_load(arquivo)

ambiente = Environment(loader=FileSystemLoader(templates_pasta), trim_blocks=True, lstrip_blocks=True)

for arquivo in os.listdir(templates_pasta):
    template = ambiente.get_template(arquivo)
    with open(f'./posts_prontos/{arquivo}', 'w') as post:
        post.write(template.render(dados))