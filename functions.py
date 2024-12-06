if __name__ == '__main__':
        pass


def several_zeros():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros



def matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]



class Matrix:
    def __init__(self, rows, cols): 
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def get_value(self, row, col):
        return self._matrix[row][col]
    
    def __eq__(self, other):

        if len(self._matrix) != len(other._matrix):
            return False
        
       
        if len(self._matrix[0]) != len(other._matrix[0]):
            return False
        
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[0])):
                if self._matrix[i][j] != other._matrix[i][j]:
                    return False
        
        return True
    



def my_sort(my_list: [int]) -> [int]:

    result = my_list.copy()
    
    n = len(result)
    
    for i in range(n):

        for j in range(0, n - i - 1):
           
            if result[j] > result[j + 1]:
                
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result

