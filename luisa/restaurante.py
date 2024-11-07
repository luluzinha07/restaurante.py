# Menu do restaurante
menu = {
    "Hamburguer": 15.00,
    "Pizza": 20.00,
    "Salada": 10.00,
    "Refrigerante": 5.00,
    "Cerveja": 8.00
}

def exibir_menu():
    """Exibe o menu do restaurante."""
    print("Menu do Restaurante:")
    for prato, preco in menu.items():
        print(f"{prato}: R${preco:.2f}")

def fazer_pedido():
    """Permite que o usuário faça um pedido."""
    pedido = []
    while True:
        prato = input("Digite o nome do prato que deseja ou 'sair' para finalizar: ")
        if prato.lower() == 'sair':
            break
        elif prato in menu:
            pedido.append(prato)
            print(f"{prato} adicionado ao pedido.")
        else:
            print("Prato não disponível. Tente novamente.")
    return pedido

def calcular_total(pedido):
    """Calcula o total do pedido."""
    total = sum(menu[prato] for prato in pedido)
    return total

def main():
    """Função principal para executar o simulador de restaurante."""
    exibir_menu()
    pedido = fazer_pedido()
    total = calcular_total(pedido)
    
    if pedido:  # Verifica se há itens no pedido
        print(f"\nSeu pedido: {pedido}")
        print(f"Total a pagar: R${total:.2f}")
    else:
        print("Nenhum pedido realizado.")

if __name__ == "__main__":
    main()
