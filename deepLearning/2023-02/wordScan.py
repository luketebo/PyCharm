def read():
    with open("Hamlet.txt") as f:
        read_data = f.readlines()
        read_ = []
        for i in range(len(read_data)):
            read_.append(read_data[i].replace('\n', '').replace(';', '').replace("?", "").replace(':', "")
                         .replace(',', '').replace('!', '').replace('.', '').replace('--', ' ').replace('|', '')
                         .replace('[', '').replace(']', ''))
        _read = []
        for i in range(len(read_)):
            if '' != read_[i]:
                _read = _read + read_[i].split()
        count = {}
        for word in _read:
            count[word] = count.get(word, 0) + 1
        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse=True)
        for index in range(len(items)):
            word, count = items[index]
            print(f"{word}:{count}")


if __name__ == '__main__':
    read()
