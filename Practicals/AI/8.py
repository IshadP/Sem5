# 

import numpy as np

class FuzzySet:
    def __init__(self, name, membership_function):
        self.name = name
        self.membership_function = membership_function

    @staticmethod
    def triangular_membership(a, b, c):
        """Creates a triangular membership function."""
        return lambda x: max(0, min((x - a) / (b - a), (c - x) / (c - b)))

    def membership(self, x):
        """Returns the membership value of x."""
        return self.membership_function(x)

    @staticmethod
    def union(A, B):
        """Returns the union of two fuzzy sets."""
        return lambda x: max(A.membership(x), B.membership(x))

    @staticmethod
    def intersection(A, B):
        """Returns the intersection of two fuzzy sets."""
        return lambda x: min(A.membership(x), B.membership(x))

    @staticmethod
    def complement(A):
        """Returns the complement of a fuzzy set."""
        return lambda x: 1 - A.membership(x)

if __name__ == "__main__":
    A = FuzzySet("A", FuzzySet.triangular_membership(0, 5, 10))
    B = FuzzySet("B", FuzzySet.triangular_membership(5, 10, 15))

    x = 7
    print(f"Membership of: {A.membership(x)}")
    print(f"Membership of {B.membership(x)}")
    
    union_set = FuzzySet.union(A, B)
    intersection_set = FuzzySet.intersection(A, B)
    complement_set_A = FuzzySet.complement(A)

    print(f"Union membership: {union_set(x)}")
    print(f"Intersection membership: {intersection_set(x)}")
    print(f"Complement membership in A: {complement_set_A(x)}")
