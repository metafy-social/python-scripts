def cnt_decoding_digits(dig, a):
    cnt = [0] * (a + 1)
    cnt[0], cnt[1] = 1, 1

    for k in range(2, a + 1):
        cnt[k] = 0
        cnt[k] = cnt[k - 1]

        if dig[k - 2] == '1' or (dig[k - 2] == '2' and dig[k - 1] < '7'):
            cnt[k] += cnt[k - 2]

    return cnt[a]


dig = input("Enter Number : ")
print("Possible count of decoding of the sequence :", cnt_decoding_digits(dig, len(dig)))
