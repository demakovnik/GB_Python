import Worker

if __name__ == "__main__":
    position = Worker.Position('Ivan', 'Ivanov', 'manager', {"wage": 1000, "bonus": 2000})

    print(position.get_full_name())
    print(position.get_total_income())
