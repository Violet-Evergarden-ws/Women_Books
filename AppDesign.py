import tkinter as tk
from time import sleep
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import translate as tl
import time

# 使窗口在中心弹出
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


# 设置返回按钮
def turn_back(root):
    bu1 = tk.Button(root, text="返回",
                    command=lambda: [root.destroy(), Function_selection()],
                    width=5, height=1)
    bu1.grid(row=0, column=0)

def insert_logo(root, window_width):
    # 加载图片
    loading_1 = Image.open(r"Image\logo.png")
    loading_1 = loading_1.resize((150, 50))
    photo_1 = ImageTk.PhotoImage(loading_1)

    # 获取图片尺寸
    width_1 = photo_1.width()
    height_1 = photo_1.height()

    # 创建标签，并将图片插入
    label_1 = tk.Label(root, image=photo_1, bg="White")
    label_1.image = photo_1
    label_1.place(x=(window_width - width_1) / 2, y=0)

def loading():  # 创建加载界面

    # 创建加载进度条
    def Pro_Bar(root_loading):
        # 标签
        label = tk.Label(root_loading, text='加载中...', font=('黑体', 12), bg="White")
        label.place(x=10, y=270)
        # 进度条
        progressbar = ttk.Progressbar(root_loading)
        progressbar.place(x=90, y=270)
        # 设置进度条最大值为100
        progressbar['maximum'] = 100
        # 设置进度条长度
        progressbar['length'] = 280

        def Value_Bar(root_loading):
            for i in range(100):
                progressbar['value'] = i + 1
                sleep(0.01)
                root_loading.update()

            # 跳转到应用界面
            if progressbar['value'] >= 100:
                root_loading.destroy()  # 关闭加载窗口

        # 控制进度条启动
        Value_Bar(root_loading)

    # 插入图片
    def insert_pic(root_loading, window_width, window_height):
        # 加载图片
        loading_1 = Image.open(r"Image\loading_1.png")
        loading_1 = loading_1.resize((int(window_width / 1.5), int(window_height / 1.5)))
        photo_1 = ImageTk.PhotoImage(loading_1)

        # 获取图片尺寸
        width_1 = photo_1.width()
        height_1 = photo_1.height()

        # 创建标签，并将图片插入
        label_1 = tk.Label(root_loading, image=photo_1, bg="White")
        label_1.image = photo_1
        label_1.place(x=(window_width - width_1) / 2, y=(window_height - height_1) / 2 - 40)

    # 创建窗口
    root_loading = tk.Tk()
    root_loading.title("Women's Books Translator")
    root_loading.resizable(False,False)  # 禁用最大化功能  # 禁用最大化功能
    root_loading.configure(bg="White")  # 背景颜色
    root_loading.geometry("400x300")
    # 设置窗口尺寸
    window_width = 400
    window_height = 300

    center_window(root_loading, window_width, window_height)
    insert_pic(root_loading, window_width, window_height)
    Pro_Bar(root_loading)
    root_loading.mainloop()


