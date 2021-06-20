
C = 299792458


def main():
    # Loop forever
    while True:
        # Read the mass in from the user.
        mass_in_kg = float(input("Enter kilos of mass: "))

        # Calculate energy
        energy_in_joules = mass_in_kg * C * C

        # Display work to the user
        print("E = m * C^2 ...")
        print("m = " + str(mass_in_kg) + " kg")
        print("C = " + str(C) + "m/s")
        print(str(energy_in_joules) + " joules of energy!")
        print()


if __name__ == '__main__':
    main()
