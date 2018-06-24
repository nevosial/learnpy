'''
Newton formula to estimate square root of a number.
Formula: newguess=1/2∗(oldguess+n/oldguess)
'''

def newton_sqrt(n):
    root = n/2    #initial guess will be half of n.

    #make 20 guesses
    for i in range(20):
        root = (1/2)*(root + (n/root))
        print(root)
    return root

nroot = newton_sqrt(743)
print(nroot)
