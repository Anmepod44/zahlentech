import redis
import json

class Feature:
    def __init__(self, name, desc, image, cta):
        self.name = name
        self.desc = desc
        self.image = image
        self.cta = cta

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "image": self.image,
            "cta": self.cta
        }

class Product:
    def __init__(self, name, image, description, features=None):
        self.name = name
        self.image = image
        self.description = description
        self.features = features if features is not None else []

    def to_dict(self):
        return {
            "name": self.name,
            "image": self.image,
            "description": self.description,
            "features": [feature.to_dict() for feature in self.features]
        }

class Package:
    def __init__(self, name, image, products=None):
        self.name = name
        self.image = image
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def to_dict(self):
        return {
            "name": self.name,
            "image": self.image,
            "products": [product.to_dict() for product in self.products]
        }

    @classmethod
    def from_dict(cls, data):
        products = [Product(product["name"], product["image"], product["description"],
                            [Feature(feature["name"], feature["desc"], feature["image"], feature["cta"]) 
                             for feature in product["features"]]) 
                    for product in data["products"]]
        return cls(data["name"], data["image"], products)

    @classmethod
    def get_all_packages(cls, redis_client):
        cursor, keys = redis_client.scan(match="package:*")
        packages = []
        for key in keys:
            package_data = redis_client.get(key)
            packages.append(cls.from_dict(json.loads(package_data)))
        return packages
    
    def __repr__(self):
        return f"Package(name={self.name}, image={self.image}, products={[i.name for i in self.products]})"
