import PySimpleGUI as sg


sg.change_look_and_feel('DarkTeal12')
        # Layout
layout = [
            [sg.Text('Conjunto de Numeros:', size =(16,0)), sg.Input(size =(25,0), key = 'ordena')],
            [sg.Text('Qual ordenação deseja?')],
            [sg.Button('Insertion_Sort'),sg.Button('Bubble_Sort'),sg.Button('Selection_Sort'),sg.Button('Strand_Sort')],
            [sg.Text('')],
            [sg.Button('Enviar Dados'),sg.Button('Limpar Lista')],
            [sg.Output(size=(50,20),key= 'output')]

        ]
        # janela

window = sg.Window('Métodos de ordenação', layout)

lista = []
while True:
    event, values = window.read()

    if event == 'Enviar Dados':
        try:
            lista += [int(values['ordena'])]
            window['output'].update(lista)

        except ValueError:
            print('Digite um valor válido!')


    elif event == 'Insertion_Sort':
        print('\nMétodo Insertion Sort: ')

        def insertion_sort(lista):
            n = len(lista)  # pegar o tamanho da lista
            for i in range(1, n):
                chave = lista[i]  # pegar o elemento que esta na posição i
                j = i - 1  # "j" representa a lista que ja esta ordenada

                while j >= 0 and lista[j] > chave:  #
                    lista[j + 1] = lista[j]  # Comparando a lista

                    j = j - 1  # para limitar o loop

                lista[j + 1] = chave  # a posição que se insere a chava, sempre uma posiçao a mais


        insertion_sort(lista)  # Executa a função
        print(lista)

    elif event == 'Bubble_Sort':

        def bubble_sort(lista):
            n = len(lista)  # ver o tamanho da lista
            for j in range(n - 1):
                for i in range(n - 1):
                    if lista[i] > lista[i + 1]:
                        # troca de elementos nas posições i e i+1
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]


        bubble_sort(lista)
        print(f'\n Método do Bubble sort: {lista}')

    elif event == 'Selection_Sort':
        print('\nMétodo do Selection Sort:')
        def selection_sort(numeros):
            for index in range(0, len(numeros)):
                min_index = index  # pra cada posição grava o numero minimo

                for right in range(index + 1, len(numeros)):
                    # percorre o resto do array procurando o item minimo
                    if numeros[right] < numeros[min_index]:
                        min_index = right  # quando achar o menor item associa ele com a variável
                # no final faz a troca
                numeros[index], numeros[min_index] = numeros[min_index], numeros[index]



        selection_sort(lista)
        print(lista)

    elif event == 'Strand_Sort':

        def strand_sort(inp):
            output = strand(inp)
            while len(inp):
                output = merge(output, strand(inp))
            return output


        def strand(inp):
            element, sub = 0, [inp.pop(0)]
            while element < len(inp):
                if inp[element] > sub[-1]:
                    sub.append(inp.pop(element))
                else:
                    element += 1
            return sub


        def merge(a, b):
            output = []
            while len(a) and len(b):
                if a[0] < b[0]:
                    output.append(a.pop(0))
                else:
                    output.append(b.pop(0))
            output += a
            output += b
            return output

        output = strand_sort(lista)
        print("\nMétodo Strand Sort:")
        print(output)

    elif event == 'Sair' or event == sg.WIN_CLOSED:  # cria o evento de saida
        break

    elif event == 'Limpar Lista':
        lista.clear()
        sg.popup('Lista foi limpa!')