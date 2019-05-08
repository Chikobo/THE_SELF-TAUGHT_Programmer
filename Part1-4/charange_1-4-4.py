def waru2(in_warareru):
    """
    引数を2で割る．

    Parameters
    ----------
    in_warareru : int
        割られる数．

    Returns
    ----------
    in_warareru // 2 : int
        引数を2で割った整数．
    """
    return in_warareru // 2

def kakeru4(in_kakerareru):
    """
    引数に4をかける．

    Parameters
    ----------
    in_kakerareru : int
        かけられる数．

    Returns
    ----------
    in_kakerareru * 4 : int
        引数に4をかけた整数．
    """
    return in_kakerareru * 4

x = waru2(9)
print(kakeru4(x))