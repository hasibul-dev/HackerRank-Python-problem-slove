if __name__ == '__main__':
    s = input().strip()
    
    freq = {}
    
    # count characters manually (no Counter for uniqueness)
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # convert to list of tuples
    items = list(freq.items())

    # custom sorting: (-count, char)
    items.sort(key=lambda x: (-x[1], x[0]))

    # print top 3
    for ch, count in items[:3]:
        print(ch, count)
