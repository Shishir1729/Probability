"""TODO:    1) Normal Operations on Matrices and Vectors
            2) Multiplication of matrix with vectors and inner product
            3) Determinant of a matrix (Using Gaussian Elimination)
            4) Charaterestic equation?
            5) Eigen values and Eigen vectors
            6) Diagonalization
            7) Functions on Matrices
            8) Special techniques for matrices in probability and Sparse Matrices?
            9) Partial Pivoting and Scaled Partial Pivoting
            10) Inverse of a matrix """

#Need to figure if I really need to make a vector space or are just JEE stuff fine.
class Vector:
    pass

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        for i in range(self.rows):
            if len(matrix[i]) != self.columns:
                raise ValueError("The matrix is not rectangular")
    
    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("The matrices must have the same dimensions")
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])
    
    def scalar_multiply(self, scalar):
        return Matrix([[self.matrix[i][j] * scalar for j in range(self.columns)] for i in range(self.rows)])
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
            return Matrix([[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)]) for j in range(other.columns)] for i in range(self.rows)])
        else:
            return self.scalar_multiply(other)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def transpose(self):
        return Matrix([[self.matrix[j][i] for j in range(self.rows)] for i in range(self.columns)])
    
    def __eq__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __pow__(self, power):
        if self.rows != self.columns:
            raise ValueError("The matrix must be a square matrix")
        if power < 0:
            raise ValueError("The power must be non-negative")
        if isinstance(power, float):
            raise ValueError("The power must be an integer")
        if power == 0:
            return Matrix([[1 if i == j else 0 for j in range(self.columns)] for i in range(self.rows)])
        elif power == 1:
            return self
        else:
            if power % 2 == 0:
                return (self * self) ** (power // 2)
            else:
                return self * (self * self) ** (power // 2)
            
    def print(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.matrix[i][j], end = " ")
            print()
            
    
    #Implement Partial Pivoting and Scaled Partial Pivoting later
    def determinant(self):
        answer = 1
        mat = [[self.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        for i in range(self.rows):
            if mat[i][i] == 0:
                for j in range(i + 1, self.rows):
                    if mat[j][i] != 0:
                        mat[i], mat[j] = mat[j], mat[i]
                        answer *= -1
                        break
                else:
                    return 0
            for j in range(i + 1, self.rows):
                factor = mat[j][i] / mat[i][i]
                for k in range(self.columns):
                    mat[j][k] -= factor * mat[i][k]
        for i in range(self.rows):
            answer *= mat[i][i]
        return answer
    
    #TODO
    def inverse(self):
        pass
    
