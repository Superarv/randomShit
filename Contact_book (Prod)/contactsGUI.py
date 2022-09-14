from tkinter import *
import os

root = Tk()
location = os.path.expanduser("~/Coding/Python/Projects/contact_book/test.txt")



def contacts_listFN():
    list = Tk()
    list.configure(bg="black")
    list.geometry("700x500")
    list.title("List Of Contacts")
    list.resizable(False, False)
    list.attributes('-topmost', 1)
    scrollbar = Scrollbar(list)
    scrollbar.pack(side=RIGHT, fill=Y)
    exitBTN = Button(list, text="Exit", font=("Arial", 35), command=list.destroy)
    exitBTN.pack()
    t = Text(list, width = 15, height = 15, wrap = NONE, yscrollcommand = scrollbar.set, bg="black")
    with open(location, 'r') as f:
        Lines = f.readlines()
        for x in Lines:
            t.insert(END, x + '\n')
    t.pack(side=TOP, fill=X)

def add_contactFN():
        
    add = Tk()
    add.geometry("700x500")
    add.title("Add A Contact")
    add.resizable(False, False)
    add.attributes('-topmost', 1)
    name_prompt = Label(add, text="Enter the person's full name:", font=("Arial", 30))
    name_prompt.place(x=10, y=30, anchor="w")
    nameENT = Entry(add, font=('Arial', 30))
    nameENT.place(x=15, y=60)
    number_prompt = Label(add, text="Enter the person's phone number:", font=("Arial", 30))
    number_prompt.place(x=10, y=120, anchor="w")
    numberENT = Entry(add, font=('Arial', 30))
    numberENT.place(x=15, y=150)
    company_prompt = Label(add, text="Enter the person's company:", font=("Arial", 30))
    company_prompt.place(x=10, y=210, anchor="w")
    companyENT = Entry(add, font=('Arial', 30))
    companyENT.place(x=15, y=240)
    def submit():
        name = nameENT.get()
        number = numberENT.get()
        company = companyENT.get()
        global contact
        contact = f"{name} {number} {company}"
        print(contact)
        with open(location, "a") as fh:
            fh.write(contact + "\n")
            fh.close()
            add.destroy()

    submitBTN = Button(add, text="Submit", command = submit, font=("Arial", 35))
    submitBTN.place(x=350, y=350,anchor="center")
    exitBTN = Button(add, text="Exit", command = add.destroy, font=("Arial", 35))
    exitBTN.place(x=350, y=450,anchor="center")

def search_contactFN():
    search = Tk()
    search.geometry("700x500")
    search.title("Search For A Contact")
    search.resizable(False, False)
    search.attributes('-topmost', 1)
    input_bar = Entry(search, font=('Arial', 30))
    input_bar.place(x=350, y=100, anchor="center")
    Results = Text(search, width = 45, height = 15, wrap = NONE, bg="black", fg="white")
    Results.place(x=350, y=350, anchor="center")
    Results.insert(INSERT, "No Results Found")
    
    def search_fn():
        user = input_bar.get()
        with open(location, 'r') as f:
            contacts = f.readlines()
    
    
 
        if any(user in word for word in contacts):
            matches = [match for match in contacts if user in match]
            with open(location, 'r') as f:
                for x in matches:
                    Results.delete(1.0, END)
                    Results.insert(END, x + '\n')
                    

        
        else:
            Results.insert("No Results Found (2)")
    
    submitBTN2 = Button(search, text="Search", font=('Arial', 30), command = search_fn)
    submitBTN2.place(x=350, y=175, anchor="center")
    exitBTN = Button(search, text="Exit", font=('Arial', 30), command = search.destroy)
    exitBTN.place(x=350, y=225, anchor="center")
    


root.geometry("700x500")
root.title("Contact Book w/ GUI")
root.resizable(False, False)
root.attributes('-topmost', 1)
title = Label(root,text="Contacts Book",font=("Arial", 35))
title.place(x=350, y=25, anchor="center")
read_all = Button(root, text="Read All",font=("Arial", 35), command=contacts_listFN)
read_all.place(x=233, y=100, anchor="center")
add_contact = Button(root, text="Add Contact",font=("Arial", 35), command=add_contactFN)
add_contact.place(x=466, y=100, anchor="center")
search_btn = Button(root, text="Search Contact",font=("Arial", 35), command = search_contactFN)
search_btn.place(x=233, y=200, anchor="center")
exit_btn = Button(root, text="Exit App",font=("Arial", 35), command = root.destroy)
exit_btn.place(x=466, y=200, anchor="center")





root.mainloop()