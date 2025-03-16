#Driver Program to potentially create multiple characters quickly.
#written courtesy of ChatGPT3.5
#corrected and adapted by Ken Smith 4/13/24
import json
import CharacterPDFMaker
import CharacterFromJSONtoPDF

def create_character():
    creation_method = input("Enter 'json' to create character from JSON string, or 'manual' for manual inputs: ").strip().lower()
    
    if creation_method == 'json':
        json_string = input("Enter JSON string for character: ")
        try:
            CharacterFromJSONtoPDF.create_from_json(json_string)
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            
    elif creation_method == 'manual':
        CharacterPDFMaker.create_from_input()
        
    else:
        print("Invalid input. Please enter 'json' or 'manual'.")

def main():
    while True:
        try:
            create_character()
            choice = input("Do you want to create another character? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Exiting program.")
                break
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
