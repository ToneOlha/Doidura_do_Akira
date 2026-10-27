from console import console


# Cria um Título (algo muito importante, ja que vai dividir as coisas e deixar mais legal)
console.rule("[bold red]Chapter 2", align="left", style="Red") # align="" define onde ficará a string na tela

# teste de uso, aparentemente é possivel fazer algumas identifações no terminal
console.print([1, 2, 3], justify="center") # algo parecido com uma cadeia de números ou vetores
console.print("[blue underline]Looks like a link") # aparencia de um LINK de navegador
console.print(locals()) #aparentemente um log
console.print("FOO", style="white on blue") # Style = "" faz com que surja uma especie de fundo na mensagem


# Forma de carregamento
with console.status("Monkeying around...", spinner="monkey"): # cria um carregamento visual no console
    for i in range(1, 10000): # O que vai estar fazendo durante o carregamento?
        print(i)
    