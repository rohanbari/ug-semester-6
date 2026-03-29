A = {num for num in range(1, 51) if num % 2 == 0}
B = {num * num for num in range(1, 8) if num * num < 50}

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_a_b = A.difference(B)
difference_b_a = B.difference(A)

print("Set A (even numbers from 1 to 50):", sorted(A))
print("Set B (perfect squares less than 50):", sorted(B))

print("\na. Union of sets (A U B):", sorted(union_set))
print("b. Intersection of sets (A n B):", sorted(intersection_set))
print("c. Difference of sets (A - B):", sorted(difference_a_b))
print("d. Difference of sets (B - A):", sorted(difference_b_a))
