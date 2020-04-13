"""
【分割数】
n個の互いに区別できない品物を,m個以下に分割する方法の総数を求め,
Mで割った余りを求めなさい
!!制約!!
1<=m<=n<=1000
2<=M<=10000
"""
#-------------------------------------------------------------------------------

#入力,準備

n= int(input())
m= int(input())
M= int(input())
dp=[[0 for i in range(n+1)] for j in range(m+1)]

#メイン
#dp[i][j]:=jのi以下分割の総数

dp[0][0]=1
for i in range(1,m+1):
    for j in range(n+1):
        if j-i>=0:
            dp[i][j]=(dp[i][j-i]+dp[i-1][j])%M
        else:
            dp[i][j]=dp[i-1][j]

#出力
print(dp[m][n])

"""
dp[i][j]はΣ[k=1~i](a_k)=jというのを考えるが,
もしすべてのkに対してa_k>=1なら
a'_k=(a_k)-1として, Σ[k=1~i](a'_k)=j-iつまりj-iのi以下分割数の総数になりdp[i][j-i]
そうでなくて,一個でもa_k=0となるものがあれば
それを除いたi-1個でjを分割することになるのでdp[i-1][j]


計算量はO(nm)

"""

