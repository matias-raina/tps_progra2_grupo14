# test_decorator.py
# Comprehensive tests for the Decorator pattern implementation
# Testing costs and descriptions for various combinations including doubles and sizes

from decimal import Decimal

import pytest
from beverages import DarkRoast, Decaf, Espresso, HouseBlend, Size
from builder import build_beverage
from condiments import Caramel, Milk, Mocha, PrettyDescriptionDecorator, Soy, Whip


class TestBasicBeverages:
    """Test basic beverage functionality without condiments."""

    def test_espresso_basic(self):
        """Test Espresso basic cost and description."""
        espresso = Espresso()
        assert espresso.cost() == Decimal("1.99")
        assert espresso.get_description() == "Espresso"
        assert espresso.get_size() == Size.TALL  # Default size

    def test_dark_roast_basic(self):
        """Test DarkRoast basic cost and description."""
        dark_roast = DarkRoast()
        assert dark_roast.cost() == Decimal("0.99")
        assert dark_roast.get_description() == "Café Dark Roast"

    def test_house_blend_basic(self):
        """Test HouseBlend basic cost and description."""
        house_blend = HouseBlend()
        assert house_blend.cost() == Decimal("0.89")
        assert house_blend.get_description() == "Café de la Casa"

    def test_decaf_basic(self):
        """Test Decaf basic cost and description."""
        decaf = Decaf()
        assert decaf.cost() == Decimal("1.05")
        assert decaf.get_description() == "Café Descafeinado"


class TestSizeOperations:
    """Test size setting and getting operations."""

    def test_default_size(self):
        """Test that beverages have TALL as default size."""
        espresso = Espresso()
        assert espresso.get_size() == Size.TALL

    def test_set_size(self):
        """Test setting different sizes."""
        espresso = Espresso()

        espresso.set_size(Size.GRANDE)
        assert espresso.get_size() == Size.GRANDE

        espresso.set_size(Size.VENTI)
        assert espresso.get_size() == Size.VENTI

        espresso.set_size(Size.TALL)
        assert espresso.get_size() == Size.TALL


class TestSingleCondiments:
    """Test single condiment decorators."""

    def test_milk_tall(self):
        """Test Milk condiment on TALL size."""
        espresso = Espresso()
        espresso.set_size(Size.TALL)
        milk_espresso = Milk(espresso)

        expected_cost = Decimal("1.99") + Decimal("0.10")  # Espresso + Milk TALL
        assert milk_espresso.cost() == expected_cost
        assert "Leche" in milk_espresso.get_description()
        assert milk_espresso.get_size() == Size.TALL

    def test_mocha_grande(self):
        """Test Mocha condiment on GRANDE size."""
        house_blend = HouseBlend()
        house_blend.set_size(Size.GRANDE)
        mocha_house_blend = Mocha(house_blend)

        expected_cost = Decimal("0.89") + Decimal("0.25")  # HouseBlend + Mocha GRANDE
        assert mocha_house_blend.cost() == expected_cost
        assert "Mocha" in mocha_house_blend.get_description()
        assert mocha_house_blend.get_size() == Size.GRANDE

    def test_soy_venti(self):
        """Test Soy condiment on VENTI size (as specified in README)."""
        dark_roast = DarkRoast()
        dark_roast.set_size(Size.VENTI)
        soy_dark_roast = Soy(dark_roast)

        expected_cost = Decimal("0.99") + Decimal("0.20")  # DarkRoast + Soy VENTI
        assert soy_dark_roast.cost() == expected_cost
        assert "Soja" in soy_dark_roast.get_description()
        assert soy_dark_roast.get_size() == Size.VENTI

    def test_whip_tall(self):
        """Test Whip condiment on TALL size."""
        decaf = Decaf()
        decaf.set_size(Size.TALL)
        whip_decaf = Whip(decaf)

        expected_cost = Decimal("1.05") + Decimal("0.10")  # Decaf + Whip TALL
        assert whip_decaf.cost() == expected_cost
        assert "Crema" in whip_decaf.get_description()

    def test_caramel_grande(self):
        """Test Caramel condiment (new from Nivel 1)."""
        espresso = Espresso()
        espresso.set_size(Size.GRANDE)
        caramel_espresso = Caramel(espresso)

        expected_cost = Decimal("1.99") + Decimal("0.25")  # Espresso + Caramel GRANDE
        assert caramel_espresso.cost() == expected_cost
        assert "Caramelo" in caramel_espresso.get_description()


