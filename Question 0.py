def concise_is_negative(num):
    return True if bool(num) else False

print(concise_is_negative(0))
print(concise_is_negative(1))
print(concise_is_negative(-1))