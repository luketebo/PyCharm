def hex_to_int16(hex_data):
    return int(hex_data, 16)


if __name__ == '__main__':
    X = '35323335'
    Y = '2'
    z = hex(hex_to_int16(X) * hex_to_int16(Y))
    print(z)