# 创建功能选择页面
def Function_selection():

    def image_word(root_selection, button_x, button_y):
        # 加载图片
        selection_word = Image.open(r"Image\word.png")
        selection_word = selection_word.resize((50, 50))
        photo_word = ImageTk.PhotoImage(selection_word)

        # 获取图片尺寸
        width_1 = photo_word.width()
        height_1 = photo_word.height()

        # 创建标签，并将图片插入
        label_1 = tk.Label(root_selection, image=photo_word, bg="White")
        label_1.image = photo_word
        label_1.place(x=button_x-60, y=button_y-15)

    def image_pic(root_selection, button_x, button_y):
        # 加载图片
        selection_word = Image.open(r"Image\image.jpg")
        selection_word = selection_word.resize((50, 50))
        photo_word = ImageTk.PhotoImage(selection_word)

        # 获取图片尺寸
        width_1 = photo_word.width()
        height_1 = photo_word.height()

        # 创建标签，并将图片插入
        label_1 = tk.Label(root_selection, image=photo_word, bg="White")
        label_1.image = photo_word
        label_1.place(x=button_x-60, y=button_y-15)

    def button_word():
        root_selection.destroy()
        windows_word()

    def button_image():
        root_selection.destroy()
        windows_WBooks()

    root_selection = tk.Tk()
    root_selection.title("Women's Books Translator")
    root_selection.resizable(False,False)  # 禁用最大化功能
    root_selection.configure(bg="White")  # 背景颜色
    root_selection.geometry("400x300")
    window_width = 400
    window_height = 300
    center_window(root_selection, window_width, window_height)

    insert_logo(root_selection, window_width)
    # 创建跳转文字转女书界面按钮
    but_word = tk.Button(root_selection, text="汉语转女书",
                         command=button_word,  # 设置按钮点击时的响应函数
                         font=("微软雅黑", 10),  # 设置字体和字号
                         bg="green",              # 设置背景颜色
                         fg="white",            # 设置前景颜色（文本颜色）
                         )
    but_word.place(width=200, height=30, x=(window_width - 200) / 2+20, y=((window_height - 30) / 2)-20)
    # 等待窗口渲染完成
    root_selection.update_idletasks()
    # 获取坐标
    butword_x = but_word.winfo_x()
    butword_y = but_word.winfo_y()
    image_word(root_selection, butword_x, butword_y)

    # 创建跳转女书转汉字界面
    but_image = tk.Button(root_selection, text="女书转汉语",
                         command=button_image,  # 设置按钮点击时的响应函数
                         font=("微软雅黑", 10),  # 设置字体和字号
                         bg="green",  # 设置背景颜色
                         fg="white",  # 设置前景颜色（文本颜色）
                         )
    but_image.place(width=200, height=30, x=(window_width - 200) / 2+20, y=((window_height - 30) / 2) + 60)
    # 等待窗口渲染完成
    root_selection.update_idletasks()
    # 获取坐标
    butimage_x = but_image.winfo_x()
    butimage_y = but_image.winfo_y()
    image_pic(root_selection, butimage_x, butimage_y)

    root_selection.mainloop()


def windows_word():

    def word_wb_logo(root, window_width, window_height):
        # 加载图片
        loading_1 = Image.open(r"Image\word_wb.png")
        loading_1 = loading_1.resize((300, 40))
        photo_1 = ImageTk.PhotoImage(loading_1)

        # 获取图片尺寸
        width_1 = photo_1.width()
        height_1 = photo_1.height()

        # 创建标签，并将图片插入
        label_1 = tk.Label(root, image=photo_1, bg="White")
        label_1.image = photo_1
        label_1.place(x=(window_width - width_1) / 2, y=50)

    root_word = tk.Tk()
    root_word.title("Women's Books Translator")
    root_word.resizable(False,False)  # 禁用最大化功能
    root_word.configure(bg="White")  # 背景颜色
    root_word.geometry("700x600")
    root_width = 700
    root_height = 600
    center_window(root_word, root_width, root_height)

    insert_logo(root_word, root_width)
    word_wb_logo(root_word, root_width, root_height)
    turn_back(root_word)

    # 创建一个Entry控件，用于用户输入文本
    entry_word = tk.Entry(root_word, width=50, bg="White", borderwidth=3, relief='sunken')
    entry_word.place(width=500, height=28, x=(root_width-500)/2, y=120)  # 使用padding增加控件之间的空间
    entry_word.config(font=("宋体", 12))

    # 创建一个幕布存放图片
    canvas_word = tk.Canvas(root_word, width=600, height=360, bg="skyblue")
    canvas_word.place(x=(root_width - 600) / 2, y=200)

    # 将文本框里的内容翻译成女书
    def on_submit():
        canvas_word.delete("all")
        k=0
        entry_text = entry_word.get()
        images = tl.word_WBooks(entry_text)
        if len(images)>36:
            messagebox.showerror("语句太长啦！！！")
        else:
            canvas_word.image_list = []
            for image in images:
                if k <= 11:
                    x_label = k * 50
                    y_label = 0
                elif 12 <= k <= 23:
                    x_label = (k - 12) * 50
                    y_label = 120
                elif 24 <= k <= 35:
                    x_label = (k - 24) * 50
                    y_label = 120 * 2
                else:
                    messagebox.showerror("出错啦！！！")
                # 显示图片
                photo = ImageTk.PhotoImage(image=image)
                canvas_word.create_image(x_label, y_label, anchor=tk.NW, image=photo)
                canvas_word.image_list.append(photo)
                k += 1

    # 创建一个按钮，用于提交文本
    submit_button = tk.Button(root_word, text="翻译", command=on_submit, bg="green", fg="white")
    submit_button.place(width=43, height=35, x=(root_width-30)/2, y=155)

    root_word.mainloop()


