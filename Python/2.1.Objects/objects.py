# x = [1, 2, 3]
# y = x

# x.append(4)

# print(x)
# print(y)

# x = 1
# print(isinstance(x, float))

# print(type(print()))

# for i in range(2):
#     a = True
#     print(id(a))

#     a = False
#     print(id(a))

# import time

# x = 4
# print(id(x))
# x = 0

# time.sleep(5)
# y = 4

# print(f"x: {id(x)}\ny: {id(y)}")

# import time
# from threading import Thread


# def sleepMe(i):
#     print("Поток %i засыпает на 5 секунд.\n" % i)
#     time.sleep(5)
#     print("Поток %i сейчас проснулся.\n" % i)


# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()

# def remind():
#     text = input('О чем вам напомнить?\n')
#     local_time = float(input('Через сколько минут?\n'))
#     local_time *= 60
#     time.sleep(local_time)
#     print(text)

# th = Thread(target=remind, args=())
# th.start()

# time.sleep(20)
# print('Пока поток работает, мы можем сделать что-нибудь еще \n')

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(300, 300)
#     w.setWindowTitle('Guru99')
#     w.show()
#     sys.exit(app.exec_())
