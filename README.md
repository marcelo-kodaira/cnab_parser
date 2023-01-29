# CNAB Parser

 "CNAB Parser" é um programa desenvolvido em python e Django que tem como objetivo processar arquivos CNAB (padrão utilizado para arquivos de remessa e retorno bancário). Ele fornece uma interface simples para que usuários possam fazer upload de arquivos CNAB, e então exibe informações estruturadas sobre as empresas e operações presentes no arquivo.
 Com isso, é possível ter uma visão geral das transações realizadas, bem como informações sobre as empresas envolvidas, tornando-se uma ferramenta útil para gerenciamento de dados financeiros.
 
 ## Instalação
 1. Criar ambiente virtual
```bash
python -m venv venv
```

2. Ativar venv:
```bash

# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. com o seu ambiente venv ativado
instalar requirements.txt
```bash
pip install -r requirements.txt
```

## Tecnologias
<div>
 <img height="60" width="80"  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
 <img height="60" width="80"  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" />
 <img height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain-wordmark.svg" />
 <img height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain-wordmark.svg" />
</div>

# Documentação do CNAB

| Descrição do campo | Inicio | Fim | Tamanho | Comentário                                                                                                                |
| ------------------ | ------ | --- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| Tipo               | 1      | 1   | 1       | Tipo da transação                                                                                                         |
| Data               | 2      | 9   | 8       | Data da ocorrência                                                                                                        |
| Valor              | 10     | 19  | 10      | Valor da movimentação. _Obs._ O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo. |
| CPF                | 20     | 30  | 11      | CPF do beneficiário                                                                                                       |
| Cartão             | 31     | 42  | 12      | Cartão utilizado na transação                                                                                             |
| Hora               | 43     | 48  | 6       | Hora da ocorrência atendendo ao fuso de UTC-3                                                                             |
| Dono da loja       | 49     | 62  | 14      | Nome do representante da loja                                                                                             |
| Nome loja          | 63     | 81  | 19      | Nome da loja                                                                                                              |

# Documentação sobre os tipos das transações

| Tipo | Descrição              | Natureza | Sinal |
| ---- | ---------------------- | -------- | ----- |
| 1    | Débito                 | Entrada  | +     |
| 2    | Boleto                 | Saída    | -     |
| 3    | Financiamento          | Saída    | -     |
| 4    | Crédito                | Entrada  | +     |
| 5    | Recebimento Empréstimo | Entrada  | +     |
| 6    | Vendas                 | Entrada  | +     |
| 7    | Recebimento TED        | Entrada  | +     |
| 8    | Recebimento DOC        | Entrada  | +     |
| 9    | Aluguel                | Saída    | -     |

