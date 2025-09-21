import sympy as sp

try:
    symbols_input = int(input("How many symbols u want?: "))
    name = input("enter the 3 symbol name e.g (y x z)")

    symbols_tuple = sp.symbols(name)
    print(symbols_tuple)

    Equations_list = []
    for i in range(symbols_input):
        eq = input(f"Enter equation {i + 1} (in terms of ({symbols_tuple}), use '=' for equals): ")

        lhs, rhs = eq.split("=")

        sympify = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        print(sympify)
        Equations_list.append(sympify)

    solve = sp.solve(Equations_list)
    print("The solution is:", solve)


except Exception as e:
    print(f"An error occurred: {e}")
