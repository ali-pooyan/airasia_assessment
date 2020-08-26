import pandas as pd
import itertools
from itertools import permutations


def Ways(N):
    a = list(itertools.product([1, 2], repeat=N - 1))
    df = pd.DataFrame(a)
    df["sum"] = df.sum(axis=1)
    new = df.loc[df['sum'] == N - 1]
    return len(new)
def findJumpingWays(N):
    count = 0
    for i in range(1,N):
        Ways(i)
        count= count + Ways(i)
    return count

findJumpingWays(3)