double=[x*2 for x in range(1, 11)]
triples=[x*3 for x in range(1, 11)]
squares=[x*x for x in range(1, 11)]

# print(double)
# print(triples)
# print(squares)


fruits=["apple", "mango", "orange", "pineapple"]
# fruits=[fruit.upper() for fruit in fruits]
fruit_chars=[fruit[0].upper() for fruit in fruits]
print(fruit_chars)


nums=[1, -2, 3, -4, 5, -6, -7, 8]

positive_nums=[num for num in nums if num >=0 ]
negative_nums=[num for num in nums if num <=0 ]
even_nums=[num for num in nums if num%2==0 ]
odd_nums=[num for num in nums if num%2==1 ]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)