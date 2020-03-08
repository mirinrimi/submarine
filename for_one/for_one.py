Alfabet = ["A", "B", "C", "D", "E"]
Number = ["1", "2", "3", "4", "5"]

# A1座標から[1, 0, 0, 0, 0]座標への変換
def coord_chg(str): 
    pt = [0, 0, 0, 0, 0]
    pt[Alfabet.index(str[0])] = int(str[1])
    return pt

# 逆変換
def inverse_chg(list):
    for i in range(1, 6):
        try:
            box = Alfabet[list.index(i)] + str(sum(list))
        except:
            pass
    return box


# 正しい座標かの判定式
def cri(str):
    if len(str) == 2 and Alfabet.count(str[0]) == 1 and Number.count(str[1]) == 1:
        return True
    else:
        return False


# 距離の定義（A1座標を代入すること！）
def dis(s_1, s_2):
    dis = abs(Alfabet.index(s_1[0]) - Alfabet.index(s_2[0])) + abs(int(s_1[1]) - int(s_2[1]))
    return dis


#ソナーを打つやつ
def sonar():
    snr = input("ソナーを打ちますか？[Y/N]: ").upper()
    if snr in ["Y", "YE", "YES"]:
        if dis(inverse_chg(ipt), inverse_chg(dpt)) <= 3:
            print("敵潜水艦の座標は" + inverse_chg(dpt) + "と判明しました。")
            print("敵潜水艦からのソナーを感知しました。")
        else:
            print("ソナーに反応するものはありません。")
    elif snr in ['N', 'NO']:
        pass
    else:
        print(" Y/YES または N/NO で入力してください。")
        return sonar()
         

# 移動距離の制限
rest = 2


# 防潜の初期配置
dpt = [0, 0, 0, 1, 0]

# -------------------------------------------

while True:
    ifirst = input("初期配置を入力: ")
    if cri(ifirst):
        ipt = coord_chg(ifirst)
        break
    else:
        print("正しい座標を入力してください(例:A1)")
    
print(inverse_chg(ipt) + "に到着しました。")

while True:
    while True:
        move = input("移動先を入力: ")
        if not cri(move):
            print("正しい座標を入力してください(例:A1)")
        elif dis(inverse_chg(ipt), move) > rest:
            print("移動できない座標が選択されています。")
        else:
            ipt = coord_chg(move)
            break
        
    print(inverse_chg(ipt) + "に移動しました。")

    if ipt == dpt:
        print("""\
            侵潜が防潜に激突！
            防潜は撃沈！
            侵略軍の勝利！""")
        break
    else:
        sonar()
        print("ターンを終了します。")





