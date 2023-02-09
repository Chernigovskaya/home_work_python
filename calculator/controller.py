import model
import view


def button_click():
    value_a = view.get_value()
    operator = view.get_operator()
    value_b = view.get_value()
    res = model.Calculator(value_a, value_b)
    if operator == "+":
        print(f"Result = {model.Calculator.sum(res)}")
    elif operator == "-":
        print(f"Result = {model.Calculator.difference(res)}")
    elif operator == "*":
        print(f"Result = {model.Calculator.multiplication(res)}")
    elif operator == "/":
        print(f"Result = {model.Calculator.division(res)}")
    else:
        print("оператор не найден ")

