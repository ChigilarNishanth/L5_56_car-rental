"""
Car Rental System Module.

Provides core functionality for managing vehicle inventory, processing
rentals, authenticating administrator credentials, and calculating payments.
"""

import os


class CarRentalSystem:
    """Manages car inventory, rental processing, and administrative access."""

    def __init__(self, fleet=None):
        """Initialize the car rental system with an optional fleet list."""
        if fleet is None:
            self.fleet = []
        else:
            self.fleet = fleet

    def add_car(self, car_id, model, rate_per_day):
        """Add a new car to the rental fleet."""
        car = {
            "id": car_id,
            "model": model,
            "rate": rate_per_day,
            "available": True,
        }
        self.fleet.append(car)

    def calculate_discount(self, discount_rate, days):
        """Calculate total discount safely using numeric inputs."""
        if discount_rate < 0 or days < 0:
            raise ValueError("Discount rate and days must be non-negative.")
        return discount_rate * days

    def rent_car(self, car_id, days):
        """Rent a vehicle from the fleet for a specific duration."""
        if days <= 0:
            raise ValueError("Days must be greater than zero.")

        for car in self.fleet:
            if car["id"] == car_id:
                if car["available"]:
                    car["available"] = False
                    return car["rate"] * days
                print("Car is already rented!")
                return None
        return None

    def authenticate_admin(self, password):
        """Authenticate administrative access against environment configuration."""
        admin_password = os.getenv("ADMIN_PASSWORD", "DefaultSecurePass123!")
        return password == admin_password

    def process_payment(self, amount):
        """Calculate rental payment including standard tax."""
        try:
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            return amount * 1.18
        except (TypeError, ValueError) as err:
            print(f"Error processing payment: {err}")
            return None


def main():
    """Execute main application entry point."""
    system = CarRentalSystem()
    system.add_car(1, "Toyota Sedan", 50)
    system.add_car(2, "SUV Extra", 80)

    print("Welcome to Car Rental System")
    system.rent_car(1, 3)
    system.calculate_discount(5.0, 3)


if __name__ == "__main__":
    main()