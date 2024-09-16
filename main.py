# Dylan Stitt
# U3L5
# Set Class 


from Set_Class import Set

def test_set():

    print(" Create Sample Sets ".center(50, "-"))
    A = Set("A", [1, 2, 3])
    B = Set("B", [3, 4, 5, 6, 7])
    C = Set("C")
    D = Set("D", [4, 5])
    E = Set("E")

    sets = [A, B, C, D, E]

    for s in sets:
        print(f"{s.name} = {s}")

    print("\n\n")
    print(" Test \"add_members\" ".center(50, "-"))

    print("\nAdd value 6 to an empty set:")
    print(f"Before: C = {C}")
    C.add(6)
    print(f"After: C = {C}")

    print("\nAdd new value 6 to a non-empty set:")
    print(f"Before: D = {D}")
    D.add(6)
    print(f"After: D = {D}")

    print("\nAdd duplicate value 6 to a non-empty set:")
    print(f"Before: B = {B}")
    B.add(6)
    print(f"After: B = {B}")


    print("\n\n")
    print(" Test \"cardinality\" ".center(50, "-"))

    for s in sets:
        print(f"|{s.name}| = {s.cardinality()}")


    print("\n\n")
    print(" Test \"has_element\" ".center(50, "-"))

    for s in sets:
        print(f"5 ∈ {s.name} = {s.has_element(5)}")


    print("\n\n")
    print(" Test \"is_subset\" ".center(50, "-"))

    for s in sets:
        for t in sets:
            print(f"{s.name} ⊆ {t.name} = {s.is_subset(t)}")

        print()

    print("\n\n")
    print(" Test \"cartesian_product\" ".center(50, "-"))

    for s in sets:
        print(f"A x {s.name} = {A.cartesian_product(s)}")
        print()


    print("\n\n")
    print(" Test \"power_set\" ".center(50, "-"))
    for s in sets:
        print(f"P({s.name}) = {s.power_set()}")
        print()

    print("\n\n")
    print(" Test \"union\" ".center(50, "-"))
    for s in sets:
        print(f"A union {s.name} = {A.union(s)}")
        print()


    print("\n\n")
    print(" Test \"intersection\" ".center(50, "-"))
    for s in sets:
        print(f"B intersection {s.name} = {B.intersection(s)}")
        print()

    print("\n\n")
    print(" Test \"difference\" ".center(50, "-"))

    for s in sets:
        print(f"B-{s.name} = {B.difference(s)}")
        print(f"{s.name}-B = {s.difference(B)}\n")


if __name__ == "__main__":
    test_set()