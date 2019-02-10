from tkinter import Tk, Frame, Canvas, ALL
import numpy as np

size = 500


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Main()
        self.mainloop()

    def Main(self):
        self.canvas = Canvas(self.master, width=size, height=size)
        self.canvas.grid()

        self.Setup()

    def Setup(self):
        self.canvas.arr = np.arange(size)
        np.random.shuffle(self.canvas.arr)
        self.time = 0

        self.Update()

    def Update(self):
        self.canvas.delete(ALL)
        for i in range(len(self.canvas.arr)):
            lenght = self.canvas.arr[i]
            self.canvas.create_line(size-i, size, size-i, lenght, fill="white")

#       ###algo###
        for j in range(len(self.canvas.arr)-self.time-1):
            if self.canvas.arr[j] > self.canvas.arr[j+1]:
                self.canvas.arr[j], self.canvas.arr[j+1] = self.canvas.arr[j+1], self.canvas.arr[j]
        print(self.canvas.arr)
        self.time += 1

        self.after(100, self.Update)


def main():
    App(Tk())


if __name__ == "__main__":
    main()
