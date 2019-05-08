def func(a,b,c,d=10,e=5):
    """
    必須変数の和を計算する．
    また，その和にオプション変数であるdをかけ，eで割る．

    Parameters
    ----------
    a : int
        和の第一引数．
    b : int
        和の第二引数．
    c : int
        和の第三引数．
    d : int, default 10
        a,b,cの和にかける数．
    e : int, default 5
        a,b,cの和かけるdを割る数．

    Returns
    ----------
    z : float
        (a+b+c)*d/eの計算結果．
    """
    z = a + b + c
    z = z * d / e
    return z

z = func( 3, 2, 5 )
print(z)