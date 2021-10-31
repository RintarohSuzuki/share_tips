from multiprocessing import Pool #1. インポート
 
def nijou(x): #引数1つ
   y = x*x
   print(y)
   return y

def kakezan(a, b): #引数2つ
   y = a*b
   print(y)
   return y

def ruijou(x):
   y1 = x**2
   y2 = x**3
   return y1, y2 #戻り値2つ
 
####### ラッパー ######
def wrapper_kakezan(args): #引数1つとして受け取って(p.mapに引数は1つだと思い込ませるため)
    return kakezan(*args) #実際にはリストとして展開して2つの引数を計算を実行する関数に渡す

def main():
   #3. CPUの設定から
   n = 4 #使うCPUの数
   p = Pool(n)

   #4-1: 引数1つで並列計算
   out1 = p.map(nijou, range(10)) #nijouに0,1,..のそれぞれを引数として与えて並列演算
   print(out1) #関数の戻り値も受け取れる

   #4-2: 引数2つで並列計算 *p.mapは引数1つの関数しか受け付けないので、間接的な関数(ラッパー)をかませて対処する
   #tutumimono = [[i, 3] for i in range(10)] #リストのリストを作る
   #out2 = p.map(wrapper_kakezan, tutumimono) #kakezanに[0, 3],[1, 3],..のそれぞれを引数として与えて並列演算
   #print(out2)

   #4-3: 戻り値2つを受け取る
   #out3 = p.map(ruijou, range(10))
   #print(out3)

   #cf. http://iatlex.com/python/parallel_first

if __name__ == "__main__": #2. このおまじないがないとうまく動かないらしい
   main()