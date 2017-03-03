import sys

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


# Q1


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

sys.stdout.write(BLUE)
print("Q1: Suppose we roll a red die and a green die\n")

# (i)
print("(i) What is the sample space for this experiment?")
sys.stdout.write(RESET)
outcomes = [1, 2, 3, 4, 5, 6]
s = ""
for i in outcomes:
    for j in outcomes:
        s += str("{{{i:0},{j:0}}} ".format(i=i, j=j))
    print(s)
    s = ""

sys.stdout.write(BLUE)
# (ii)
print("\n(ii) What is the probability that the number on the green die is larger than the number "
      "on the red die?")
sys.stdout.write(RESET)
count = 0
for i in outcomes:
    for j in outcomes:
        if i > j:
            count += 1
common_divisor = gcd(count, len(outcomes) ** 2)
(reduced_num, reduced_den) = (count / common_divisor, len(outcomes) ** 2 / common_divisor)
print("{0:g}/{1:g}".format(reduced_num, reduced_den))

sys.stdout.write(BLUE)
# (iii)
print("\n(iii)Define what it means for two events E and F to be independent.")
sys.stdout.write(RESET)
print("Two events E and F are independent if the order in which they occur doesn't matter. "
      "Alternatively, if observing one doesn't affect the other.")
print("P(E ∩ F) = P(E)P(F)")

sys.stdout.write(BLUE)
# (iv)
print("\n(iv) Let event E be that the sum of the dice equals 2 or 3 and event F be that"
      " the sum equals 3. Are E and F independent? Explain with reference to the "
      "definition given above")
sys.stdout.write(RESET)
print("No, E and F are not independent. Observing E affects the outcome of F. Using the mathematical definition "
      "P(E ∩ F) = P(E)P(F):")
print("P(E ∩ F) = 1/36, P(E)P(F) = 1/12 * 1/18 = 1/216")
print("Thus, E and F are dependent as P(E ∩ F) != P(E)P(F)")
