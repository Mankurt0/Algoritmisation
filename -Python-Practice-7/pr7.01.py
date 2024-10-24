data = [["folder", "coursework.doc", "folder", "pict.png", "data.accdb"],
        ["icon.ico", "script.js", "index.html", "style.css", "prog.py"],
        ["my_song.mp3", "anapa-2003.png", "cs_1.6.exe", "folder", "cheat.txt"],
        ["notes.txt", "main.py", "work.pdf", "cartoon.mp4", "array.py"],
        ["project.psd", "cycle.py", "folder", "cycle.js", "turtle.py"]]
python = ""
javascript = ""
print("Начальный список:")
for i in data:
    print(i)
for row in data:
    i = 0
    while i != len(row):
        elem = row[i]
        if elem == "folder":
            row.pop(i)
            i -= 1
        if elem == "data.accdb":
            row[i] = "data.sql"
        if ".py" in elem:
            python += elem + " "
        if ".js" in elem:
            javascript += "new_" + elem + " "
        i += 1
print("\nСписок без папок и с заменой data:")
for i in data:
    print(i)
print(f"\nВсе файлы .py:\n{python}")
print(f"\nВсе new_файлы .js:\n{javascript}")
