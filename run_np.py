import sys
import numpy as np

def numpy_add_backtrack(a,b):
    return a+b
    
if __name__ == "__main__":
    a = list(map(int,sys.argv[1].split(',')))
    b = list(map(int,sys.argv[2].split(',')))
    print(numpy_add_backtrack(np.array(a),np.array(b)))