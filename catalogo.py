# lista para exibir os produtos disponíveis
catalogo_produtos = ['maçã', 'banana', 'uva', 'mamão', 'pêssego']

# função para adicionar um produto ao catálogo de produtos
def adicionar_produto():
    print('\nVocê está a adicionar um novo produto.')

    novo_produto = str(input('\nDigite um nome para o produto a ser adicionado: '))
    novo_produto.lower()

    # verifica se o produto especificado já existe
    if (novo_produto in catalogo_produtos):
        print('\n{0} já existe no catálogo! Retornando ao menu...\n'.format(novo_produto))
        voltar_ao_menu()
    else:
        catalogo_produtos.append(novo_produto)
        print('{0} adicionado(a) com sucesso ao catálogo! Retornando ao menu...\n'.format(novo_produto))
        voltar_ao_menu()

# função para remover um produto do catálogo de produtos
def remover_produto():
    deseja_continuar = 's'

    print('\nVocê está a remover um novo produto.')

    while (deseja_continuar == 's'):
        print('Produtos no catálogo: {0}'.format(catalogo_produtos))

        # verifica se a lista está vazia
        if (len(catalogo_produtos) == 0):
            print('\nNão existem itens no catálogo! Retornando ao menu...\n')
            voltar_ao_menu()
        else:
            produto = str(input('\nDigite um nome para o produto a ser removido: '))
            produto.lower()

            # verifica se o produto especificado está na lista, caso sim, remova-o
            if (produto in catalogo_produtos):
                # remove o produto de catalogo_produtos
                catalogo_produtos.remove(produto)
                print('{0} removido(a) com sucesso! Retornando ao menu...'.format(produto))
                voltar_ao_menu()
            else:
                deseja_continuar = str(input("{0} não foi encontrado! Pressione 'S' para tentar novamente OU 'N' para voltar ao menu: ".format(produto)))
                deseja_continuar.lower()

                if (deseja_continuar != 's' and deseja_continuar != 'n'):
                    print('Comando inválido! Retornando...')
                    deseja_continuar = 's'

                # se a resposta é 'n' então saia do loop
                if (deseja_continuar == 'n'):
                    break

# função para retornar ao menu
def voltar_ao_menu():
    import main
    main.mostrar_menu()
