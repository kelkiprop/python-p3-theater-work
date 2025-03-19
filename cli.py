from database import get_session
from models import Role, Audition  
def main():
    session = get_session()
    
    while True:
        print("\nMoringa Theater CLI")
        print("1. Add Role")
        print("2. Add Audition")
        print("3. View Roles")
        print("4. View Auditions")
        print("5. Call Back Actor")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            character_name = input("Enter role name: ")
            role = Role(character_name=character_name)
            session.add(role)
            session.commit()
            print("Role added successfully!")

        elif choice == "2":
            actor = input("Enter actor name: ")
            location = input("Enter audition location: ")
            phone = int(input("Enter actor phone number: "))
            role_id = int(input("Enter role ID: "))
            audition = Audition(actor=actor, location=location, phone=phone, role_id=role_id)
            session.add(audition)
            session.commit()
            print("Audition added successfully!")

        elif choice == "3":
            roles = session.query(Role).all()
            for role in roles:
                print(role)

        elif choice == "4":
            auditions = session.query(Audition).all()
            for audition in auditions:
                print(audition)

        elif choice == "5":
            audition_id = int(input("Enter audition ID to call back: "))
            audition = session.query(Audition).get(audition_id)
            if audition:
                audition.call_back()
                session.commit()
                print("Actor called back successfully!")
            else:
                print("Audition not found!")

        elif choice == "6":
            print("Exiting CLI...")
            break

        else:
            print("Invalid option, please try again!")

if __name__ == "__main__":
    main()
