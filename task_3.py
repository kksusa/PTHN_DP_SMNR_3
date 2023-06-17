from random import shuffle

camp_things = {"палатка": 2, "спальник": 2, "аптечка": 2, "дождевик": 0.7, "лопата": 0.5, "фонарик": 0.3,
               "тарелка": 0.4, "кружка": 0.2, "ложка": 0.05, "вилка": 0.05, "нож": 0.05, "кастрюля": 1, "сковородка": 1,
               "спички": 0.05, "компас": 0.1, "веревка": 0.4, "туалетная бумага": 0.1, "щётка зубная": 0.05,
               "зубная паста": 0.1, "полотенце": 0.2, "хлеб": 0.4, "картошка": 2, "гречка": 0.5, "мясо": 1, "куртка": 1,
               "кофта": 1, "носки": 0.2}
sorted_things = sorted(camp_things.items(), key=lambda item: item[1], reverse=True)
print(sorted_things)
listed_things = list(camp_things.items())
shuffle(listed_things)
load = 0
BACKPACK_MAX_LOAD = 10
print("Список вещей в рюкзаке:")
while load < BACKPACK_MAX_LOAD:
    """Вариант 1: если проходить по отсортированному списку от большего к меньшему"""
    # for i in range(len(sorted_things)):
    #     if sorted_things[i][1] <= BACKPACK_MAX_LOAD - load:
    #         load += sorted_things[i][1]
    #         print(f"{i + 1}: {sorted_things[i][0]} (загрузка: {load:.2f} кг)")
    # if i == len(sorted_things) - 1:
    #     break

    """Вариант 2: каждый раз получается уникальная последовательность вещей для отбора"""
    for i in range(len(listed_things)):
        if listed_things[i][1] <= BACKPACK_MAX_LOAD - load:
            load += listed_things[i][1]
            print(f"{i + 1}: {listed_things[i][0]} (загрузка: {load:.2f} кг)")
    if i == len(listed_things) - 1:
        break
print(f"Общая загрузка рюкзака: {load:.2f} кг")
