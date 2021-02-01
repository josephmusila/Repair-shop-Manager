from tkinter import *
from db import Database
from tkinter import messagebox

db=Database('store.db')

app=Tk()

def populate_list():

    parts_list.delete(0,END)
    for row in db.fetch():
            parts_list.insert(END,row)

def add_item():
    if part_text.get()=='' or customer_text.get()=='' or retailer_text.get()=='' or price_text.get()=='':
        messagebox.showerror('Required fields','include all fields')
        return
    db.insert(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END,(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get()))
    clear_item()
    populate_list()


def select_item(event):
   try:
       global select_item
       index = parts_list.curselection()[0]
       select_item = parts_list.get(index)
       part_entry.delete(0, END)
       part_entry.insert(END, select_item[1])

       customer_entry.delete(0, END)
       customer_entry.insert(END, select_item[2])

       retailer_entry.delete(0, END)
       retailer_entry.insert(END, select_item[3])

       price_entry.delete(0, END)
       price_entry.insert(END, select_item[4])

   except IndexError:
        pass
def remove_item():
    db.remove(select_item[0])
    clear_item()
    populate_list()


def update_item():
    db.update(select_item[0],part_text.get(),customer_text.get(),retailer_text.get(),price_text.get())
    clear_item()
    populate_list()

def clear_item():
    part_entry.delete(0,END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

#part
part_text=StringVar()
part_label=Label(app,font=(14),text="Part Name",pady=20)
part_label.grid(row=0,column=0,sticky=W)
part_entry=Entry(app,text=part_text)
part_entry.grid(row=0,column=1)

#customer
customer_text=StringVar()
customer_label=Label(app,font=(14),text="Customer")
customer_label.grid(row=0,column=2,sticky=W)
customer_entry=Entry(app,text=customer_text)
customer_entry.grid(row=0,column=3)

#retailer
retailer_text=StringVar()
retailer_label=Label(app,font=(14),text="Retailer")
retailer_label.grid(row=1,column=0,sticky=W)
retailer_entry=Entry(app,text=retailer_text)
retailer_entry.grid(row=1,column=1)

#price
price_text=StringVar()
price_label=Label(app,font=(14),text="Price")
price_label.grid(row=1,column=2,sticky=W)
price_entry=Entry(app,text=price_text)
price_entry.grid(row=1,column=3)

#partsList

parts_list=Listbox(app,height=8,width=50)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=3,pady=20,padx=20)
#bind select

parts_list.bind('<<ListboxSelect>>',select_item)
#create scrooll bar

scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)
#set scroll to listbox

parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#buttons

add_btn=Button(app,text="Add Part",width=12,command=add_item)
add_btn.grid(row=2,column=0,pady=20)
#remove
remove_btn=Button(app,text="Remove Part",width=12,command=remove_item)
remove_btn.grid(row=2,column=1)
#update
update_btn=Button(app,text="Update Part",width=12,command=update_item)
update_btn.grid(row=2,column=2)
#clear
clear_btn=Button(app,text="Clear fields",width=12,command=clear_item)
clear_btn.grid(row=2,column=3)

app.title("part manager")
app.geometry('700x350')

#populate data

populate_list()



app.mainloop()