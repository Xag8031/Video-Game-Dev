# Partially copied from https://stackoverflow.com/a/74162322/11106801
import tkinter as tk

def tksleep(self, time:float) -> None:
    """
    Emulating `time.sleep(seconds)`
    Created by TheLizzard, inspired by Thingamabobs
    """
    self.after(int(time*1000), self.quit)
    self.mainloop()

tk.Misc.tksleep = tksleep # Monkey patching


# Test code
root = tk.Tk()
for i in range(30):
    root.tksleep(1)
    root.title(f"Seconds passed: {i+1}")
root.destroy()
root.mainloop()