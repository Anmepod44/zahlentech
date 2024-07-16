import redis
from models import *
import json

class PackageController:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def create_package(self, package):
        key = f"package:{package.name}"
        value = json.dumps(package.to_dict())
        self.redis_client.set(key, value)

    def read_package(self, package_name):
        key = f"package:{package_name}"
        package_data = self.redis_client.get(key)
        if package_data:
            return Package.from_dict(json.loads(package_data))
        return None

    def update_package(self, package_name, updated_package):
        key = f"package:{package_name}"
        if self.redis_client.exists(key):
            value = json.dumps(updated_package.to_dict())
            self.redis_client.set(key, value)
            return True
        return False

    def delete_package(self, package_name):
        key = f"package:{package_name}"
        if self.redis_client.exists(key):
            self.redis_client.delete(key)
            return True
        return False

    def get_all_packages(self):
        return Package.get_all_packages(self.redis_client)

# Example usage
if __name__ == "__main__":
    redis_client = redis.Redis(
        host='localhost'
    )

    controller = PackageController(redis_client)

    # Create a package
    feature1 = Feature("Feature 1", "Description 1", "image1.png", "cta1")
    feature2 = Feature("Feature 2", "Description 2", "image2.png", "cta2")
    product1 = Product("Zoho Books", "zoho.png", "Accounting software", [feature1, feature2])
    package = Package("bronze", "bronze.png", [product1])
    controller.create_package(package)

    # Read a package
    retrieved_package = controller.read_package("bronze")
    print(retrieved_package)

    # Update a package
    feature3 = Feature("Feature 3", "Description 3", "image3.png", "cta3")
    product2 = Product("Sage 50", "sage.png", "Accounting software", [feature3])
    updated_package = Package("bronze", "bronze.png", [product1, product2])
    controller.update_package("bronze", updated_package)

    # Delete a package
    controller.delete_package("bronze")

    # Get all packages
    all_packages = controller.get_all_packages()
    for pkg in all_packages:
        print(pkg)
