nome_produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = (preco_original * desconto_percentual) / 100
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")