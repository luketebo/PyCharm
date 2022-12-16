def hex_to_int16(hex_data):
    return int(hex_data, 16)


def CrackHead(code_, type_):
    ecx = type_
    edi = 0
    while ecx != 0:
        eax = str(ecx)
        ebx = code_
        eax_ = hex(hex_to_int16(eax) * hex_to_int16(ebx))[2:]
        edi = hex(hex_to_int16(eax_) + hex_to_int16(str(edi)))[2:]
        ecx -= 1
    return edi


def getVolumeInformation(name):
    asc_list = []
    for i in name:
        asc_list.append(hex(ord(i))[2:])
    asc_list.reverse()
    asc_list = asc_list[:4]
    print(f"asc_list: {asc_list}")
    Volume = ""
    for item in asc_list:
        Volume += str(item)
    return Volume


if __name__ == "__main__":
    print("仅支持数字和字母，汉字目前转ASCII有问题，还没有解决")
    VolumeName = input("请输入卷标名：")
    type_ = int(input("请输入磁盘类型：（u盘：2 硬盘：3）"))
    code = getVolumeInformation(VolumeName)
    register = CrackHead(code, type_)
    register = hex_to_int16(register)
    print("注册码： " + str(register))
