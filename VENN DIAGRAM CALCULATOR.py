from matplotlib_venn import venn2
import matplotlib.pyplot as plt

plt.title("WELCOME IN VENN DIAGRAM CALCULATOR")

SETS = {}
UNIVERSAL = {1,2,3,4,5,6,7,8,9,10}

def create_set():
    try:
        set_name = input("Enter the name of the set: ")
        elements = input("Enter the elements of the set (comma separated): ").split(",")
        set_elements = set(elements)
        SETS[set_name] = set_elements
        print(f"Set {set_name} created:", set_elements)
        return set_name, set_elements
    except Exception as e:
        print("Invalid input. Please enter a valid set of elements.")


def oprations():
    try:
        print("Choose operation:")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference")
        print("4. Complement")
        choice = input("Enter the operation number: ")


        set1_name = input("Enter the first set name: ")
        set2_name = input("Enter the second set name: ")
        set_1 = SETS[set1_name]
        set_2 = SETS[set2_name]

        if choice == "1":
            print("Union of two sets:", set_1 | set_2)
            venn2([set_1, set_2], set_labels=(set1_name, set2_name))
            plt.title("Union of two sets")
            plt.show(block=False)

        elif choice == "2":
            print("Intersection of two sets:", set_1 & set_2)
            venn2([set_1, set_2], set_labels=(set1_name, set2_name))
            plt.title("Intersection of two sets")
            plt.show(block=False)

        elif choice == "3":
            print("Difference of two sets:", set_1 - set_2)
            venn2([set_1, set_2], set_labels=(set1_name, set2_name))
            plt.title("Difference of two sets")
            plt.show(block=False)

        elif choice == "4":

            complement = UNIVERSAL - set_1
            print(f"Complement of {set1_name} wrt Universal:", complement)
            venn2([set_1, UNIVERSAL], set_labels=(set1_name, "Universal"))
            plt.title("Complement")
            plt.show(block=False)

        else:
            print("Invalid choice. Please try again.")

    except KeyError:
        print("Invalid set name. Please enter a valid set name.")
    except Exception as e:
        print("An error occurred:", e)


def cardinality():
    try:
        set_name = input("Enter the name of the set: ")
        set_elements = SETS[set_name]
        cardinality = len(set_elements)
        print(f"Cardinality of {set_name}: {cardinality}")
    except KeyError:
        print("Invalid set name. Please enter a valid set name.")
    except Exception as e:
        print("An error occurred:", e)

def visualzation():
    try:
        set1_name = input("Enter the first set name: ")
        set2_name = input("Enter the second set name: ")
        set_1 = SETS[set1_name]
        set_2 = SETS[set2_name]

        venn2([set_1, set_2], set_labels=(set1_name, set2_name))
        plt.title("Venn Diagram")
        plt.show(block=False)
    except KeyError:
        print("Invalid set name. Please enter a valid set name.")
    except Exception as e:
        print("An error occurred:", e)

def menu():
    while True:
        try:

            print("1. Create a Set")
            print("2. Perform Set Operations")
            print("3. Cardinality")
            print("4. Visualization")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_set()
            elif choice == 2:
                oprations()
            elif choice == 3:
                cardinality()
            elif choice == 4:
                visualzation()
            elif choice == 5:
                print("Thank you for using the Venn Diagram Calculator!")
                break
            else:
                print("Invalid choice. Please try again.")

            again = input("Do you want to perform another operation? (yes/no): ")
            if again.lower() != "yes":
                break

        except Exception as e:
            print("An error occurred:", e)

menu()
