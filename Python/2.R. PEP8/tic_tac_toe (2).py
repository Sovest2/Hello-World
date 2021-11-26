class aaaaa:
    def __init__(me, a, b):
        me.a = a
        me.b = b
        me.c = dict()

    def DEF1(me):
        print(f"Имя: { me.a }\nДолжность: { me.b }\nПроекты: { me.c }")

    def DEF2(me, aa):
        me.c[aa] = "Принят в работу"

    def DEF3(me, aa):
        me.c.update(aa)

    def DEF4(me, aa):
        bb = me.c.pop(aa)
        if bb:
            return True
        else:
            return False


new_test = aaaaa(45, 60)

new_test.DEF1()
