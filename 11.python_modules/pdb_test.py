import pdb
# python debugger

def multi(n1,n2):
    pdb.set_trace() # set_trace can check params in terminal, you can type help in pdb terminal
    # you can use pdb step in terminal
    tnum = 2*11
    return n1 * n2

print(multi(1, '22'))