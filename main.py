# Criando um analisador de vendas
import pandas as pd

# Carregando os dados da tabela
tabela = pd.read_excel('Vendas.xlsx')



# Evita valores vazios na tabela
if tabela.isnull().values.any():
    print("Existem valores nulos na tabela. Verifique os dados!")



# ----------------------------------------------------------------------
# Encontrando o total de vendas da empresa
tabela['Total'] = tabela['Quantidade'] * tabela['Valor Unitário']
total_vendas = tabela['Total'].sum()

print('O total de vendas foi de R${:,.2f}'.format(total_vendas))



# ----------------------------------------------------------------------
# Encontrando o produto mais vendido 
print(20 * "---")
produto_mais_vendido = tabela.groupby('Produto')['Quantidade'].sum().idxmax()
produto_mais_vendido_qtd = tabela.groupby('Produto')['Quantidade'].sum().max()

print('O produto mais vendido em quantidade foi {} com {} unidades vendidas'.format(produto_mais_vendido, produto_mais_vendido_qtd))



# ----------------------------------------------------------------------
# Total de vendas por loja
print(20 * "---")
vendas_por_loja = tabela.groupby('ID Loja')['Total'].sum()
vendas_por_loja = vendas_por_loja.apply(lambda x: f"R$ {x:,.2f}")

print('Total de vendas por loja foi: \n{}'.format(vendas_por_loja))

