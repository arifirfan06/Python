import utility # just the name .py not needed because everything in import is py files
# print(utility) # __pycache__ created when we running code in import, dont modify it. pychache keep track change in modules so we always use updated module changes
import cart.cart_main as cart

print(utility.divide(4,2))
print(cart.buy('Milks'))

