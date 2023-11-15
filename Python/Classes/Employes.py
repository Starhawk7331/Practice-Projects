class employees:
    def __init__(
        self,
        first_name,
        last_name,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name + "@company.com"


Emp_1 = employees("Daniel", "Kaiser")
Emp_2 = employees("David", "Kaiser")

print(Emp_1.email)
print(Emp_2.email)
