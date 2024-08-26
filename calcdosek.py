#Calculadora de dose de cloreto de potássio
print("Olá! Sou sua calculadora de dose de cloreto de potássio para correção de solo.\n Por favor, insira os dados a seguir (em decimal, use ponto ao invés de vírgula): ")
print("O teor de K da sua análise de solo: ")
k_da_analise = float(input())
print("Agora, o teor que você deseja alcançar de K")
k_desejado = float(input())
#Vamos calcular a diferença entre os teores
diferenca_Kda_Kde = k_desejado - k_da_analise
#Agora, vamos transformar para miligrama/dm³
resultado_mg_dm3 = diferenca_Kda_Kde * 391
#Vamos transformar agora para kg/ha de K
resultado_kg_ha = resultado_mg_dm3 * 2
#multiplicamos por 1,2 para transformar em K2O
resultado_K2O = resultado_kg_ha * 1.2
print(resultado_K2O)
#Dividimos pelo teor de K2O do que tem dentro do cloreto, vamos usar 
resultado_final = resultado_K2O / 0.6
#resultado será em kg/ha de K
#print("Seu resultado foi calculado para um teor de 60%")
print("Seu resultado é de [ " + str(resultado_final) + "kg/ha ]")
print("Esse cálculo foi feito para um teor de Cloreto de potássio de 60%")
print("\n\n\nSe o teor de K2O for diferente de 60%, por favor, insira a porcentagem correta em (decimal)")
novo_teor = float(input())
novo_teor1 = novo_teor / 100
resultado_novo = resultado_K2O / novo_teor1

print("Seu resultado para esse teor de K2O é de: [" + str(resultado_novo) + "kg/ha ]")
#https://github.com/Y0n1-F0r3sT/Lil-codes
