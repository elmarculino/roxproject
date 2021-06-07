# RoxProject

Projeto de engenharia e análise de dados de empresa de produção de bicicletas visando a criação de infraestrutura cloud na AWS e o carregamento dos dados armazenados na S3 para Data Warehouse Redshift. 

![airflow dag execution](https://github.com/elmarculino/roxproject/blob/master/images/airflow_stage_execution.png?raw=true)

### objetivos:

- Fazer a modelagem conceitual dos dados;
- Criação da infraestrutura necessária;
- Criação de todos os artefatos necessários para carregar os arquivos para o banco criado;
- Desenvolvimento de SCRIPT para análise de dados;
- (opcional) Criar um relatório em qualquer ferramenta de visualização de dados.

## Desenvolvimento

O desenvolvimento da solução foi feito, em sua maioria, utilizando Programação Interativa em Jupyter Notebooks em um ambiente Anaconda com Python 3.9.4. Parte do código utilizado, como funções específicas, foi retirado das documentações da AWS ou dos pacotes utilizados. 

Todo o código pode ser análisado e executado diretamente nos notebooks e os scripts de criação da infraestrutura cloud na AWS e migração de dados podem ser exportados para serem executados diretamente no terminal.

A criação do ambiente cloud na AWS e a conexão com bancos de dados locais dependem das variáveis salvas no arquivo __dwh.cfg__. No repositório foi disponibilizado um __dwh.cfg.modelo__ para que seja editado com a KEY e SECRET do usuário da AWS. As demais variáveis do arquivo foram mantidas como exemplo.

Para a resolução dos desafios apresentados foram utilizadas as seguintes ferramentas: 

Apache Spark
Pandas Dataframe
PostgresSQL
Infraestrutura cloud da AWS
Apache Airflow 
Jupyter Notebook

## Como Utilizar

#### Jupyter Notebooks

Para executar o código disponibilizado nos notebooks é necessário que se tenha o pacote Jupyter instalado no ambiente Python. A maneira mais conveniente de ter vários ambientes virtuais python é com o pacote Anaconda ou com pyenv. Já com o ambiente ativado é só executar o comando __jupyter notebook__ ou __jupyter lab__ e entrar com endereço apresentato no terminal pelo browser. Os notebooks devem ser executados célula a célula sequencialmente e de acordo com as instruções disponibilizadas nos mesmos. 

#### Apache Airflow

O processo de criação das tabelas no Data Warehouse e o carregamento dos dados foi automatizado em um Dag do Airflow. Para utilizar é preciso entrar na pasta __airflow__ pelo terminal, executar __docker-compose up__ para que com containers Docker sejam iniciados e entrar na interface web para executar o Dag __stage_rox_bike_tables__. 

#### Python Scripts (TODO)

O repositório do projeto foi configurado com o pacote __nbdev__ que gera os scripts python automativamente de acordo com marcações nas células. Esta atualização dos notebooks e a geração dos scripts é o próximo passo no desenvolvimento do projeto. 


## Roteiro de Desenvolvimento

Os notebooks foram numerados de acordo com uma ordem lógica de execução. No entando, o desenvolvimento dos mesmos não foi linear. Apenas como exemplo, o primeiro notebook criado foi o __analise_dados_spark.ipynb__ já que o Apache Spark permite a importação dos arquivos CSV e a execução de queries SQL nos Dataframes gerados diretamente dos arquivos de texto.

    ├── 00_criacao_infra_aws.ipynb
    ├── 01_prepacacao_dados_pandas.ipynb
    ├── 02_envio_arquivos_s3.ipynb
    ├── 03_criacao_tablelas_redshift.ipynb
    ├── 04_analise_dados_spark.ipynb
    ├── 05_criacao_tabelas_postgres.ipynb
    ├── 06_analise_dados_postgres.ipynb

#### 00_criacao_infra_aws.ipynb
    
Código para a criação do banco de bados no Redshift, o Bucket no S3 e Permissões necessárias para a troca de dados e o acesso externo aos serviços da Amazon.

#### 01_prepacacao_dados_pandas.ipynb

Notebook usado para a preparação dos arquivos CSV com tipos compatíveis com o Schema para a importação. Durante o desenvolvimento deste notebook foram também criadas as queries de criação das tabelas com os tipos e relacionamentos apresentados no notebook 03.

#### 02_envio_arquivos_s3.ipynb

Código para o upload dos arquivos CSV preparados para o bucket do projeto, criado no notebook 01, utilizando o cliente Python do S3. 

#### 03_criacao_tablelas_redshift.ipynb

Notebook para a execução dos códigos SQL para criação das tabelas no Redshift e o carregamento dos dados armazenados no S3 utilizano o comando SQL __COPY__.

#### 04_analise_dados_spark.ipynb

Importação dos dados em CSV para Dataframes Spark para a realização das consultas solicitadas. Neste notebook estão disponiveis as queries e os resultados como respostas para os questionamentos apresentados no arquivo de apresentação do projeto. 

#### 05_criacao_tabelas_postgres.ipynb

Notebook utilizado para o desenvolvimento dos Schemas das tabelas do banco de dados. Como o Redshift é baseado no PostgresSQL a utilização de um ambiente local compativel é mais rápido e econômico.

#### 06_analise_dados_postgres.ipynb

Foram executadas as mesmas consultas do notebook Spark mas agora nas tabelas criadas com base nos arquivos CSV. O objetivo dessa segunda execução foi realizar o nos dados após tratamento para identificar eventuais deferenças. Também apresenta as responstas para as questões do arquivo de apresentação do projeto.

## Objetivos

Além do desenvolvimento em notebooks, foi também incluido no repositório a pasta __airflow/__ com o _docker-compose.yaml_ para a criação da infraestrutura necessária para a automação dos processoas. Foi criado DAG para criação da tabelas no Redshift e o carregamento dos dados dos arquivos CSV de forma automática. Foram criados também Operators com o objetivo de deixar o código do DAG mais limpo mas esse acabou não sendo usado na execução teste.


![airflow dag execution](https://github.com/elmarculino/roxproject/blob/master/images/airflow_stage_execution.png?raw=true)

Com o objetivo de testar os dados e a integração dos serviços AWS foi 
criado um dashboard para a visualização dos dados de total de vendas por dia demonstrado no print abaixo.

![quicksight dashboard](https://github.com/elmarculino/roxproject/blob/master/images/dashboard_quicksight.png?raw=true)

## Conclusão

Os objetivos o projeto exigiram o uso de uma gama variada de tecnologias de engenharia e análise de dados, computação na nuvem e automação.  No entanto, a solução entregue, com o devido tempo, pode ser melhorada. As tabelas no Data Warehouse, por exemplo, podem ser modificadas para uma estrutura de Fatos e Dimensões e a distribuição pode ser modificada para melhorar a velocidade das queries. A automação desenvolvida utilizando o Airflow pode incluir o processamento e transformação dos dados para as novas tabelas, além de todo o tratamento dos arquivos CSV.

Outro ponto de melhora seria a entrega um dashboard interativo como o demonstrado acima ou utilizando ferramentas open source como o Graphana.

Como citado anteriormentei, a atualização dos notebooks para a geração automática dos scripts python é o próximo passo natural para o projeto.  

O projeto foi um ótimo exercicio. Espero que gostem!
