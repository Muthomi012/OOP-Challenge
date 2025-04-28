from pet import Pet

def main():
    # Create a Pet object
    my_pet = Pet("Buddy")

    # Test different behaviors
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