class TestMultipleCondiments:
    """Test multiple condiments including doubles and triples."""

    def test_double_mocha(self):
        """Test double Mocha (Nivel 1 requirement)."""
        dark_roast = DarkRoast()
        dark_roast.set_size(Size.TALL)

        # Add two Mocha decorators
        double_mocha = Mocha(Mocha(dark_roast))

        expected_cost = (
            Decimal("0.99") + Decimal("0.20") + Decimal("0.20")
        )  # DarkRoast + 2x Mocha TALL
        assert double_mocha.cost() == expected_cost
        assert double_mocha.get_description() == "Café Dark Roast, Mocha, Mocha"

    def test_triple_caramel(self):
        """Test triple Caramel."""
        house_blend = HouseBlend()
        house_blend.set_size(Size.TALL)

        # Add three Caramel decorators
        triple_caramel = Caramel(Caramel(Caramel(house_blend)))

        expected_cost = (
            Decimal("0.89") + Decimal("0.20") + Decimal("0.20") + Decimal("0.20")
        )  # HouseBlend + 3x Caramel TALL
        assert triple_caramel.cost() == expected_cost
        assert (
            triple_caramel.get_description()
            == "Café de la Casa, Caramelo, Caramelo, Caramelo"
        )

    def test_mixed_condiments(self):
        """Test mixed condiments."""
        espresso = Espresso()
        espresso.set_size(Size.TALL)

        # Add Soy, Mocha, and Whip
        mixed_espresso = Whip(Mocha(Soy(espresso)))

        expected_cost = (
            Decimal("1.99") + Decimal("0.10") + Decimal("0.20") + Decimal("0.10")
        )  # Espresso + Soy + Mocha + Whip (all TALL)
        assert mixed_espresso.cost() == expected_cost
        assert "Soja" in mixed_espresso.get_description()
        assert "Mocha" in mixed_espresso.get_description()
        assert "Crema" in mixed_espresso.get_description()


class TestSizeBasedPricing:
    """Test size-based pricing for condiments (Nivel 2)."""

    def test_soy_different_sizes(self):
        """Test Soy pricing across different sizes."""
        # Test TALL
        house_blend_tall = HouseBlend()
        house_blend_tall.set_size(Size.TALL)
        soy_tall = Soy(house_blend_tall)
        expected_tall = Decimal("0.89") + Decimal("0.10")
        assert soy_tall.cost() == expected_tall

        # Test GRANDE
        house_blend_grande = HouseBlend()
        house_blend_grande.set_size(Size.GRANDE)
        soy_grande = Soy(house_blend_grande)
        expected_grande = Decimal("0.89") + Decimal("0.15")
        assert soy_grande.cost() == expected_grande

        # Test VENTI
        house_blend_venti = HouseBlend()
        house_blend_venti.set_size(Size.VENTI)
        soy_venti = Soy(house_blend_venti)
        expected_venti = Decimal("0.89") + Decimal("0.20")
        assert soy_venti.cost() == expected_venti

    def test_size_propagation(self):
        """Test that size changes propagate through decorators."""
        espresso = Espresso()
        decorated = Soy(Mocha(espresso))

        # Change size and verify it propagates
        decorated.set_size(Size.VENTI)
        assert espresso.get_size() == Size.VENTI
        assert decorated.get_size() == Size.VENTI

        # Verify cost reflects the new size
        expected_cost = (
            Decimal("1.99") + Decimal("0.30") + Decimal("0.20")
        )  # Espresso + Mocha VENTI + Soy VENTI
        assert decorated.cost() == expected_cost


class TestBuilderPattern:
    """Test the builder pattern functionality (Nivel 3)."""

    def test_simple_build(self):
        """Test simple beverage building."""
        beverage = build_beverage("espresso")
        # Note: build_beverage wraps with PrettyDescriptionDecorator
        assert beverage.cost() == Decimal("1.99")
        assert "Espresso" in beverage.get_description()

    def test_build_with_condiments(self):
        """Test building with condiments."""
        beverage = build_beverage("houseblend", "tall", ["soy", "mocha"])
        expected_cost = (
            Decimal("0.89") + Decimal("0.10") + Decimal("0.20")
        )  # HouseBlend + Soy TALL + Mocha TALL
        assert beverage.cost() == expected_cost
        assert "Café de la Casa" in beverage.get_description()
        assert "Soja" in beverage.get_description()
        assert "Mocha" in beverage.get_description()

    def test_build_with_size(self):
        """Test building with different sizes."""
        beverage = build_beverage("darkroast", "venti", ["soy"])
        expected_cost = Decimal("0.99") + Decimal("0.20")  # DarkRoast + Soy VENTI
        assert beverage.cost() == expected_cost
        assert beverage.get_size() == Size.VENTI


