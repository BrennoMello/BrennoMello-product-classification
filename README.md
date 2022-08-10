# Classificação de Produtos

A aplicação desenvolvida tem como objetivo a criação de um pipeline de treinamento para um modelo de categorização de produtos e o desenvolvimento de uma API para servir o modelo treinado. Esse repositório é estruturado com os seguintes diretórios:

1. **data**: Local de armazenamento do dataset e do modelo treinado pelo pipeline.
2. **server**: Diretório onde contém a aplicação da API RESTfull app.py. Além disso, contém a aplicação de teste do endpoint: test_app.py. Também contém os arquivos para criação do ambiente de docker e docker-compose.
3. **training**:  Diretório que contém o ambiente para executação do jupyter através do docker e docker-compose. Também contém o notebook jupyter para execução do pipeline de treinamento do modelo no arquivo: train_product_classification.ipynb.

## Execução dos ambientes

* Para realizar o treinamento do modelo deve ser executado o pipeline train_product_classification.ipynb no ambiente do jupyter. Para inciar o servidor do jupyter deve ser executado o seguinte comando no diretório 'training':  
```shell
   $ docker-compose up --build
```
* Para iniciar o serviço de API RESTfull o mesmo comando acima deve ser executado. Porém, deve ser no diretório 'server'. O serviço da API assume que o modelo treinado foi salvo como 'model.pkl' no diretório 'data'.

## Testes

* Após iniciar o serviço RESTfull é possível testar se o serviço está corretamente implantado. Para isso no diretório 'server' deve ser executado o seguinte comando: 

```shell
   $ docker-compose exec api pytest .
```

Apos a execução deve ser apresentado o resultado de um requisição para o serviço de classicação de produtos.

## Consumo do serviço

Para requisições do endpoint do serviço deve ser utilizado o seguinte formato de dados:

```
# Entrada

{
  "products": [
    {
      "title": "Lembrancinha"
    },
    {
      "title": "Roupa de Bebê"
    }
  ]
}
```
```
# Saída

{
  "categories": [
    "Lembrancinha",
    "Bebê"
  ]
}
```

O endpoint definido foi '/predict'. Em ambiente local a URL do serviço ficou definida como: localhost:5000/predict

Para execução de requisições em ambiente local pode ser executado o seguinte comando: 

```shell
   curl --location --request POST 'localhost:5000/predict' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "products": [
                {
                "title": "Lembrancinha"
                },
                {
                "title": "Roupa de Bebê"
                },
                {
                "title": "Mandala Espírito Santo"
                }
            ]
            }'  
```
