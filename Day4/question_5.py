class Poly:
    def __init__(self, *cof):
        self.cof = list(cof)

    def __add__(self, b):
        max_len = max(len(self.cof), len(b.cof))
        self.cof = [0] * (max_len - len(self.cof)) + self.cof
        b.cof = [0] * (max_len - len(b.cof)) + b.cof
        final_result = [a + b for a, b in zip(self.cof, b.cof)]
        return Poly(*final_result)

    def __repr__(self):
        return f"Poly({', '.join(map(str, self.cof))})"
# if __name__ == "__main__':
#     a = Poly(1, 2, 3)
#     b = Poly(1, 0, 1, 1, 2, 3)
#     c = a + b
#     print(c)
