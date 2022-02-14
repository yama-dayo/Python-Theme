# 戦いBOT、計算BOT、数当てゲームをインポート
import tatakai,kazuate, keisan

# おしゃべり用の辞書データ
bot_dict = {'ありがとう':'ドウイタシマシテ',
            'おはよう':'オハヨウゴザイマス',
            'げんき？':'ワタシハトテモゲンキデス',
            'こんにちは':'コンニチハ'}
# 数当てゲームのインスタンスを生成
number = kazuate.NumberingGame()

# 計算BOTのインスタンスを生成
keisan = keisan.KeisanPlay()

# 戦いBOTのインスタンスを生成
tatakai = tatakai.Fight()

while True:
    try:
        print('何をしますか？')
        print('0: 会話BOT')
        print('1: 戦う')
        print('2: 数当てゲーム')
        print('3: 計算する')
        print('9: 終了する')

        act = int(input('整数で番号を入力:'))

        if act == 0:
            command = input('話しかける→')
            
            responce = ""
            
            #辞書のキーが含まれているかチェック
            for key in bot_dict:
                if key in command:
                    responce = bot_dict[key]
                    break
                
            
            # 空文字の判定
            if not responce:
                responce = 'ヨクワカリマセン'
            
            print(responce)
            
            if 'ばいばい' in command:
                break

        elif act == 1:
            tatakai.FightPlay()

        elif act == 2:
            number.action()

        elif act == 3:
            keisan.action()

        elif act == 9:
            print('また来てね！')
            break  
          
    except ValueError:
        print('数字を入力してください')