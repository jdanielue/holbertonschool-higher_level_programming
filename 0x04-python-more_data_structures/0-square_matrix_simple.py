#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        matrizala2 = []
        for row in matrix:
                dato = []
                for col in row:
                        dato.append(col ** 2)
                matrizala2.append(dato)
        return matrizala2