class TestPrettyDescriptionDecorator:
    """Test the pretty description functionality (Nivel 3)."""

    def test_double_grouping(self):
        """Test that double condiments are grouped properly."""
        espresso = Espresso()
        double_mocha = Mocha(Mocha(espresso))
        pretty = PrettyDescriptionDecorator(double_mocha)

        description = pretty.get_description()
        assert "Double Mocha" in description
        assert (
            description.count("Mocha") == 1
        )  # Should only appear once as "Double Mocha"

    def test_triple_grouping(self):
        """Test that triple condiments are grouped properly."""
        house_blend = HouseBlend()
        triple_caramel = Caramel(Caramel(Caramel(house_blend)))
        pretty = PrettyDescriptionDecorator(triple_caramel)

        description = pretty.get_description()
        assert "Triple Caramel" in description

    def test_cost_unchanged_by_pretty_decorator(self):
        """Test that PrettyDescriptionDecorator doesn't change cost."""
        espresso = Espresso()
        mocha_espresso = Mocha(espresso)
        pretty_mocha = PrettyDescriptionDecorator(mocha_espresso)

        assert pretty_mocha.cost() == mocha_espresso.cost()


class TestComplexCombinations:
    """Test complex real-world combinations (comprehensive scenarios)."""

    def test_complex_scenario_1(self):
        """Test: Espresso VENTI with Soy and Mocha."""
        beverage = build_beverage("espresso", "venti", ["soy", "mocha"])
        expected_cost = (
            Decimal("1.99") + Decimal("0.20") + Decimal("0.30")
        )  # Espresso + Soy VENTI + Mocha VENTI
        assert beverage.cost() == expected_cost
        assert beverage.get_size() == Size.VENTI
        assert "Espresso" in beverage.get_description()
        assert "Soja" in beverage.get_description()
        assert "Mocha" in beverage.get_description()

    def test_complex_scenario_2(self):
        """Test: DarkRoast GRANDE with Soy, Caramel, and Whip."""
        beverage = build_beverage("darkroast", "grande", ["soy", "caramel", "whip"])
        expected_cost = (
            Decimal("0.99") + Decimal("0.15") + Decimal("0.25") + Decimal("0.15")
        )  # DarkRoast + Soy GRANDE + Caramel GRANDE + Whip GRANDE
        assert beverage.cost() == expected_cost
        assert beverage.get_size() == Size.GRANDE

    def test_complex_scenario_3(self):
        """Test: HouseBlend TALL with double Soy (size propagation test)."""
        beverage = build_beverage("houseblend", "tall", ["soy", "soy"])
        expected_cost = (
            Decimal("0.89") + Decimal("0.10") + Decimal("0.10")
        )  # HouseBlend + 2x Soy TALL
        assert beverage.cost() == expected_cost
        assert beverage.get_size() == Size.TALL
        # With PrettyDescriptionDecorator, should show "Double Soja"
        assert "Double Soja" in beverage.get_description()

    def test_complex_scenario_4(self):
        """Test: All condiments on one beverage."""
        beverage = build_beverage(
            "decaf", "grande", ["milk", "mocha", "soy", "whip", "caramel"]
        )
        # Decaf + Milk GRANDE + Mocha GRANDE + Soy GRANDE + Whip GRANDE + Caramel GRANDE
        expected_cost = (
            Decimal("1.05")
            + Decimal("0.15")
            + Decimal("0.25")
            + Decimal("0.15")
            + Decimal("0.15")
            + Decimal("0.25")
        )
        assert beverage.cost() == expected_cost

        description = beverage.get_description()
        assert "Café Descafeinado" in description
        assert "Leche" in description
        assert "Mocha" in description
        assert "Soja" in description
        assert "Crema" in description
        assert "Caramelo" in description

    def test_complex_scenario_5(self):
        """Test: Multiple doubles and triples mixed."""
        # This tests the most complex scenario: multiple repeated condiments
        espresso = Espresso()
        espresso.set_size(Size.TALL)

        # Add: 2x Mocha, 3x Caramel, 1x Whip
        complex_beverage = Whip(Caramel(Caramel(Caramel(Mocha(Mocha(espresso))))))

        expected_cost = (
            Decimal("1.99")
            + 2 * Decimal("0.20")
            + 3 * Decimal("0.20")
            + Decimal("0.10")
        )  # Espresso + 2xMocha + 3xCaramel + Whip (all TALL)
        assert complex_beverage.cost() == expected_cost

        # Test with PrettyDescriptionDecorator
        pretty_complex = PrettyDescriptionDecorator(complex_beverage)
        description = pretty_complex.get_description()
        assert "Double Mocha" in description
        assert "Triple Caramel" in description
        assert "Crema" in description


class TestErrorHandling:
    """Test error handling in builder pattern."""

    def test_invalid_base_beverage(self):
        """Test that invalid base beverage raises error."""
        with pytest.raises(ValueError, match="Bebida base desconocida"):
            build_beverage("invalid_beverage")

    def test_invalid_condiment(self):
        """Test that invalid condiment raises error."""
        with pytest.raises(ValueError, match="Condimento desconocido"):
            build_beverage("espresso", "tall", ["invalid_condiment"])


if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])
