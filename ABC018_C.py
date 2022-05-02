import io
import sys

_INPUT = """\
6
4 5 2
xoooo
oooox
ooooo
oxxoo
4 5 2
ooooo
oxoox
oooox
oxxoo
8 6 3
oooooo
oooooo
oooooo
oooooo
oxoooo
oooooo
oooooo
oooooo
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  R,C,K=map(int,input().split())
  S=[input() for _ in range(R)]
  AS=[[-1]*4 for _ in range(R*C)]
  if R<2*K-1 or C<2*K-1: print(0)
  else:
    for i in range(R):
      for j in range(C):
        if i>=K-1 and j>=K-1:
          if i==K-1 or j==K-1:
            AS[i*C+j][0]=sum([1 if S[i-k][j-k]=='o' else 0 for k in range(K)])
          else:
            AS[i*C+j][0]=AS[(i-1)*C+j-1][0]-(1 if S[i-K][j-K]=='o' else 0)+(1 if S[i][j]=='o' else 0)
    for i in range(R):
      for j in reversed(range(C)):
        if i>=K-1 and j<C-K+1:
          if i==K-1 or j==C-K:
            AS[i*C+j][1]=sum([1 if S[i-k][j+k]=='o' else 0 for k in range(K)])
          else:
            AS[i*C+j][1]=AS[(i-1)*C+j+1][1]-(1 if S[i-K][j+K]=='o' else 0)+(1 if S[i][j]=='o' else 0)
    for i in reversed(range(R)):
      for j in reversed(range(C)):
        if i<R-K+1 and j<C-K+1:
          if i==R-K or j==C-K:
            AS[i*C+j][2]=sum([1 if S[i+k][j+k]=='o' else 0 for k in range(K)])
          else:
            AS[i*C+j][2]=AS[(i+1)*C+j+1][2]-(1 if S[i+K][j+K]=='o' else 0)+(1 if S[i][j]=='o' else 0)
    for i in reversed(range(R)):
      for j in range(C):
        if i<R-K+1 and j>=K-1:
          if i==R-K or j==K-1:
            AS[i*C+j][3]=sum([1 if S[i+k][j-k]=='o' else 0 for k in range(K)])
          else:
            AS[i*C+j][3]=AS[(i+1)*C+j-1][3]-(1 if S[i+K][j-K]=='o' else 0)+(1 if S[i][j]=='o' else 0)
    ans=[[-1]*C for _ in range(R)]
    for i in range(K-1,R-K+1):
      for j in range(K-1,C-K+1):
        if i==K-1 and j==K-1:
          ans[i][j]=sum([1 if S[k][l]=='o' else 0 for k in range(i-K+1,i+K) for l in range(j-K+1,j+K) if abs(i-k)+abs(j-l)<K])
        else:
          if i>=K:
            ans[i][j]=ans[i-1][j]+AS[(i+K-1)*C+j][0]+AS[(i+K-1)*C+j][1]-AS[(i-K)*C+j][2]-AS[(i-K)*C+j][3]-(1 if S[i+K-1][j]=='o' else 0)+(1 if S[i-K][j]=='o' else 0)
          else:
            ans[i][j]=ans[i][j-1]+AS[i*C+j+K-1][0]+AS[i*C+j+K-1][3]-AS[i*C+j-K][1]-AS[i*C+j-K][2]-(1 if S[i][j+K-1]=='o' else 0)+(1 if S[i][j-K]=='o' else 0)
    tmp=0
    for i in range(R):
      for j in range(C):
        if ans[i][j]==2*K**2-2*K+1: tmp+=1
    print(tmp)