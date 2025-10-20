'''

nomeclatura
PASCALCase
CamelCase
-> Snake_Case <-
Kebab-Case

Comentários, pode ser usados como apostrofos ou cerquilhas


'''


print ("\n--------------------")
print ("\fBem vindo ae estudioso! o_o")
print ("\n--------------------")

nome_pessoa = str (input ("Qual o seu nome? "))
print(f"Olá, {nome_pessoa}! ")

idade_pessoa = int(
    input("Qual é sua idade? ")
)
if idade_pessoa >= 18:
    print ("Muito bem, você pode ser preso ^-^ ")

else:
    print ("Aah, que pena! Você não pode ser preso  u_u ")

altura_pessoa = float(input ("Qual é sua altura? "))
print(f"sua altura é {altura_pessoa}! ")

print ("\n-------------------------------------------")
print("Seja muito bem vindo, sinta se a vontade! ^-^")
print ("\n-------------------------------------------")
#print(f"Olá, seu nome é {nome_pessoa}!, sua idade seria {idade_pessoa}, e você diz que sua altura é {altura_pessoa}? ")
#print (f"Olá {nome_pessoa}! Você é maior de idade ^o^ que maneiroo, você tem {altura_pessoa}. Você é bastante alto ^-^)