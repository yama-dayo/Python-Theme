class  NumberingGame:

    def action(self):
        # インポート
        import random
        try:
            ans = random.randint(1, 100)
            max_count = 10
            print('1~100の数字の中から一つ選んだよ。')
            print('その数字を', max_count, '回以内に当ててね。')
            
            # Forでループ処理
            for i in range(1, max_count + 1):
                print(i, '回目、いくつかな?')
                num = int(input())
                if num == ans:
                    print('当たり!!')
                    break
                elif i == max_count:
                    pass
                elif num > ans:
                    print('もっと下だよ')
                else:
                    print('もっと上だよ')
            else:
                print('正解は',ans,'でした^^')
        # 例外処理
        except ValueError:
            print('正しい値を入力してください')
