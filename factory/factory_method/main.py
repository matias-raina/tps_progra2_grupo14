from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore()
    chi = ChicagoPizzaStore()

    for kind in ["cheese", "veggie", "pepperoni"]:
        p1 = ny.order_pizza(kind)
        print("Ethan ordered:", p1)
        print("---")
        p2 = chi.order_pizza(kind)
        print("Joel ordered:", p2)
        print("---")

if __name__ == "__main__":
    main()
