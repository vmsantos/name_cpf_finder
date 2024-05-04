import re

def validador(cpf):
  #cpf = str(input("Digite um CPF para ser validado ao lado. >>>"))

  #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
  numeros = [int(digito) for digito in cpf if digito.isdigit()]
  
  formatacao = False
  quant_digitos = False
  validacao1 = False
  validacao2 = False

  #Verifica a estrutura do CPF (111.222.333-44)
  if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
      formatacao = True

  if len(numeros) == 11:
      quant_digitos = True
  
      soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
      digito_esperado = (soma_produtos * 10 % 11) % 10
      if numeros[9] == digito_esperado:
          validacao1 = True

      soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
      digito_esperado1 = (soma_produtos1 *10 % 11) % 10
      if numeros[10] == digito_esperado1:
          validacao2 = True

      if quant_digitos == True and formatacao == True and validacao1 == True and validacao2 == True:
            return 1
          #print(f"O CPF {cpf} é válido.")
      else:
            return 0 
          #print(f"O CPF {cpf} não é válido... Tente outro CPF...")

  else:
    return 0 
    #print(print(f"O CPF {cpf} não é válido... Tente outro CPF..."))

def generate_cpf(fixed_middle):
    # Split the fixed middle part into the first and second parts
    first_part, second_part = fixed_middle.split('.')

    # Generate all possible combinations for the first three digits
    for i in range(0, 1000):
        first_part_str = str(i).zfill(3)

        # Generate all possible combinations for the last two digits
        for j in range(0, 100):
            last_part_str = str(j).zfill(2)

            # Combine the parts
            cpf = first_part_str + '.' + first_part + '.'  + second_part + '-' + last_part_str    
            x = validador(cpf) 
            if x == 1:
                print(cpf)    
            #print(cpf)

generate_cpf('456.789')

x = validador('123.456.789-09')
print(x)
