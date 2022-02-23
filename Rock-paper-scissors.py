# コンピュータの手をランダムにするために
import random
# 間を開けるために
import time

# じゃんけんの手を保持
hands = ['グー', 'チョキ', 'パー']
# コマンドリスト
command_list = [0, 1, 2, 3]

# じゃんけんの手と対応するコマンドを表示
print('0:' + hands[0] + ' 1:' + hands[1] +' 2:' + hands[2] + ' 3:ゲームを終わる')
print('「じゃんけん………」')

# ゲーム全体のループ
while True:
    # 正しく入力されたか判定。間違えていた場合入力に戻る
    while True:
        # 入力された内容を保持
        player_hand_num = int(input('あなたは何を出す？>>>\n'))

        # 入力がcommand_listの数字と対応していれば判定のループから抜ける
        if player_hand_num in command_list:
            break
        # 入力がcommand_listの数字と対応していなければ「間違えて入力しているよ」と表示
        else:
            print('間違えて入力しているよ')
    
    # 入力された内容が3ならゲームを終了する
    if player_hand_num == command_list[3]:
        print('ゲームを終了します')
        break

    # 入力された数字と対応する手を保持
    player_hand = hands[player_hand_num]

    # コンピュータの手の数字をランダムに決定して保持
    computer_hand_num = random.randrange(3)
    # コンピュータの手の数字と対応する手を保持
    computer_hand = hands[computer_hand_num]

    print('「ぽん」')
    # 1秒待つ
    time.sleep(1)

    # プレイヤーとコンピュータの手を表示
    print('あなたは' + player_hand + 'を出しました')
    print('コンピュータは' + computer_hand + 'を出しました')
    # 1秒待つ
    time.sleep(1)

    # あいこは0、プレイヤーが負けた時は-1か2、プレイヤーが勝った時は1か-2で勝敗の判定
    judge = computer_hand_num - player_hand_num
    # じゃんけんの勝敗を表示
    if judge in [0]:
        print('あいこです。もう1回！')
    elif judge in [-1, 2]:
        print('あなたの負け')
        # ゲームを終了する
        break
    elif judge in [1, -2]:
        print('あなたの勝ち')
        # ゲームを終了する
        break
