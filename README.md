# Projeto 1 - Índice HASH

Este projeto implementa um índice hash utilizando programação orientada a objetos em Python. O objetivo é construir um índice para uma tabela, possibilitando a busca rápida de tuplas (linhas) a partir de uma chave de busca. Além disso, o sistema permite a realização de um *table scan* (busca linear) para comparação de desempenho.

## Funcionalidades

- **Construção do Índice Hash:** O índice é construído aplicando uma função hash (a função `hash()` nativa do Python) às chaves de busca de cada tupla, mapeando-as para os endereços das páginas onde estão armazenadas.
- **Busca por Chave (Busca por CB):** A busca utiliza o índice hash para encontrar a página correspondente e retorna os dados da tupla desejada.
- **Table Scan:** Realiza uma busca linear em todas as páginas até encontrar a tupla com a chave especificada.
- **Medição de Desempenho:**
  O tempo de execução das buscas pode ser medido (em milissegundos) para comparação entre os métodos.

## Estrutura do Projeto

- **Tupla.py:** Define a classe `Tupla`, que representa uma linha da tabela. Cada tupla contém uma chave de busca e os dados associados.
- **Tabela.py:** Define a classe `Tabela`, que gerencia as tuplas carregadas a partir do arquivo de dados. Contém os métodos `tableScan` e `buscaPorCB` para efetuar as buscas.
- **Pagina.py:** Define a classe `Pagina`, que representa a divisão da tabela em páginas. Cada página possui um limite de capacidade (número de tuplas) e armazena as tuplas correspondentes. O método `setNovaTupla` é implementado como um método estático para gerenciar a criação e preenchimento das páginas.
- **Bucket.py:** Define a classe `Bucket`, que mapeia as chaves de busca aos endereços das páginas onde as tuplas estão armazenadas. Implementa também a lógica de verificação de tamanho e overflow.
- **Indice.py:** Implementa a classe `Indice`, responsável por criar e gerenciar o índice hash. Contém métodos estáticos para calcular o hash, adicionar buckets, tratar colisões e lidar com overflow.
- **main.py:** Arquivo principal que:

  - Lê os dados do arquivo `words.txt`.
  - Cria as tuplas e as armazena na tabela.
  - Divide os dados em páginas.
  - Constrói o índice hash a partir das informações das páginas.
  - Permite a entrada de uma chave de busca e realiza a busca utilizando o índice e também por meio de table scan.
- **words.txt:** Arquivo de dados contendo uma palavra por linha (dados extraídos do repositório [dwyl/english-words](https://github.com/dwyl/english-words)). Cada palavra é considerada única e serve de chave de busca.
- **Projeto 1 - Índice HASH.docx.pdf:**
  Documento com as instruções e requisitos do projeto, contendo informações sobre as funcionalidades, entidades e parâmetros a serem implementados.

## Requisitos

- **Python 3.x**
  Não há dependências externas além das bibliotecas padrão do Python.

## Como Executar

1. **Clonar o Repositório**: Certifique-se de que todos os arquivos listados (os módulos Python, o `words.txt` e o documento PDF com as instruções) estejam na mesma estrutura de diretórios.
2. **Executar o Programa:**
   Abra um terminal na pasta raiz do projeto e execute:

   ```bash
   python main.py
   ```
3. **Interação com o Sistema:**
   O programa solicitará que você digite uma chave de busca. Após a entrada, serão exibidos os resultados da busca por índice (buscaPorCB) e do table scan, além dos tempos de execução (se implementado).

## Considerações

* **Resolução de Colisões e Overflow:**
  O índice hash foi implementado considerando a possibilidade de colisões e overflow nos buckets, com métodos para tratar essas situações conforme as instruções do projeto.
* **Interface Gráfica:**
  Embora o projeto exija uma interface gráfica para ilustrar as estruturas de dados e o funcionamento do índice, esta implementação apresenta os resultados no console. A inclusão de uma interface gráfica pode ser realizada futuramente, integrando os mesmos conceitos e funcionalidades.

## Autores

* **Eduardo de Morais Tajra** - [GitHub](https://github.com/eduardotajra)
* **Andrei Fernandes Bastos** - [GitHub](https://github.com/afbastos-compsci)
* **Natan Coelho Pucci Benevides** - [GitHub](https://github.com/pucciNatan)
