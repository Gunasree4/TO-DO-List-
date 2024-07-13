import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.config(bg="#808080")

        self.tasks = []

        self.frame = tk.Frame(root, bg="#808080")
        self.frame.pack(pady=14)

        self.task_listbox = tk.Listbox(self.frame, width=80, height=15, bg="#ffffff", bd=2, highlightthickness=4, relief="solid")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=(16, 0))

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=80, bd=2, highlightthickness=3, relief="solid", bg="#ffffff")
        self.entry.pack(pady=16)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#87CEEB", fg="#000000", bd=3, highlightthickness=2, relief="groove")
        self.add_task_button.pack(pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#FFE5B4", fg="#000000", bd=3, highlightthickness=2, relief="groove")
        self.delete_task_button.pack(pady=10)

        self.mark_done_button = tk.Button(root, text="Mark as Done", command=self.mark_task_done, bg="#FFFDD0", fg="#000000", bd=3, highlightthickness=2, relief="groove")
        self.mark_done_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, bg="#FF6347", fg="#ffffff", bd=3, highlightthickness=2, relief="groove")
        self.exit_button.pack(pady=10)

        self.load_tasks_into_listbox()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append((task, False))
            self.entry.delete(0, tk.END)
            self.load_tasks_into_listbox()
        else:
            messagebox.showwarning("Warning", " enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.load_tasks_into_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "select a task to delete.")

    def mark_task_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task, done = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = (task, not done)
            self.load_tasks_into_listbox()
        except IndexError:
            messagebox.showwarning("Warning", " select a task to mark as done.")

    def load_tasks_into_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, done in self.tasks:
            display_task = f"{'[DONE] ' if done else ''}{task}"
            self.task_listbox.insert(tk.END, display_task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
