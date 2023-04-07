def fibonacci():
    n = int(input("Lütfen bir sayı giriniz:"))
    while n < 20:
         print("Lütfen 20 veya daha büyük bir sayı giriniz.")
         n = int(input("Lütfen bir sayı giriniz:"))
    fib = [1,1]
    while len(fib) < n:
          fib.append(fib[-1]+ fib[-2])
    return fib
fibonacci_list = fibonacci()
print(fibonacci_list)






     



