import pytest
from .store import NYPizzaStore, ChicagoPizzaStore
from .pizza import CheesePizza, ClamPizza, VeggiePizza, PepperoniPizza


def test_ny_cheese_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert "NY Style" in pizza.name
    assert isinstance(pizza, CheesePizza)
    assert pizza.dough.name == "Thin Crust Dough"
    assert pizza.sauce.name == "Marinara Sauce"
    assert pizza.cheese.name == "Reggiano Cheese"


def test_chicago_clam_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert "Chicago Style" in pizza.name
    assert isinstance(pizza, ClamPizza)
    assert pizza.dough.name == "Thick Crust Dough"
    assert pizza.sauce.name == "Plum Tomato Sauce"
    assert pizza.cheese.name == "Mozzarella Cheese"
    assert pizza.clam.name == "Frozen Clams"


def test_ny_veggie_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("veggie")
    assert "NY Style" in pizza.name
    assert isinstance(pizza, VeggiePizza)
    assert pizza.dough.name == "Thin Crust Dough"
    assert pizza.sauce.name == "Marinara Sauce"
    assert pizza.cheese.name == "Reggiano Cheese"
    assert "Mushroom" in pizza.veggies.name
    assert "Onion" in pizza.veggies.name
    assert "Red Pepper" in pizza.veggies.name


def test_chicago_pepperoni_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("pepperoni")
    assert "Chicago Style" in pizza.name
    assert isinstance(pizza, PepperoniPizza)
    assert pizza.dough.name == "Thick Crust Dough"
    assert pizza.sauce.name == "Plum Tomato Sauce"
    assert pizza.cheese.name == "Mozzarella Cheese"
    assert pizza.pepperoni.name == "Sliced Pepperoni"

def test_invalid_pizza_type():
    store = NYPizzaStore()
    with pytest.raises(ValueError, match="No NY pizza for kind: invalid_type"):
        store.order_pizza("invalid_type")