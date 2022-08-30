#* Prime Numbers

Given a number $N$, find all the prime numbers smaller than $N$, where $N$ is an integer $< 10^6$.

**Solution**

Using sieves of erastothenes, the prime numbers smaller than $N$ can be found:

```python
def sieves_of_erastothenes(N: int) -> list[int]:
    """Finds the prime numbers from range N

    Args:
        N -- the upper limit

    Returns:
        The list of primes smaller than N.
    """

    not_primes: list[int] = [True]*N
    for i in range(2, N):
        if not_primes[i]:
            for j in range(i, N, i):
                not_primes[j] = False

    return [x for x in range(N) if not_primes[x]]
```

Sieves of erastothenes can also be implemented in C:

```c
#include <stdio.h>
#include <stdlib.h>

#define ARR_LIMIT 10000000

int main(){
    unsigned long long int i,j;
    int *primes;
    int z = 1;

    primes = malloc(sizeof(int)*LIMIT);

    for (i=2;i<limit;i++) {
        primes[i]=1;
    }

    for (i=2;i<limit;i++) {
        if (primes[i]) {
            for (j=i;i*j<limit;j++) {
                primes[i*j]=0;
            }
        }
    }

    for (i=2;i<limit;i++) {
        if (primes[i]) {
            printf("%dth prime = %dn",z++,i);
        }
    }

    return 0;
}
```
