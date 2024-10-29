a = 5 # 0101
      # 8421

a = a << 1    # 01010
print(a)

a = a << 2    # 0101000
print(a)
# desloca p/ esquerda, add o 0 no final

a = a >> 3    
print(a)
# desloca p/ direita, tira o último número 

