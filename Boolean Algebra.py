OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
​
def boolean(x, y, operation):
​
    if operation=="conjunction":
    #"conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
        return x*y
​
    elif operation=="disjunction":
    #"disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
        return x or y
​
    elif operation=="implication":
    #"implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true.
        return not_(x)or y
​
    elif operation=="exclusive":
    #"exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y.
        return (x+y)%2
    elif operation=="equivalence":
    #"equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
        return not_(boolean(x,y,"exclusive"))
​
​
def not_(x):
    if x is 0 : return 1
    else: return 0
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"