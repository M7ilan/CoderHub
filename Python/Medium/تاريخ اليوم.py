
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def date_format(date: str) -> str:
    x = date.split('/')
    split1 = x[0]
    split2 = x[1]
    split3 = x[2]
    reverse = f"{split2}/{split3}/{split1}"
    dash = '-'.join(x)
    x = f"{date} | {dash} | {reverse}"
    return x