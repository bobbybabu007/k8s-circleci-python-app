# Import the Add function, and assert that it works correctly.
from app import Add

def Tester():
        assert Add(5,5) == 10
        print("Testing Functions inside app completed successfully")

if __name__ == '__main__':
        Tester()