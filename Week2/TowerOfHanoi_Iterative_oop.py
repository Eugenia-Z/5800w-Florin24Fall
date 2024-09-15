class Disks:
    def __init__ (self, n, src, trgt, aux):
        self.n  = n # number of disks to be moved
        self.src = src # source peg
        self.trgt = trgt # target peg
        self.aux = aux # Auxiliary peg
        
def iterative_Hanoi(n, src, trgt, aux):
    L = [] # Stack to store disk movement states
    L.append(Disks(n, src, trgt, aux))
    
    while L:
        curr = L.pop()
        if curr.n == 1:
            print(f"Move disk from {curr.src} to {curr.trgt}")
        else:
            # Push subproblems onto stack in REVERSE order
            L.append(Disks(curr.n - 1, curr.aux, curr.trgt, curr.src))
            L.append(Disks(1, curr.src, curr.trgt, curr.aux))
            L.append(Disks(curr.n-1, curr.src, curr.aux, curr.trgt))
            
if __name__ == "__main__":
    n = 3
    source = "1"
    target = "2"
    aux = "3"
    iterative_Hanoi(n, source, target, aux)
    
    