from app import render


def test_render_contains_payment():
    assert "215.07" in render("1000000", "10", "10")


def test_render_custom_values():
    assert "Ежемесячный платёж" in render("500000", "12", "5")


def test_render_invalid_values():
    assert "Ошибка" in render("abc", "10", "10")
