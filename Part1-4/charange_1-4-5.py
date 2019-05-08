def change_to_float(str_in):
    """
    引数をfloat型に変換する．変換できない文字列の場合，エラーメッセージを出力する．

    Parameters
    ----------
    str_in : str
        float型に変換される文字列

    Returns
    ----------
    float_out : float
        文字列からfloat型に変換された値．
    """
    try:
        float_out = float(str_in)
        return float_out
    except ValueError:
        print("Error ! It's not Value!")

put_float = change_to_float("100.5")
put_float2 = change_to_float("HogeHoge")

print(put_float)
print(put_float2)