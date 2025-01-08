def perfume():
    initialperfume = 0
    while True:
        initialperfume += 1
        yield initialperfume

def cosmetics():
    initialcosmetics = 0
    while True:
        initialcosmetics += 1
        yield initialcosmetics

# Generator for medicine tickets
def medicine():
    initialmedicine = 0
    while True:
        initialmedicine += 1
        yield initialmedicine

perfumegen = perfume()
cosmeticsgen = cosmetics()
medicinegen = medicine()

def perfume_recursion(ticketnumber):
    print(f"Hello\nYour perfume ticket is: A-{ticketnumber}\nThank you for waiting")

def cosmetics_recursion(ticketnumber):
    print(f"Hello\nYour cosmetics ticket is: B-{ticketnumber}\nThank you for waiting")

def medicine_recursion(ticketnumber):
    print(f"Hello\nYour medicine ticket is: C-{ticketnumber}\nThank you for waiting")

while True:
    choice = input("Type 'perfume', 'cosmetics', 'medicine', or 'exit' to leave: ")
    if choice == "perfume":
        ticketnumber = next(perfumegen)
        perfume_recursion(ticketnumber)
    elif choice == "cosmetics":
        ticketnumber = next(cosmeticsgen)
        cosmetics_recursion(ticketnumber)
    elif choice == "medicine":
        ticketnumber = next(medicinegen)
        medicine_recursion(ticketnumber)
    elif choice == "exit":
        print("Thank you for visiting!")
        break

print('practice')




