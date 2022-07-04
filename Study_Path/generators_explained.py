gen_exp =(i ** 2 for i in range(1,11) if i % 2 == 0)

print(gen_exp)

for i in gen_exp:
    print(i)

for i in gen_exp:
    print(i)
# noting will be printed as the generator is exhausted using the first loop, so no more items

