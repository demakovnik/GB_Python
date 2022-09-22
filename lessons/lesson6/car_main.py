import Car

if __name__ == "__main__":
    townCar = Car.TownCar(100, "red", "toyota")
    townCar.go()
    townCar.stop()
    townCar.turn("right")
    townCar.show_speed()

    workCar = Car.WorkCar(60, "yellow", "Komazu")
    workCar.go()
    workCar.stop()
    workCar.turn("left")
    workCar.show_speed()

    sportCar = Car.SportCar(150, "green", "BMW")
    sportCar.go()
    sportCar.stop()
    sportCar.turn("left")
    sportCar.show_speed()

    policeCar = Car.PoliceCar(160, "black", "Subaru")
    policeCar.go()
    policeCar.stop()
    policeCar.turn("left")
    policeCar.show_speed()


