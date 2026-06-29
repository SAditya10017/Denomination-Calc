import tkinter as tk

pounds = [200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
rupees = [2000,1000,500,200,100,50,20,10,5,2,1]
dollars = [500,200,100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]
yen = [5000,2000,1000,500,200,100,50,20,10,1]

def calculate_denominations():

    amount=int(entry_amount.get())
    if amount<=0:
        print("This amount is invalid to denominate")
    currency = input("What currency do you use?(Rupees, Dollars, Pounds, Yen): ").lower()
    denominations=[currency]
    result_text.delete("1.0",tk.END)

    for part in denominations:
        count=amount//part
        if count>0:
            result_text.insert(tk.END,f"{count} x {part}\n")
            amount%=part

window=tk.Tk()

window.title("Denomination of Money")
window.geometry("300x400")

tk.Label(window,text="Denomination of your Money").pack(pady=10)
tk.Label(window,text="Enter the amount: ").pack()

entry_amount=tk.Entry(window,justify="center")
entry_amount.pack(pady=5)

tk.Button(window,text="Split into Denominations",command=calculate_denominations).pack(pady=10)

result_text=tk.Text(window,height=12,width=30)
result_text.pack(pady=10)

window.mainloop()