import unittest
import data.client_dto

class Test_DTO_Object(unittest.TestCase):
    
    def test_create_and_string(self):
        
        clients = data.client_dto.ClientData()
        self.assertIsNotNone(clients)

        print(clients)

    def test_create_and_Data(self):
            
        clients = data.client_dto.ClientData()
        clients.set_filenames("some string")
        clients.set_file_sizes("some string 2")


if __name__ == '__main__':
    unittest.main()
