import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.

        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
def get_row(matrix, row):
    return matrix[row]

def get_column(matrix, column_number,rowcount):
    column = []
    for i in range(rowcount):
        column.append(matrix[i][column_number])
        
    return column

def dot_product(vector_one, vector_two):
    sum1=0
    for i in range(len(vector_one)):
        sum1 = sum1 +vector_one[i]*vector_two[i]
    return sum1

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        det1 =0
        if self.h==1:
            det1 =self[0][0]
        elif self.h==2 and self.w==2:
            det1 = (self.g[0][0]*self.g[1][1])-(self.g[0][1]*self.g[1][0])
        
        return det1

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        tracesum=0
        for i in range(self.h):
            for j in range(self.w):
                if i==j:
                    tracesum+= self.g[i][j]
        return tracesum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        invermetrics = []
        inverrow1=[]   
        inverrow2=[]  
        ## TODO: Check if matrix is larger than 2x2.
        ## If matrix is too large, then raise an error
        det1 =1/self.determinant()
        if self.h==1 and self.w==1:
            inverrow1.append(det1)
            invermetrics.append(inverrow1)

        elif self.h==2 and self.w==2:
             

            inverrow1.append(det1*self.g[1][1])
            inverrow1.append(-det1*self.g[0][1])
            inverrow2.append(-det1*self.g[1][0])
            inverrow2.append(det1*self.g[0][0])
            invermetrics.append(inverrow1)
            invermetrics.append(inverrow2)
            
        return Matrix(invermetrics)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        matrix_row=[]
        for i in range(self.w):
            for j in range(self.h):
                matrix_row.append(self.g[j][i])
            matrix_transpose.append(matrix_row)
            matrix_row=[]
       
        
    
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        add_row=[]
        add_met=[]
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be Addition if the dimensions are the same")
        for i in range(self.h):
            for j in range(self.w):
                add_row.append(self.g[i][j]+other.g[i][j])
            add_met.append(add_row)
            add_row=[]
            
        return Matrix(add_met)

        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg_row=[]
        neg_met=[]
        for i in range(self.h):
            for j in range(self.w):
                neg_row.append(-1*self.g[i][j])
            neg_met.append(neg_row)
            neg_row=[]
            
        return Matrix(neg_met)
            

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        sub_row=[]
        sub_met=[]
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
        for i in range(self.h):
            for j in range(self.w):
                sub_row.append(self.g[i][j]-other.g[i][j])
            sub_met.append(sub_row)
            sub_row=[]
            
        return Matrix(sub_met)

    def __mul__(self, other):
        m_rows = self.h
        p_columns=other.w
        p_row=other.h
        result=[]
        row1=[]
        col1=[]
        row_result = []
        for i in range(m_rows):
            row1=get_row(self.g,i)
            for j in range(p_columns):
                col1=get_column(other,j,other.h)
                row_result.append(dot_product(row1,col1))
            result.append(row_result)
            row_result=[]
                    
                
        
       
        """
        Defines the behavior of * operator (matrix multiplication)
        """
            
            
        return Matrix(result)
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            rmul_row=[]
            rmul_met=[]
            for i in range(self.h):
                for j in range(self.w):
                    rmul_row.append(other*self.g[i][j])
                rmul_met.append(rmul_row)
                rmul_row=[]
        
            
        return Matrix(rmul_met)