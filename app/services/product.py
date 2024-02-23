from app.repositories.product import ProductRepository
from app.utils.exceptions import GenericExceptions


class ProductService:
    """
        class responsible for managing product business rules
    """

    def get_products(self) -> dict:

        #TODO add validate credentials
        
        result = {}

        return result
    
    def get_product_by_id(self, id: str) -> dict:

        #TODO add validate id in bd
        #TODO add validate credentials

        if not id:
            GenericExceptions(status_code=404, message="Not found.").generic_http_exception()

        result = {}

        return result
    
    def put_product(self, data: dict) -> str: 

        #TODO add validate id in bd
        #TODO add validate credentials

        result = 1

        return result
    
    def delete_product(self, id: str) -> str:

        #TODO add validate id in bd
        #TODO add validate credentials

        result = 1

        return result
