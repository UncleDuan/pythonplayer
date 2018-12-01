# __codeing__ 'UTF-8'
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from aip import AipSpeech
from playsound import playsound


class Voice(object):
    def __init__(self):
        self.file_count = 0

        self.top = tk.Tk()
        self.top.title('语音软件界面')
        self.top.geometry('400x500')
        self.top.resizable(0, 0)
        self.top.protocol('WM_DELETE_WINDOW', self.myquit)

        self.label = tk.Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'),
                              text='输入要转换文字')
        self.label.pack()
        self.confm = tk.Frame(self.top)
        self.consb = tk.Scrollbar(self.confm)
        self.consb.pack(side=tk.RIGHT, fill=tk.Y)
        self.contents = tk.Text(self.confm, font=10, height=26, width=50, yscrollcommand=self.consb.set)
        self.consb.config(command=self.contents.yview)
        self.contents.pack(side=tk.LEFT, fill=tk.BOTH)
        self.confm.pack()

        self.selfm = tk.Frame(self.top, borderwidth=1, relief=tk.SUNKEN, pady=3)

        per_label = tk.Label(self.selfm, font=10, text='发音：')
        per_label.grid(column=0, row=0)
        self.perchosen = ttk.Combobox(self.selfm, width=5, font=9)
        self.perchosen['values'] = ('男声', '女声', '混合')
        self.perchosen.grid(column=1, row=0)
        self.perchosen.current(0)

        spd_label = tk.Label(self.selfm, font=10, text='语速：')
        spd_label.grid(column=2, row=0)
        self.spdchosen = ttk.Combobox(self.selfm, width=5, font=9)
        self.spdchosen['values'] = ('慢', '普通', '快')
        self.spdchosen.grid(column=3, row=0)
        self.spdchosen.current(1)

        pit_label = tk.Label(self.selfm, font=10, text='语调：')
        pit_label.grid(column=4, row=0)
        self.pitchosen = ttk.Combobox(self.selfm, width=5, font=9)
        self.pitchosen['values'] = ('低', '中', '高')
        self.pitchosen.grid(column=5, row=0)
        self.pitchosen.current(2)

        self.selfm.pack()

        self.bfm = tk.Frame(self.top)
        self.clrtext = tk.Button(self.bfm, text='清除', width=10, font=8,
                                 command=self.clrtext, activeforeground='white', activebackground='blue')
        self.play = tk.Button(self.bfm, text='播放', width=10, font=8,
                              command=self.txt2voice, activeforeground='white', activebackground='green')
        self.quit = tk.Button(self.bfm, text='退出', width=10, font=8,
                              command=self.myquit, activeforeground='white', activebackground='red')
        self.play.pack(side=tk.LEFT)
        self.clrtext.pack(side=tk.LEFT)
        self.quit.pack(side=tk.LEFT)
        self.bfm.pack()

    def myquit(self):
        myquit = tkinter.messagebox.askokcancel('提示', '确认退出？')
        if myquit == True:
            self.top.destroy()

    def clrtext(self):
        self.contents.delete(0.0, tk.END)

    def get_voice_para(self):
        per_dict = {'女声': 0, '男声': 1, '混合': 2}
        spd_dict = {'慢': 3, '普通': 5, '快': 9}
        pit_dict = {'低': 0, '中': 5, '高': 9}
        self.per = per_dict[self.perchosen.get()]
        self.spd = spd_dict[self.spdchosen.get()]
        self.pit = pit_dict[self.pitchosen.get()]

    def txt2voice(self):
        APP_ID = '14624722'
        API_KEY = 'ZIjGS2NA7ksxQsH29rfA538i'
        SECRET_KEY = '716BPFUDDsOjHUOKYghRxcLavveyag14'
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        txt = self.contents.get('0.0', 'end')
        if txt == '\n':
            tk.messagebox.showinfo('', '请输入需要播放的文字')
            return
        self.get_voice_para()
        result = client.synthesis(txt, 'zh', 1,
                                  {
                                      'per': self.per,
                                      'pit': self.pit,
                                      'spd': self.spd
                                  })
        if not isinstance(result, dict):
            self.file_count += 1
            file = self.get_filename()
            with open(file, 'wb') as f:
                f.write(result)
            playsound(file)

    def get_filename(self):
        return 'voice' + str(self.file_count) + '.mp3'


if __name__ == '__main__':
    s = Voice()