# Import the Add function, and assert that it works correctly.
from app import Add

def Tester():
        assert Add(2,3) == 5
        print("Testing Functions inside app completed successfully")

if __name__ == '__main__':
        Tester()