def windows_WBooks():

    def word_wb_logo(root, window_width, window_height):
        # 加载图片
        loading_1 = Image.open(r"Image\wb_word.png")
        loading_1 = loading_1.resize((300, 40))
        photo_1 = ImageTk.PhotoImage(loading_1)

        # 获取图片尺寸
        width_1 = photo_1.width()
        height_1 = photo_1.height()

        # 创建标签，并将图片插入
        label_1 = tk.Label(root, image=photo_1, bg="White")
        label_1.image = photo_1
        label_1.place(x=(window_width - width_1) / 2, y=50)

    # 选择本地图片
    def load_image():
        # 打开文件选择器
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        entry_path.config(state="normal")
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        entry_path.config(state="disabled")

        # 展示图片
        canvas_image.delete("all")
        photo = Image.open(entry_path.get())
        photo = photo.resize((200, 300))
        photo_bw = ImageTk.PhotoImage(photo)
        canvas_image.create_image(102, 185, image=photo_bw)
        canvas_image.image = photo_bw



    root_image = tk.Tk()
    root_image.title("Women's Books Translator")
    root_image.resizable(False,False)  # 禁用最大化功能
    root_image.configure(bg="White")  # 背景颜色
    root_image.geometry("700x600")
    root_width = 700
    root_height = 600
    center_window(root_image, root_width, root_height)

    insert_logo(root_image, root_width)
    word_wb_logo(root_image, root_width, root_height)
    turn_back(root_image)

    # 显示选择的文件地址
    entry_path = tk.Entry(root_image, width=50, bg="White", borderwidth=3, relief='sunken')
    entry_path.place(width=560, height=28, x=(root_width - 500) / 2, y=120)  # 使用padding增加控件之间的空间
    entry_path.config(font=("宋体", 12), state="disabled")

    # 创建一个幕布存放图片
    canvas_image = tk.Canvas(root_image, width=200, height=360, bg="skyblue")
    canvas_image.place(x=50, y=200)

    # 创建导入文件按钮
    style_1 = ttk.Style()
    style_1.configure("RoundedButton.TButton", relief="groove",
                    foreground="black", background="gray",
                    width="30%", height="30%",
                    font=("宋体", 10))
    but_getimg = ttk.Button(root_image, text="选择图片", style="RoundedButton.TButton",
                            command=load_image)
    but_getimg.place(relx=0.05, rely=0.2)

    # 创建翻译功能
    def image_tran():
        results_wb = tl.WBooks_word(entry_path.get())
        output_result.config(state="normal")
        output_result.delete('1.0', tk.END)  # 清空输出栏的文本
        for result_wb in results_wb:
            output_result.insert(tk.END, result_wb)
            output_result.update_idletasks()  # 更新输出栏的显示
            time.sleep(0.2)  # 暂停一段时间，以便逐字显示
        output_result.config(state="disabled")

    # 翻译按钮
    but_tran = tk.Button(root_image, text="翻译", width=5, height=1,
                         bg='blue', fg='white',
                         font=('微软雅黑', 12),
                         command=image_tran)
    but_tran.place(relx=0.42, rely=0.6)

    # 创建输出栏
    output_result = tk.Text(root_image, height=17, width=25, background="lightgrey",
                            font=("微软雅黑", 12), state="disabled")
    output_result.place(x=400, y=200)

    root_image.mainloop()


if __name__ == '__main__':
    loading()
    Function_selection()
