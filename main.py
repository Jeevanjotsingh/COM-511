import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
import datetime


class FileManager:
    @staticmethod
    def read_data(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return {}

    @staticmethod
    def write_data(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


class User:
    def __init__(self, bank, username, password, phone_number):
        self.bank = bank
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.balance = 0
        self.transaction_history = []

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transaction_history.append(transaction)

    def add_transaction_admin(transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        User.transaction_history.append(transaction)

    def deposit(self, current_role):
        def deposit_amount(amount):
            if amount <= self.balance:
                self.balance += amount
                self.bank.users[self.username]["balance"] = self.balance
                self.bank.save_data()
                messagebox.showinfo("Deposit Successful",
                                    f"Deposited {amount} successfully.")
                User.add_transaction(self, "Deposit", amount)
            else:
                messagebox.showinfo("Deposit Unsuccessful",
                                    "Insufficient balance.")

        def get_deposit_amount(self, current_role):
            amount = simpledialog.askinteger(
                "Deposit Amount", "Enter deposit amount:")
            if amount is not None:
                if current_role == "admin":
                    if amount <= 300000:
                        self.deposit_amount(amount)
                    else:
                        messagebox.showinfo(
                            "Limit Exceeded", "Deposit limit exceeded for admin.")
                elif current_role == "user":
                    if amount <= 100000:
                        self.deposit_amount(amount)
                    else:
                        messagebox.showinfo(
                            "Limit Exceeded", "Deposit limit exceeded for user.")
                else:
                    messagebox.showinfo(
                        "Invalid Role", "Invalid role specified.")

        get_deposit_amount(current_role)

    def withdraw_admin(bank, com_user_admin_window):
        def withdraw_amount(amount, user):
            current = user["balance"]
            if amount <= current and current - amount >= 5000:
                current -= amount
                bank.users[username]["balance"] = current
                bank.save_data()
                messagebox.showinfo("Withdrawal Successful",
                                    f"Withdrew {amount} successfully.")
                User.add_transaction_admin("Withdraw", amount)
            else:
                messagebox.showinfo("Insufficient Balance",
                                    "Insufficient balance.")

        def get_withdrawal_amount(user):
            amount = simpledialog.askinteger(
                "Withdrawal Amount", "Enter withdrawal amount:")
            if amount is not None:
                if amount <= 300000:
                    withdraw_amount(amount, user)
                else:
                    messagebox.showinfo(
                        "Limit Exceeded", "Withdrawal limit exceeded for admin.")

        username = simpledialog.askstring(parent=com_user_admin_window,
                                          title="Withdraw Amount",
                                          prompt="Enter username:")

        if username in bank.users:
            user = bank.users[username]
            get_withdrawal_amount(user)
        else:
            messagebox.showerror("Cash Withdraw", "User not found")

    def withdraw_user(self):
        amount = simpledialog.askinteger(
            "Withdraw Amount", "Enter the amount:")
        if amount is not None:
            if amount <= 50000 and self.balance - amount >= 5000:
                self.balance -= amount
                self.bank.users[self.username]["balance"] = self.balance
                self.bank.save_data()
                messagebox.showinfo(
                    "Cash Withdraw", f"Withdrew ${amount} successfully.")
                User.add_transaction(self, "Withdraw", amount)
            else:
                messagebox.showerror(
                    "Cash Withdraw", "Insufficient balance or exceeded limit")

    def deposit_admin(bank, com_user_admin_window):
        def deposit_amount(amount, user):
            current = user["balance"]
            if amount <= 300000:
                current += amount
                bank.users[username]["balance"] = current
                bank.save_data()
                messagebox.showinfo("Deposit Successful",
                                    f"Deposited ${amount} successfully.")
                User.add_transaction_admin("Deposit", amount)
            else:
                messagebox.showinfo(
                    "Limit Exceeded", "Deposit limit exceeded for admin.")

        def get_deposit_amount(user):
            amount = simpledialog.askinteger(
                "Deposit Amount", "Enter deposit amount:")
            if amount is not None:
                deposit_amount(amount, user)

        username = simpledialog.askstring(parent=com_user_admin_window,
                                          title="Deposit",
                                          prompt="Enter username:")

        if username in bank.users:
            user = bank.users[username]
            get_deposit_amount(user)
        else:
            messagebox.showerror("Cash Deposit", "User not found")

    def show_trans(self):
        messagebox.showinfo(
            "Transaction", f"Transaction_historty:{self.transaction_history}")

    def deposit_user(self):
        amount = simpledialog.askinteger("Deposit Amount", "Enter the amount:")
        if amount is not None:
            if amount <= 100000:
                self.balance += amount
                self.bank.users[self.username]["balance"] = self.balance
                self.bank.save_data()
                messagebox.showinfo(
                    "Cash Deposit", f"Deposited ${amount} successfully.")
            else:
                messagebox.showerror("Cash Deposit", "Deposit limit exceeded")

    def check_balance(self):
        messagebox.showinfo(
            "Balance", f"Your Total Balance is : ${self.balance}")


class Bank:
    def __init__(self):
        self.users_file = "users.json"
        self.admin_file = "admin.json"
        self.users = FileManager.read_data(self.users_file)
        self.admin = FileManager.read_data(
            self.admin_file)
        self.login_attempts = {}
        self.admin_credentials = {"admin": "admin", "password": "password"}

    def delete_user_account(self):
        username = simpledialog.askstring("Delete Account", "Enter username:")
        if username in self.users:
            del self.users[username]
            self.save_data()
            messagebox.showinfo(
                title="Delete Account", message=f"User '{username}' account deleted successfully.")
        else:
            messagebox.showerror("Delete Account", "Username not found")

    def get_total_balance(self):
        total_balance = sum(user["balance"] for user in self.users.values())
        if total_balance < 75000:
            messagebox.showinfo(
                title="Total Balance", message=f"Total balance is less than $75,000.\nCurrent Total Balance: ${total_balance}")
        else:
            messagebox.showinfo(
                title="Total Balance", message=f"Total Balance: ${total_balance}")

    def save_data(self):
        FileManager.write_data(self.users_file, self.users)
        FileManager.write_data(self.admin_file, self.admin)

    def login(self, username, password, role):
        if role == "user" and username in self.users:
            if self.login_attempts.get(username, 0) >= 3:
                messagebox.showwarning("Login",
                                       f"Account for user '{username}' is locked. Contact admin for assistance.")
                return False
            elif self.users[username]["password"] == password:
                self.login_attempts.pop(username, None)
                return True
            else:
                self.login_attempts[username] = self.login_attempts.get(
                    username, 0) + 1
                messagebox.showwarning("Login",
                                       "Incorrect password. Please try again.")
                if self.login_attempts[username] == 3:
                    messagebox.showwarning("Login",
                                           f"Too many unsuccessful login attempts for user '{username}'. Contact admin.")
                return False
        elif role == "admin" and username == self.admin_credentials["admin"] and password == self.admin_credentials["password"]:
            return True
        else:
            return False

    def register_user(self):
        username = simpledialog.askstring(
            "New User Registration", "Enter username:")
        password = simpledialog.askstring(
            "New User Registration", "Enter password:")
        phone_number = simpledialog.askstring(
            "New User Registration", "Enter phone number:")

        if username and password and phone_number:
            if username not in self.users:
                self.users[username] = {"password": password,
                                        "phone_number": phone_number, "balance": 5000}
                self.save_data()
                messagebox.showinfo("Registration Successful",
                                    "User registered successfully.")
            else:
                messagebox.showerror(
                    "Register user", "Username already exists. Please choose another.")
        else:
            messagebox.showerror(
                "Register user", "Username already exists. Please choose another.")
            return False

    def reset_password(self):
        username = simpledialog.askstring("Password Reset", "Enter username:")
        if username in self.users:
            new_password = simpledialog.askstring(
                "Password Reset", "Enter new password:")
            self.users[username]["password"] = new_password
            self.login_attempts.pop(username, None)
            self.save_data()
            return True
        else:
            messagebox.showerror("Password reset", "Username not found")
            return False

    def change_password(self):
        username = simpledialog.askstring(
            "Change password", "Enter username:")
        current_password = simpledialog.askstring(
            "Change password", "Enter current password:")
        new_password = simpledialog.askstring(
            "Change password", "Enter new password:")
        if username in self.users and self.users[username]["password"] == current_password:
            self.users[username]["password"] = new_password
            self.login_attempts.pop(username, None)
            self.save_data()
            messagebox.showinfo("Change Password",
                                "Password Changed successfully")
        else:
            messagebox.showerror(
                "Change password", "Invalid username or current password. Password change failed.")


def main():
    bank = Bank()

    def show_user_login(id, user_login_window):
        user_data = bank.users[id]
        user = User(bank, id, user_data["password"], user_data["phone_number"])
        user.balance = user_data["balance"]

        def go_back():
            bank.save_data
            com_user_login_window.destroy()
            main_window.deiconify()
        user_login_window.withdraw()
        com_user_login_window = tk.Toplevel(main_window)
        # Maximizes the window on most systems
        com_user_login_window.attributes('-fullscreen', True)
        com_user_login_window.title("User Login")

        label = tk.Label(com_user_login_window,
                         text='*USER*', font=("Arial", 20))
        deposit_button = tk.Button(com_user_login_window, text='Cash Deposit', font=(
            "Arial", 14), command=lambda: user.deposit_user())
        withdraw_button = tk.Button(com_user_login_window, text='Cash Withdraw', font=(
            "Arial", 14), command=lambda: user.withdraw_user())
        transaction_button = tk.Button(com_user_login_window, text='Transaction History', font=(
            "Arial", 14), command=user.show_trans)
        check_balance_button = tk.Button(com_user_login_window, text='Check Balance', font=(
            "Arial", 14), command=user.check_balance)
        change_password_button = tk.Button(com_user_login_window, text='Change Password', font=(
            "Arial", 14), command=bank.change_password)
        logout_button = tk.Button(
            com_user_login_window, text='Logout', font=("Arial", 14), command=go_back)
        label.grid(row=0, column=0, padx=800, pady=10)
        deposit_button.grid(row=1, column=0, padx=800, pady=30)
        withdraw_button.grid(row=2, column=0, padx=800, pady=30)
        transaction_button.grid(row=3, column=0, padx=800, pady=30)
        check_balance_button.grid(row=4, column=0, padx=800, pady=30)
        change_password_button.grid(row=5, column=0, padx=800, pady=30)
        logout_button.grid(row=6, column=0, padx=800, pady=30)

    def show_admin_login(admin_login_window):
        def go_back():
            bank.save_data
            com_admin_login_window.destroy()
            main_window.deiconify()
        admin_login_window.withdraw()
        com_admin_login_window = tk.Toplevel(main_window)
        com_admin_login_window.attributes('-fullscreen', True)
        com_admin_login_window.title("Admin Login")
        label = tk.Label(com_admin_login_window,
                         text='*ADMIN*', font=("Arial", 25))
        totalbal_button = tk.Button(com_admin_login_window, text='Total Balance', font=(
            "Arial", 14), command=bank.get_total_balance)
        cashwd_button = tk.Button(com_admin_login_window, text='User Cash Withdraw', font=(
            "Arial", 14),  command=lambda: User.withdraw_admin(bank, com_admin_login_window))
        cashdepo_button = tk.Button(com_admin_login_window, text='User Cash Deposit', font=(
            "Arial", 14), command=lambda: User.deposit_admin(bank, com_admin_login_window))
        check_balance_button = tk.Button(com_admin_login_window, text='Register New User', font=(
            "Arial", 14), command=bank.register_user)
        reset_button = tk.Button(com_admin_login_window, text='Reset Password', font=(
            "Arial", 14), command=bank.reset_password)
        deluser_button = tk.Button(com_admin_login_window, text='Delete user account', font=(
            "Arial", 14), command=bank.delete_user_account)
        back_button = tk.Button(
            com_admin_login_window, text='Logout', font=("Arial", 14), command=go_back)
        label.grid(row=0, column=0, padx=800, pady=10)
        totalbal_button.grid(row=1, column=0, padx=800, pady=30)
        cashwd_button.grid(row=2, column=0, padx=800, pady=30)
        cashdepo_button.grid(row=3, column=0, padx=800, pady=30)
        check_balance_button.grid(row=4, column=0, padx=800, pady=30)
        reset_button.grid(row=5, column=0, padx=800, pady=30)
        deluser_button.grid(row=6, column=0, padx=800, pady=30)
        back_button.grid(row=7, column=0, padx=800, pady=30)

    def user_check():
        def check():
            user_entry_val = user_entry.get()
            user_pass_entry_val = user_pass_entry.get()
            val = bank.login(user_entry_val, user_pass_entry_val, "user")
            if (val):
                show_user_login(user_entry_val, user_login_window)
            else:
                user_login_window.destroy()
                main_window.deiconify()
        main_window.withdraw()
        user_login_window = tk.Toplevel(main_window)
        user_login_window.attributes('-fullscreen', True)
        user_login_window.title("User Login",)
        empty_label = tk.Label(user_login_window)
        empty_label.pack(padx=750, pady=200)
        user = tk.Label(user_login_window, text="User id:")
        user.pack(padx=750, pady=5)
        user_entry = tk.Entry(user_login_window, font=("Arial", 16))
        user_entry.pack(padx=750, pady=5)
        user_pass = tk.Label(user_login_window, text="Password:")
        user_pass.pack(padx=750, pady=5)
        user_pass_entry = tk.Entry(
            user_login_window, font=("Arial", 16), show="*")
        user_pass_entry.pack(padx=750, pady=5)

        confirm_button = tk.Button(
            user_login_window, text="Confirm", font=("Arial", 16), command=check)
        confirm_button.pack(padx=10, pady=5)

    def admin_check():
        def check():
            admin_entry_val = admin_entry.get()
            admin_pass_entry_val = admin_pass_entry.get()

            val = bank.login(admin_entry_val, admin_pass_entry_val, "admin")

            if val:
                show_admin_login(admin_login_window)
            else:
                admin_login_window.destroy()
                main_window.deiconify()
        main_window.withdraw()
        admin_login_window = tk.Toplevel(main_window)
        admin_login_window.attributes('-fullscreen', True)
        admin_login_window.title("Admin Login")
        empty_label = tk.Label(admin_login_window)
        empty_label.pack(padx=750, pady=200)
        admin = tk.Label(admin_login_window, text="User id:")
        admin.pack(padx=750, pady=5)
        admin_entry = tk.Entry(admin_login_window, font=("Arial", 16))
        admin_entry.pack(padx=750, pady=5)
        admin_pass = tk.Label(admin_login_window, text="Password:")
        admin_pass.pack(padx=750, pady=10)
        admin_pass_entry = tk.Entry(
            admin_login_window, font=("Arial", 16), show="*")
        admin_pass_entry.pack(padx=750, pady=5)

        confirm_button = tk.Button(
            admin_login_window, text="Confirm", font=("Arial", 16), command=check)
        confirm_button.pack(padx=750, pady=5)
    main_window = tk.Tk()
    main_window.title("Bank System")
    main_window.attributes('-fullscreen', True)

    window_width = 600
    window_height = 700

    center_window(main_window, window_width, window_height)
    label = tk.Label(
        main_window, text='***Welcome to the ATM***', font=("Arial", 25))
    label.pack(padx=10, pady=70)

    user_button = tk.Button(main_window, text="User Login",
                            command=user_check, font=("Arial", 14))
    user_button.pack(padx=10, pady=50)

    admin_button = tk.Button(
        main_window, text="Admin Login", command=admin_check, font=("Arial", 14))
    admin_button.pack(padx=10, pady=50)

    exit_button = tk.Button(main_window, text="Exit",
                            command=main_window.destroy, font=("Arial", 14))
    exit_button.pack(padx=10, pady=50)

    main_window.mainloop()


if __name__ == "__main__":
    main()
