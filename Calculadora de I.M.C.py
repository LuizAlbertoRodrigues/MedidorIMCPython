#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Medidor de IMC 
# Created by Luiz Alberto 


peso = float(input('Digite seu Peso : '))
altura = float(input('Digite sua Altura : '))
imc = peso/altura **2 
print('Seu IMC é :', imc)
if imc < 18.5 :
    print('Você está abaixo do peso')
elif imc < 24.9 :
    print('Parabéns você está no seu Peso Ideal')
elif imc > 25.0 and imc < 29.9 :
    print('Você está levemente acima do Peso')
elif imc > 30.0 and imc < 34.9 :
    print('ATENÇÃO OBESIDADE GRAU 1')
elif imc > 35.0 and imc < 39.9 :
    print('ATENÇÃO OBESIDADE SEVERA GRAU 2')
elif imc > 40.0 :
    print('ATENÇÃO VOCÊ ESTÁ NA OBESIDADE MÓRBIDA, PROCURE UM MÉDICO')
print('Obrigado por consultar seu I.M.C !!!')

