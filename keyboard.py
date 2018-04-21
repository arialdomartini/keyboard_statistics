import csv

def remove_quotes(s):
    return s
    return s[1:-1]

def main():
    stats = dict()

    with open("keycounter/3") as csv_file:
        reader = csv.reader(csv_file, delimiter=",", quotechar="\"")
        for row in reader:
            key = remove_quotes(row[0])
            usage = remove_quotes(row[1])
            stats[key] = usage

    for k, v in stats.items():
        print(k, " ", v)


if __name__ == "__main__":
    main()
