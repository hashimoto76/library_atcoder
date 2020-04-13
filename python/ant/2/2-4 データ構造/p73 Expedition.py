"""
Expedition(プライオリティーキューを用いる問題)
はじめガソリンPが入っているトラックで、途中にあるガソリンスタンドで補給しながら
距離Lを走り切れるか？走り切れるなら補給回数を最小にしてそれを出力せよ。
（走り切れないなら-1を出力）

条件
L:トラックで走る距離
P:はじめトラックに入っているガソリンの量
N:途中にあるガソリンスタンドの個数
A[i]:スタート地点からのi+1番目のガソリンスタンドの場所
B[i]:i+1番目のガソリンスタンドで補給できるガソリンの限界量
また、このトラックは距離1走るとガソリンを1消費する。
さらにこのトラックの燃料タンクの容量は無限大である。(つよい)

!!制約!!
1<=n<=10000
1<=L<=1000000,1<=P<=1000000
1<=A[i]<=L,1<=B[i]<=100

入力形式
入力は以下の形式で標準入力から与えられる。(Atcoder感)
N L P
A[0] ... A[n-1]
B[0] ... B[n-1]
"""
#-------------------------------------------------------------------------------
import heapq #プライオリティーキューのインポート 
#入力,準備
N,L,P=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

#ゴールを "補給できないガソリンスタンド" としてリストA,Bに追加
A.append(L)
B.append(0)

#メイン
ans=0 #補給回数
pos=0 #今いる場所
tank=P #トラックの補給タンクに入っているガソリンの量

for k in range(N):
    B[k]-=2*B[k]

x=[]
heapq.heapify(x)#プライオリティーキューの準備 (最初は何も入っていないことに注意)

for j in range(N+1):
    d=A[j]-pos
    while tank-d<0: #入っている燃料だけでは足りない場合にのみwhileループ
        if len(x)==0: #もう使えるガソリンスタンドが存在しない場合
            print(-1)
            exit()
        else: #まだ使えるガソリンスタンドが存在する場合
            tank+=heapq.heappop(x)*(-1) #通り過ぎたガソリンスタンドのうち補給できる限界量が最も大きいものを補給
            ans+=1
            #注意:heapq.heappopはheapqの中で最小値を取り出しそれを取り除く(再利用不可)
    tank-=d
    pos=A[j]
    if ans!=-1: #一回でもans=-1が出力されたらずっとans=-1を保っていてほしい
        heapq.heappush(x,B[j]) #到達したガソリンスタンドは足りなくなった場合に使えるようにする(ans=-1の場合を除く)
    
print(ans)#出力
"""
実際にはガソリンの補給はガソリンスタンドの場所でしかできないが、
あくまで自分に起こっているリアルな問題ではない(計画的な問題)ので、
A[i]にあるガソリンスタンドに到達したときに、今後いつでも一度だけB[i]補給できると考えてもよい。
すなわち、途中で燃料が無くなった時に実は前に通ったガソリンスタンドのうち最も多く補給できる
ガソリンスタンドで補給していたとできる。(最大をとる理由はなるべくansを小さくしたいから)
このような操作をすればansが最小になるような気がするよなぁ！？(証明？しらん)
​
計算量はO(n)に毛が生えた程度(だと思う)
​
"""
