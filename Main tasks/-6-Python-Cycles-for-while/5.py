tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате",
         "Подготовить отчёт"]
for i, task in enumerate(tasks, start=1):
    if "(Важная)" in task:
        print(i, "!:", task)
    else:
        print(i, ":", task)
