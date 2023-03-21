import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI Calculator")
        self.root.configure(bg="green")
        
        # Create input and output text boxes
        self.input_box = tk.Entry(self.root, width=20)
        self.input_box.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        self.output_box = tk.Entry(self.root, width=20)
        self.output_box.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        
        button_cls = tk.Button(self.root, text="AC", width=4, height=2,command=self.clear,bg="red",fg='white')
        button_cls.grid(row=2, column=0, padx=5, pady=5)
        
        # Create buttons
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        for i in range(len(button_list)):
            button = tk.Button(self.root, text=button_list[i], width=4, height=2,bg="light blue",fg='Red')
            button.grid(row=i // 4 + 3, column=i % 4, padx=5, pady=5)
            button.bind("<Button-1>", self.button_press)
        
        # Bind keys to functions
        self.root.bind("<Return>", self.calculate)
        self.root.bind("<KP_Enter>", self.calculate)
        self.root.bind("<Escape>", lambda event: self.clear())
        self.root.bind("<Delete>", lambda event: self.clear())
        
        self.root.mainloop()
    
    def button_press(self, event):
        """Add clicked button's value to input box"""
        
        if event.widget["text"]=='=':
            self.calculate(event)
        else:
            self.input_box.insert(tk.END, event.widget["text"])
        
    def calculate(self, event):
        """Evaluate expression and display result"""
        try:
            result = eval(self.input_box.get())
            self.output_box.delete(0, tk.END)
            self.output_box.insert(0, str(result))
        except:
            self.output_box.delete(0, tk.END)
            self.output_box.insert(0, "Error")
    
    def clear(self):
        """Clear input and output boxes"""
        self.input_box.delete(0, tk.END)
        self.output_box.delete(0, tk.END)

# Create instance of calculator
calc = Calculator()
