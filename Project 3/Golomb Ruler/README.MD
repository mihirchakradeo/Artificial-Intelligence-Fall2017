# AI Project 3 Report

**Algorithm**

```
▫ Backtracking:
```
```
Algorithm BT (L, M)
```
1. Call BTHelper(L, M, res, ruler, curr)
2. If true returned, store result in temp
3. Else return solution as is
4. L --
5. If L >= M, goto 1
6. Return temp

```
Algorithm BTHelper (L, M, res, ruler, curr)
```
1. If constraint satisfied goto 3
2. Else return False, []
3. M--
4. If M > 0, goto 6
5. Else return True,ruler
6. I = 0
7. If curr+1<I<L, goto to 9
8. Else goto 12
9. Call BTHelper(L, M, res, ruler, i)
10. If True returned, return True,ruler
11. Else I++, goto 7
12. If result found, return True,result
13. Else return False,[]

```
▫ Backtracking + Forward Checking
```
```
Algorithm FC (L, M)
```
1. Call FCHelper(L, M, res, ruler, curr)
2. If true returned, store result in temp
3. Else return solution as is
4. L --
5. If L >= M, goto 1
6. Return temp
Algorithm FCHelper (L, M, res, ruler, curr, domain)
1. Call constraintConsistent (domain, ruler, curr)
2. If step 1 returns True, goto 4


3. Else, return False,[]
4. Place marker
5. If constraint satisfied goto 7
6. Else return False, []
7. M--
8. If M > 0, goto 10
9. Else return True,ruler
10. I = 0
11. If curr+1<I<L, goto to 13
12. Else goto 12
13. Call FCHelper(L, M, res, ruler, i)
14. If True returned, return True,ruler
15. Else I++, goto 11
16. If result found, return True,result
17. Else return False,[]

## Statistics

**1. Number of consistency checks**

```
L, M BT FC
3, 3 2 2
```
```
6, 4 16 11
11, 5 93 43
17, 6 734 253
25 ,7 7166 1972
44, 9 597487 117333
```
**2. Time taken to execute**

```
L, M BT FC
3, 3 0.0000700950622559 0.
6, 4 0.000267028808594 0.
11, 5 0.00202512741089 0.
17, 6 0.00937604904175 0.
25, 7 0.0762989521027 0.
44, 9 10.4548079967 6.
```
The number of consistency checks performed is same for the L =3 and M = 3. But there is a steep
increase in case of Back tracking as the input size becomes large

After L = 72, M = 11, the program takes a long time



