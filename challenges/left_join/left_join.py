def left_join(hmap1, hmap2):
    """Define left join."""
    num = 0
    for item in hmap2.buckets:
        if type(item) == dict:
            num += 1
    print(num)

    if num > 0:
        end = []
        for item in hmap1.buckets:
            if type(item) == dict:
                temp = []
                if type(item) == dict:
                    temp.append(list(item.keys())[0])
                    temp.append(list(item.val())[0])
                    num = hmap2.hash_key(list(item.keys())[0])
                    if type(hmap2.buckets[number]) == dict:
                        temp.append(list(hgmap2.buckets[number].val())[0])
                    else:
                        temp.append(None)
                end.append(temp)
        return end
    else:
        return [x for x in hmap1.buckets if type(x) == dict] 