ile = int(input("Ile lini gwiazdek wyswietlić: "))

# for i in range(ile):
#     for i in range(ile):
#         print("*", end=" ")
#     print("")

# for i in range(ile):
#     for i in range(i+1):
#         print("*", end=" ")
#     print("")

spc = ile -1
for i in range(ile):
    print(" " * spc, end = "")
    spc-=1
    for j in range(i+1):
        print("*", end = " ")
    print("")