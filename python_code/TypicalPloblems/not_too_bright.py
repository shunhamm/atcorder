def main():
    H, W = map(int, input().split(" "))

    #  縦、横の偶奇で場合分け
    led_h = H / 2 if H % 2 == 0 else H // 2 + 1
    led_w = W / 2 if W % 2 == 0 else W // 2 + 1

    #  縦または横が1の時は全てのマスにLEDを置けることを考慮する
    print(H * W if H == 1 or W == 1 else int(led_h * led_w))


if __name__ == '__main__':
    main()
