import csv
import operator

def remove_quotes(s):
    return s
    return s[1:-1]

def group(stats):
    gstats = {}
    grouped = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "9",
        "9": "9",
        "F1": "F1",
        "F2": "F2",
        "F3": "F3",
        "F4": "F4",
        "F5": "F5",
        "F6": "F6",
        "F7": "F7",
        "F8": "F8",
        "F9": "F9",
        "F10": "F10",
        "F11": "F11",
        "F12": "F12",
        "Up": "Up",
        "Down": "Down",
        "Left": "Left",
        "Right": "Right",
        "Insert": "Insert",
        "Home": "Home",
        "Delete": "Delete",
        "End": "End",
        "PgUp": "PgUp",
        "PgDn": "PgDn",
        "Enter": "Enter",
        "Backspace": "Backspace",
        "Space": "Space",
        "Escape": "Escape",
        "Tab": "Tab",
        "Pause": "Pause",
        "LControl": "Control",
        "RControl": "Control",
        "LAlt": "Alt",
        "RAlt": "Alt",
        "LShift": "Shift",
        "RShift": "Shift",
        "LWin": "LWin",
        "RWin": "RWin",
        "CapsLock": "Control",
        "NumLock": "NumLock",
        "ScrollLock": "ScrollLock",
        "AppsKey": "AppsKey",
        "PrintScreen": "PrintScreen",
        "`": "`",
        "~": "`",
        "!": "1",
        "@": "2",
        "#": "3",
        "$": "4",
        "%": "5",
        "^": "6",
        "&": "7",
        "*": "8",
        "(": "9",
        ")": "0",
        "-": "-",
        "_": "-",
        "=": "=",
        "+": "=",
        "[": "[",
        "{": "[",
        "]": "]",
        "}": "]",
        "\\": "\\",
        "|": "\\",
        ";": ";",
        ":": ";",
        "'": "'",
        '"': "'",
        ",": ",",
        "<": ",",
        ".": ".",
        ">": ".",
        "/": "/",
        "?": "/"
    }
    for k, v in stats.items():
        if k in grouped:
            gk = grouped[k]
            if gk not in gstats:
                gstats[gk] = 0
            gstats[gk] = gstats[gk] + v
    return gstats

def main():
    stats = dict()

    with open("keycounter/3") as csv_file:
        reader = csv.reader(csv_file, delimiter=",", quotechar="\"")
        c = 0
        for row in reader:
            c = c + 1
            if c > 1:
                key = remove_quotes(row[0])
                usage = int(remove_quotes(row[1]))
                stats[key] = usage



    gstats = group(stats)
    res = sorted(gstats.items(), key=lambda x: x[1], reverse=True)
    for k, v in res:
        print(k, " ", v)


if __name__ == "__main__":
    main()

