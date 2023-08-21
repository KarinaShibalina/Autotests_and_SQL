# Карина Шибалина, 7-я когорта — Финальный проект. Инженер по тестированию плюс
import create_order


def test_create_order():
    create_order.get_order()
    status_code = create_order.get_order().status_code
    exp = 200
    assert status_code == exp


test_create_order()
