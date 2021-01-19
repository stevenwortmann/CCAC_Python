# 'NumPy' package allows linear algebra solution of arrays
import numpy

# 'a' is made up of chicken/rabbit heads [1,1] and chicken/rabbit legs [2,4]
# 'b' is made up of chicken/rabbit totals [70,188] = [heads,legs]
a = numpy.array([[1,1],[2,4]])
b = numpy.array([70,188])

# Assuming 'x' for chickens and 'y' for rabbits
# 'linalg' solves both variables for the following linear equations:
# x + y = 70      2x + 4y = 188
solution = numpy.linalg.solve(a,b)

# Index values 0, 1 stored as integer values 46 (chickens) and 24 (rabbits)
chickens = int(solution[0])
rabbits = int(solution[1])

# Solution is printed, with variables inserted to prove linear algebra
print("\n\n\n")
print("You count 70 heads and 188 legs among the chickens and rabbits on" \
      " a farm. \nHow many rabbits and how many chickens do you have?")
print("\n")
print("Chickens have 2 legs, while rabbits have 4 legs. " \
      "Both have only one head.")
print("\n")
print("Thus, with  70  heads and  188  legs, we can account for... \n\n", \
      chickens, "chickens and ", rabbits, "rabbits!\n\n\n")