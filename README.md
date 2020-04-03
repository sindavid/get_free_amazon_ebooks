# get_free_amazon_ebooks

Olá, aqui vou te explicar o que é esse repositorio e como estar utlizando ele!

### O que é?
Recebi no WhatsApp uma mensagem que dizia "50 mil ebooks de graça na Amazon, corram!!!", achei uma coisa interessante e resolvi dar uma olhada. De fato haviam 50 mil ebooks de graça e vivendo em meio ao tédio da quarentena, decidi que queria ter todos aqueles ebooks em minha, mas seria uma tarefa muito demorada, afinal, são dezenas de milhares de itens que eu teria de comprar manualmente um a um. Desenvolvi esse webcrawling para resolver esse problema, ele entra automaticamente no site da Amazon e vai comprando um por um.
### Dependencias
* Python 3.x
*  Selenium
* Geckodriver
### Como usar?
**Importante:** é possível que a Amazon peça para que você autorizar o login através de uma verificação de duas etapas, nesse caso, você terá que fazer login e liberar o navegador que o crawler abrir, feito isso, pode fechar e colocar para rodar novamente.

Recomendo o uso de uma virtual env para rodar o projeto, você pode aprender a criar uma <a href="http://https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais" target="_blank">aqui </a> com esse tutorial.

Caso não tenha o geckodriver instalado e/ou não saiba como, <a href="https://medium.com/beelabsolutions/baixando-e-configurando-o-geckodriver-no-ubuntu-dc2fe14d91c">aqui </a> você encontra um tutorial.

Para instalar a biblioteca Selenium, você precisa rodar no terminal um dos dois comandos (_isso com sua virtualenv ativada_)
> pip install -r requirements.txt

ou
> pip install selenium 

Após esses passos é necessário que você copie o arquivo **user.py.dist**, que esta localizado em _~/config/user.py.dist_, o renomeie removendo _.dist_.
Agora no arquivo _user.py_ insira a seu e-mail e senha da Amazon.

Para executar o projeto você precisa rodar:
_para iniciar sem interface gráfica_
> python app.py 0 

_para iniciar com interface gráfica_
> python app.py 1

Caso você queira ver ele entrando no site e clicando nas coisas, execute com interface gráfica.

Agora é só esperar ele concluir o processo de compra dos ebooks para sua conta :)

___
> Computador utilizado para testes possuía:
> * Ubuntu 18.04.4 LTS
> * I5 8265U
> * 8GB RAM
> * Python 3.8
