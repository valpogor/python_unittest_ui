import math as _math
import mpmath
list=[3,12,14,17,41, 50]
def golden_ratio(n):
    a = 1
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return b / a

# Usage example
iterations = 10
result = golden_ratio(iterations)
# print(f"The golden ratio after {iterations} iterations is approximately: {result}")

# pi = 4 * _math.atan(1)
# print(pi)
# print(mpmath.mp.phi)
# golden = golden_ratio = (1 + _math.sqrt(5)) / 2
# print(golden)
def sum_float_numbers(float_value):
    total_sum = 0.0
    float_str = str(float_value)

    for char in float_str:
        if char.isdigit():
            total_sum += float(char)

    return total_sum

for i in list:
    result = sum_float_numbers(4 * _math.atan(i)*golden_ratio(i))
    result2 = sum_float_numbers(result)
    print(f"The numbers is: {result2}")

# for x in list:
#     result = sum_float_numbers(golden_ratio(x))
#     print(f"The numbers is: {result}")





    # Usage example
