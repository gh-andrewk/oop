filenames = [
    "1.txt",
    "2.txt",
    "3.txt",
]

files_data = []
for fname in filenames:
    with open(f"testfiles/{fname}", "rt", encoding="utf8") as f:
        data = f.readlines()
        cnt = sum(1 for _ in f)
        files_data.append({"name": fname, "line_cnt": len(data), "data": "".join(data)})

files_data.sort(key=lambda x: x["line_cnt"])

with open("testfiles/out.txt", "wt", encoding="utf8") as f:
    for file in files_data:
        f.write(f"{file['name']}\n")
        f.write(f"{file['line_cnt']}\n")
        f.write(f"{file['data']}\n")
