import tkinter as tk
from tkinter import ttk, filedialog

from lesson_file_selection import LessonFileSelection

class LessonFileSelectionForm:
    def __init__(self):
        self.video_file_paths: list[str] = []
        self.root = tk.Tk()
        self.root.title("Lesson Video Speed Editor")
        self.root.geometry("800x400")
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Top row: Add and Remove buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        ttk.Button(button_frame, text="Add Video Files", command=self._browse_files).pack(side="left", padx=(0, 5))
        ttk.Button(button_frame, text="Remove Selected", command=self._remove_selected).pack(side="left")

        # Middle: Listbox with scrollbar
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=1, column=0, sticky="nsew")
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        self.listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox.configure(yscrollcommand=scrollbar.set)

        # Bottom: Submit button
        ttk.Button(main_frame, text="Submit", command=self._on_submit).grid(row=2, column=0, pady=(10, 0))

    def _browse_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Select video files",
            filetypes=[("Video Files", "*.mp4"), ("All Files", "*.*")]
        )
        existing = set(self.listbox.get(0, tk.END))
        for path in file_paths:
            if path not in existing:
                self.listbox.insert(tk.END, path)

    def _remove_selected(self):
        for index in reversed(self.listbox.curselection()):
            self.listbox.delete(index)

    def _on_submit(self):
        self.video_file_paths = list(self.listbox.get(0, tk.END))
        self.root.destroy()

    def get_lesson_file_selection(self) -> LessonFileSelection:
        self.root.mainloop()
        return LessonFileSelection(
            video_file_paths=self.video_file_paths,
        )
