def fibonacci(n):
    if n <= 1:
      return n
    else:
       return fibonacci(n-1) + fibonacci(n-2)
    
numero_terminos = 10
print("Serie de Fibonacci: ")
for i in range(numero_terminos):
   print(fibonacci(i))        