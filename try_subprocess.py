import subprocess as sp #1. インポート (略称spはあまり一般的ではありません)

def main():
   #2-1: 一番簡単な例 lsを実行
   sp.run('ls')

   #2-2: 引数を持たせる場合
   #sp.run(['ls', 'hoge'])

   #2-3: 自作コードの場合
   #com = './hoge.bash'
   #sp.run(com, shell=True) #shell=Trueとするとシェルのコマンドをそのまま受け付けてくれるので動く
   #ただし、外部からアクセスできるようなサイトのコーディングでは非推奨(コマンドインジェクションの可能性があるため)

   #2-4: 標準出力、標準エラー出力を受けたい場合
   #com = 'ls | wc -l'
   #proc = sp.run(com, shell=True, stdout = sp.PIPE, stderr = sp.STDOUT)
   #out = proc.stdout.decode("utf8")
   #print(out) #この書き方だとエラーもくっついて出てくる
   #2-1~2-3では勝手に標準出力が出てきたが、2-4では変数で受けないと出力できない
   #どのコマンドが標準出力、標準エラー出力を勝手に吐き出すかは不明

   #cf.
   # https://tech.mobilefactory.jp/entry/2018/12/27/150000
   # https://www.shadan-kun.com/blog/measure/2873/
   # https://dev.classmethod.jp/articles/python-subprocess-shell-command/

if __name__ == '__main__':
   main()