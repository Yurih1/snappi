from app.repositories.category import CategoryRepository
from app.utils.exceptions import GenericExceptions


class CategoryService:
    """
        class responsible for managing category business rules
    """

    def get_categories(self) -> dict:

        #TODO add validate credentials
        
        result = {}

        return result
    
    def get_category_by_id(self, id: str) -> dict:

        #TODO add validate id in bd
        #TODO add validate credentials

        if not id:
            GenericExceptions(status_code=404, message="Not found.").generic_http_exception()

        result = {}

        return result
    
    def put_category(self, data: dict) -> str: 

        #TODO add validate id in bd
        #TODO add validate credentials

        result = 1

        return result
    
    def delete_category(self, id: str) -> str:

        #TODO add validate id in bd
        #TODO add validate credentials

        result = 1

        return result
