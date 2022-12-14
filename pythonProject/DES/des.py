# S盒 的置换矩阵
S_MATRIX = [(14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
             0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
             4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
             15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),
            (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
             3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
             0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
             13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
            (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
             13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
             13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
             1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),
            (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
             13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
             10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
             3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),
            (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
             14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
             4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
             11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3),
            (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
             10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
             9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
             4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),
            (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
             13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
             1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
             6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),
            (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
             1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
             7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
             2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)]
# P置换的置换矩阵
P_MATRIX = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
# IP置换的 置换矩阵
IP_MATRIX = [58, 50, 42, 34, 26, 18, 10, 2,
             60, 52, 44, 36, 28, 20, 12, 4,
             62, 54, 46, 38, 30, 22, 14, 6,
             64, 56, 48, 40, 32, 24, 16, 8,
             57, 49, 41, 33, 25, 17, 9, 1,
             59, 51, 43, 35, 27, 19, 11, 3,
             61, 53, 45, 37, 29, 21, 13, 5,
             63, 55, 47, 39, 31, 23, 15, 7]

# 压缩置换矩阵  从56位里选48位
COMPRESS_MATRIXS = [14, 17, 11, 24, 1, 5,
                    3, 28, 15, 6, 21, 10,
                    23, 19, 12, 4, 26, 8,
                    16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]
# E扩展置换矩阵

E_MATRIX = [32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]
# IP逆置换矩阵
IP_INVERSE_MATRIX = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
                     38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                     36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
                     34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


def Chr2Bin(text):
    bins = ""
    for i in range(len(text)):
        bins += bin(ord(text[i]))
    return bins


# IP置换
def IPChange(plaintext):
    ret = ""
    for i in IP_MATRIX:
        ret = ret + plaintext[i - 1]
    return ret


# 循环移位
def move(text, number):
    text = text[number:] + text[0:number]
    return text


# 子密钥
def createKey(key):
    Llist = [57, 49, 41, 33, 25, 17, 9,
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36]
    Rlist = [63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4]

    L0 = ""
    R0 = ""

    for i in Llist:
        L0 += key[i - 1]
    for i in Rlist:
        R0 += key[i - 1]

    MoveTimes = [2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2]
    subKey = []
    # 16轮置换
    for i in range(0, 16):
        L0 = move(L0, MoveTimes[i])
        R0 = move(R0, MoveTimes[i])
        # 合并
        mergeKey = L0 + R0

        tempKey = ""
        for i in COMPRESS_MATRIXS:
            tempKey += mergeKey[i - 1]
        subKey.append(tempKey)
    return subKey


# 把右边32位拓展为48位
def E_expend(Rn):
    temRn = ""
    for i in E_MATRIX:
        temRn += Rn[i - 1]
    return temRn


# S盒运算
def S_sub(text):
    text = bin(text)[2:]

    while len(text) < 48:
        text = "0" + text

    index = 0
    temStr = ""

    for ls in S_MATRIX:
        row = int(text[index] + text[index + 5], base=2)
        col = int(text[index + 1:index + 5], base=2)
        tem_single = bin(ls[row * 16 + col])[2:]

        while len(tem_single) < 4:
            tem_single = "0" + tem_single

        temStr += tem_single
        index += 6

    return temStr


# P盒
def P(Ln, subStr, oldRn):
    tmp = ""
    for i in P_MATRIX:
        tmp += subStr[i - 1]
    LnNew = int(tmp, base=2) ^ int(Ln, base=2)
    LnNew = bin(LnNew)[2:]
    while len(LnNew) < 32:
        LnNew = "0" + LnNew
    (Ln, Rn) = (oldRn, LnNew)
    return (Ln, Rn)


def IP_reverse(L, R):
    tmp = L + R
    tmpStr = ""
    for i in IP_INVERSE_MATRIX:
        tmpStr += tmp[i - 1]
    return tmpStr


def DES(text, key, flag='0'):
    InitKey = IPChange(text)
    subKeyList = createKey(key)
    Ln = InitKey[0:32]
    Rn = InitKey[32:]

    if ('-1' == flag):
        subKeyList = subKeyList[::-1]

    for subKey in subKeyList:
        while len(Rn) < 32:
            Rn = "0" + Rn
        while len(Ln) < 32:
            Ln = "0" + Ln

        Rn_expend = E_expend(Rn)
        # print("Rn_expend: " + Rn_expend)
        S_Input = int(Rn_expend, base=2) ^ int(subKey, base=2)
        # print('S_Input: ' + str(S_Input))
        subStr = S_sub(S_Input)
        # print('subStr: ' + subStr)

        (Ln, Rn) = P(Ln, subStr, Rn)

    (Ln, Rn) = (Rn, Ln)
    en_text = IP_reverse(Ln, Rn)
    return en_text


if __name__ == '__main__':
    # key = '1100110111111000110000101111011110110000101100101100100010101011'
    # plaintext = '1101011011011000110001111110110011001010101001101011010011110011'
    key = "0001001000110100010101100111100010010001001000110100010101100111"
    plaintext = "1001100001110110010101000011001000010001010001110010010110000011"
    print('明文：' + plaintext)

    ciphertext = DES(plaintext, key)
    print('密文: ' + ciphertext)

    decode_ciphertext = DES(ciphertext, key, flag='-1')
    print('解密: ' + decode_ciphertext)

    # print(plaintext)
    # print(decode_ciphertext)

    # print('明文: ' + hex(int(plaintext, base=2)).upper())
    #
    # ciphertext = DES(plaintext, key)
    #
    # print("密文: " + hex(int(ciphertext, base=2)).upper())
    #
    # decode_ciphertext = DES(plaintext, key, flag='-1')
    #
    # print('解密: ' + hex(int(decode_ciphertext, base=2)).upper())