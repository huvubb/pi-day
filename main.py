import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import mpmath as mp


def find_birthday():
    try:
        birthday = datetime.strptime(date.get(), '%Y/%m/%d').strftime('%Y%m%d')
        mp.mp.dps = max(100, int(precision.get() or 10000)) + 1
        pos = str(mp.pi).split('.')[1].find(birthday)
        result.config(text=f'✨ 找到了！\n你的生日藏在 π 小数点后第 {pos + 1} 位。\n\n这串数字穿越无穷，最后遇见了你。' if pos >= 0 else '🌙 这次还没找到，\n但你依然是独一无二的数字。')
    except ValueError:
        messagebox.showwarning('格式提示', '请输入 yyyy/mm/dd，例如 2000/01/01')


root = tk.Tk()
root.title('你的生日在圆周率哪里')
root.geometry('430x300')
root.configure(bg='#fff5f7')
tk.Label(root, text='💌 你的生日在圆周率哪里', font=('微软雅黑', 18, 'bold'), bg='#fff5f7', fg='#c94f76').pack(pady=18)
tk.Label(root, text='生日（yyyy/mm/dd）', bg='#fff5f7').pack()
date = tk.Entry(root, justify='center', font=('Arial', 13))
date.pack(pady=5)
tk.Label(root, text='搜索小数位（默认 10000）', bg='#fff5f7').pack()
precision = tk.Entry(root, justify='center', font=('Arial', 11))
precision.insert(0, '10000')
precision.pack(pady=5)
tk.Button(root, text='开始寻找 💖', command=find_birthday, bg='#e982a3', fg='white', relief='flat', padx=18, pady=7).pack(pady=12)
result = tk.Label(root, text='输入你的生日，让我去 π 里找找看~', bg='#fff5f7', fg='#8d5366', font=('微软雅黑', 11), justify='center')
result.pack(pady=5)
root.mainloop()
