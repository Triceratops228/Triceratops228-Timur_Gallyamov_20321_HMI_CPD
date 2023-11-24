import tkinter as tk
from tkinter import ttk
import csv
from tkinter import filedialog

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Учет расходов")
        
        # Создаем и размещаем элементы на главном окне
        self.date_label = tk.Label(self.root, text="Дата расхода:")
        self.date_label.grid(row=0,column=0)

        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=1,column=0)

        self.category_label = tk.Label(self.root, text="Категория расхода:")
        self.category_label.grid(row=2,column=0)

        self.category_entry = tk.Entry(self.root)
        self.category_entry.grid(row=3,column=0)

        self.amount_label = tk.Label(self.root, text="Сумма расхода:")
        self.amount_label.grid(row=4,column=0)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=5,column=0)

        self.save_button = tk.Button(self.root, text="Сохранить", command=self.save_expense)
        self.save_button.grid(row=6,column=0)

        self.delete_button = tk.Button(self.root, text="Удалить", command=self.delete_expense)
        self.delete_button.grid(row=7,column=0)

        self.open_button = tk.Button(self.root, text="Открыть CSV", command=self.open_csv)
        self.open_button.grid(row=8,column=0)

        self.save_csv_button = tk.Button(self.root, text="Сохранить в CSV", command=self.save_csv)
        self.save_csv_button.grid(row=9,column=0)

        # Создаем Treeview для отображения данных
        self.expense_tree = ttk.Treeview(self.root, columns=("Дата","Категория","Сумма"), show = "headings")
        self.expense_tree.heading("Дата", text="Дата")
        self.expense_tree.heading("Категория", text="Категория")
        self.expense_tree.heading("Сумма", text="Сумма")
        self.expense_tree.grid(row=10,column=0)

        # Создаем метку для отображения суммы
        self.total_label = tk.Label(self.root, text="Итого: 0.00 руб")
        self.total_label.grid()

    def save_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        
        # Добавляем данные в таблицу Treeview
        self.expense_tree.insert('', 'end', values=(date, category, amount), tags=('data',))
        
        # Обновляем сумму расходов
        self.update_total()

        # Очищаем поля ввода после сохранения
        self.date_entry.delete(0, 'end')
        self.category_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')



    def delete_expense(self):
        selected_item = self.expense_tree.selection()
        if selected_item:
            self.expense_tree.delete(selected_item)
            # Обновляем сумму расходов
            self.update_total()

    def update_total(self):
        total = 0
        for item in self.expense_tree.get_children():
            total += float(self.expense_tree.item(item, 'values')[2])  # Здесь '2' - индекс столбца "Сумма"
        self.total_label.config(text=f"Итого: {total:.2f} руб")

    def open_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            # Очищаем таблицу перед загрузкой данных из CSV файла
            for item in self.expense_tree.get_children():
                self.expense_tree.delete(item)
            
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.expense_tree.insert('', 'end', values=tuple(row))
            
            # Обновляем сумму расходов после загрузки данных
            self.update_total()

    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for item in self.expense_tree.get_children():
                    values = self.expense_tree.item(item, 'values')
                    writer.writerow(values)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
