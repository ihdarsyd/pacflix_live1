
#  pip install tabulate
from tabulate import tabulate

class User:

    # data user: username, current_plan, duration, kode_referal
    data = {
        1: ["Rosy", "Basic Plan", 13, "rosy-123"],
        2: ["Ana", "Standard Plan", 8, "ana-123"],
        3: ["Agus", "Premium Plan", 4, "agus-123"],
        4: ["Budi", "Basic Plan", 10, "budi-123"]
    }

    # data plan dan benefit
    header_benefit = ["Basic Plan","Standard Plan", "Premium Plan", "Services"]
    table_benefit = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]
    

    def __init__(self):
        self.username = None
        self.duration_plan = None
        self.current_plan = None
        self.kode_referal = None

    def login(self, username):
        """
        Fungsi untuk melakukan login

        input: 
        - username: str
        return: -
        """
        self.username = username
        
        # pengecekan apakah user yang melakukan login itu ada pada data user pacflix
        for key,value in self.data.items():
            if value[0] == username:
                self.duration_plan = value[2]
                self.current_plan = value[1]
                self.kode_referal = value[3]
                break
            else:
                self.duration_plan = None
                self.current_plan = None
                self.kode_referal = None

    def check_benefit(self):
        """
        Fungsi untu menampilkan list plan dan benefit dari Pacflix

        input: -
        output: print
        return: -
        """

        print("Pacflix Plan List")
        print("")
        print(tabulate(self.table_benefit, self.header_benefit))

    def check_plan(self):
        """
        Fungsi untuk menampilkan current plan dari current user (user yang melakukan login)

        input: - 
        return: -
        """
        print(f"User {self.username} sedang berlangganan:")

        if(self.current_plan in self.header_benefit[0:3]):
            if self.current_plan == "Basic Plan":
                idx_current = 0
            elif self.current_plan == "Standard Plan":
                idx_current = 1
            elif self.current_plan == "Premium Plan":
                idx_current = 2
            
            table_data = [[row[idx_current],row[-1]] for row in self.table_benefit]
            header = [self.header_benefit[idx_current],self.header_benefit[-1]]
            print(tabulate(table_data,header))
        else:
            raise Exception("Data plan tidak ada")
            
