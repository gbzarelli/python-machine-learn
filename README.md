# Python Machine Learn

Studies with machine learn in Python. These lessons are based on the ['Machine Learn' training of Alura](https://cursos.alura.com.br/formacao-machine-learning).
	
#### [pt][Machine Learn introduction to training]
Como seres humanos somos capazes de aprender como detectar diversos tipos de padrões. Contudo, com o avanço na quantidade e qualidade de dados que capturamos, fica cada vez mais difícil elaborar em nossa cabeça um modelo que descreva o que acontece ou acontecerá em determinadas situações.

Para isso utilizamos técnicas de aprendizado de máquina, Machine Learning, onde aprendemos com os dados que coletamos, melhorando processos, produtos e serviços.

Imagine, por exemplo, uma escola do ensino médio que consegue prever se alunos ou alunas estão correndo risco de desistir do curso, para poder trazer uma solução antes disso acontecer. Ou uma empresa que consegue recomendar produtos que fazem sentido para um cliente dado a lista de compras e visualizações passadas.

Uma marca de sucos saudáveis que passa a entender o consumo de acordo com a temperatura e chuva no dia a dia de um ano, podendo então prever as vendas e minimizar o desperdício de produção...seria o máximo, não é?

E que tal um sistema que detecta fraudes em cartões de crédito no exato instante que tentam fraudá-lo? Ou ainda um site que revela usuários com comportamento estranho, indício de um hacker ou uso mal intencionado?

Na prática, ao invés de implementarmos heurísticas simples, podemos treinar algoritmos, testar, validar contra modelos de base e colocá-los em produção, medindo o resultado de nossos modelos.

Nem tudo é mágica, não existem garantias que um método simples ou complexo de Machine Learning irá funcionar sempre. Portanto, nos cursos desta Formação vamos ver diversas maneiras de atacar problemas, sempre tentando resolver ou olhar nossos desafios de pontos de vista diferentes, encontrando a melhor ferramenta para cada solução.

Como profissional de Machine Learning, você pode entrar em um mercado que está crescendo cada vez mais e ajudar as empresas a otimizar recursos, escalar atendimento, aumentar segurança do trabalho ou diminuir falhas e muito mais.

## In these samples we will use that libaries:

- [Scikit](https://scikit-learn.org)
- [Pandas](https://pandas.pydata.org)

#### Installing libaries:
    
   - Scikit:
    	
    	$pip install -U scikit-learn

   - Pandas:

    	$pip install pandas
    	$pip install pandas --upgrade

## Projects:

All projects contain a learning sequence, containing what was learned in the previous ones, the lessons will be inserted in that README in order.

### Firsts steps - Introduction to classification

#### 1 [First Classification](https://github.com/gbzarelli/python-machine-learn/tree/master/1_first_classification)
 In this project we can see how to implement the Multinomial ([MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)) algorithm from the sklearn.naive_bayes library. 
 	- Libraries used: `Scikit`

#### 2 [Categorical Variable](https://github.com/gbzarelli/python-machine-learn/tree/master/2_categorical_variable)
 The categorical variables are variables that we can not classify only with binary values, that is, 0 and 1 or -1 and 1. One of the examples we used was the search variable that contained the values: algorithms, Java and Ruby. Note that if a variable can have more than one possible value, we consider it as a categorical variable.
  	- Libraries used: `Scikit`, `Pandas`

