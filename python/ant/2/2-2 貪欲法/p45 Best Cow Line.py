"""
n文字の文字列sが与えられ, n文字の文字列tを作る.
はじめはtは長さ0の文字列で, 次のいずれかの操作が行える.

  sの先頭を一文字削除し, tの末尾に追加する.
  sの末尾を一文字削除し, tの末尾に追加する.

辞書順比較でできるだけ小さくなるようにtを作れ.
 1<=n<=2000 文字列sに含まれるのはローマ字の大文字のみ.
 """
#-------------------------------------------------------------------------------

n=int(input())
s=input()
t=''
a=0
b=n-1
while a<=b:
    left=False
    for i in range(b-a+1):
        if s[a+i]<s[b-i]:
            left=True
            break
        elif s[a+i]>s[b-i]:
            break
    if left:
        t+=s[a]
        a+=1
    else:
        t+=s[b]
        b-=1
print(t)
