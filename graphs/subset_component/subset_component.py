#!python3

import sys, os
#import cProfile, pstats, io, pdb

def connected_components(ds):
    ret = 64
    for i in range(len(ds)):
        if ds[i][1] == i:
            ret -= ones(ds[i][2])-1
    return ret

def ones(n):
    ons = 0
    while n > 0:
        ons += n & 1
        n = n >> 1
    return ons


# receives next clique to add and a disjointSet data structure
def findcc(newClique, ds):
#    print(newClique)
    
    # Update disjoint set
    sons = []
    n = ds[newClique][0]
    for parent in range(len(ds)):
        if ds[parent][1] != parent or ds[parent][1] == -1:
            continue
        component = ds[parent][2]
        if n+component != n ^ component:
            ds[parent][1] = newClique
            ds[newClique][2] |= ds[parent][2]
            sons.append(parent)
    ds[newClique][1] = newClique

    # Compute number of connected components
    cc = connected_components(ds)

    nextClique = 0
    while nextClique < newClique:
        cc += findcc(nextClique, ds)
        nextClique += 1

    # Undo disjoint set changes
    ds[newClique][1] = -1
    ds[newClique][2] = ds[newClique][0]
    for s in sons:
        ds[s][1] = s

    return cc


# Special case for the first recursion step
def firstIteration(ds):
    cc = 64 #This is for the case where no numbers are selected (each node is its own set)
    nextClique = 0
    while nextClique < len(ds):
        cc += findcc(nextClique, ds)
        nextClique += 1
    return cc
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    d_count = int(input())
    ds = list(map((lambda a: [int(a), -1, int(a)]), input().rstrip().split()))

    # f = open(sys.argv[1], 'r')
    # case = f.readlines()
    # ds = list(map((lambda a: [int(a), -1, int(a)]), case[1].rstrip().split()))
    # f.close()
    
    #pr = cProfile.Profile()
    #pr.enable()
    #pdb.set_trace()
    components = firstIteration(ds)
    #pr.disable()
    #s = io.StringIO()
    #sortby = 'cumulative'
    #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    #ps.print_stats()
    #print(s.getvalue())
    #print(components)

    fptr.write(str(components) + '\n')
    fptr.close()
