import argparse #1. インポート

def read_args():
   parser = argparse.ArgumentParser() # 2. perserという引数を納める箱を作る

   #3. どんな引数を受け取るかの設定(1行＝1つの引数)
   parser.add_argument('--list') #一番シンプルな形

   parser.add_argument('--in_dir', required=True) #絶対指定してね

   parser.add_argument('--mode', choices=['train', 'test', 'cont', 'seq'], required=True) #リストのどれかしか受け付けない

   parser.add_argument('--chtbl', default='etc/ch_merge.dat') #指定しなくても勝手にデフォルト値が入る

   parser.add_argument('--filter', action='store_true') #引数無しでオプションを付けたらTrueを返す

   parser.add_argument('--rottbl', default='etc/ch_rot.dat', help='rotation table') #helpも設定できる、-hか--helpで出力
   
   parser.add_argument('--overlap', type=int, default=0) #読み込み時の型(フォーマット)を指定

   tp1 = lambda x:list(map(str, x.split('-'))) #型は自分でも作れる
   parser.add_argument('--term', type=tp1, default=['20210910', '20210911'], help='format: yymmdd-yymmdd term for conversion')

   args = parser.parse_args() # 4.ここまでで設定した通りに引数を受け取る

   #cf. https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0

   return args

def main(args):
   print(args)
   #print(args.list) #指定した引数を取り出したい場合

   #args.add = 'hoge' #後から追加もできる
   #print(args)

   #args.list = 'hoge2.txt' #更新もできる
   #print(args.list)

if __name__ == '__main__':
   args = read_args()
   main(args)