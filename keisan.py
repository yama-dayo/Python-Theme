class KeisanPlay:
    # 関数を指定
    def action(self):
        num1 = int(input('数字を入力してね'))        #2つの変数を変えることで結果も変わる！
        num2 = int(input('数字を入力してね'))
        n = input('+, -, *, / の中から選んでね！ ：')

        # 四則演算を実行
        try:
            if n == '+':
                print((num1 + num2),'だよ')

            elif n == '-':
                print((num1 - num2),'だよ')

            elif n == '*':
                print((num1 * num2),'だよ')

            elif n == ('/'):
                print(int(num1 / num2),'だよ')
                
        # ゼロによる除算をした時
        except ZeroDivisionError:
            print('ゼロによる除算です')

        