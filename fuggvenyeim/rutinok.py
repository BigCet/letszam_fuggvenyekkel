
def honap_atalakito(honap):
    if honap == "1" or honap == "01" or honap == "Január":
        honap = "Január"
    elif honap == "2" or honap == "02" or honap == "Február":
        honap = "Február"
    elif honap == "3" or honap == "03" or honap == "Március":
        honap = "Március"
    elif honap == "4" or honap == "04" or honap == "Április":
        honap = "Április"
    elif honap == "5" or honap == "05" or honap == "Május":
        honap = "Május"
    elif honap == "6" or honap == "06" or honap == "Június":
        honap = "Június"
    elif honap == "7" or honap == "07" or honap == "Július":
        honap = "Július"
    elif honap == "8" or honap == "08" or honap == "Augusztus":
        honap = "Augusztus"
    elif honap == "9" or honap == "09" or honap == "Szeptember":
        honap = "Szeptember"
    elif honap == "10" or honap == "Október":
        honap = "Október"
    elif honap == "11" or honap == "November":
        honap = "November"
    elif honap == "12" or honap == "December":
        honap = "December"

    else:
        honap=False

    return honap

def napok_validalas(nap):
    if nap <= "32":
        return nap
    else:
        nap = False

    return nap

def szakok_validalasa(szak):
    if szak == "B1" or szak == "b1":
        szak = "B1"

    elif szak == "B2" or szak == "b2":
        szak = "B2"

    elif szak == "B3" or szak == "b3":
        szak = "B3"

    elif szak == "B4" or szak == "b4":
        szak = "B4"

    elif szak == "H4" or szak == "h4":
        szak = "H4"

    elif szak == "H5" or szak == "h5":
        szak = "H5"

    elif szak == "H6" or szak == "h6":
        szak = "H6"

    else:
        szak = False

    return szak







