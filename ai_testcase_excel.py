import pandas as pd

def generate_test_cases(feature):
    test_cases = []

    if "login" in feature.lower():
        test_cases = [
            ["Login Page", "Valid Login", "Enter correct username & password", "User should login successfully"],
            ["Login Page", "Invalid Login", "Enter wrong password", "Error message should appear"],
            ["Login Page", "Empty Fields", "Leave fields blank", "Validation message should show"],
            ["Login Page", "Security Test", "SQL injection attempt", "System should block attack"],
        ]
    else:
        test_cases = [
            [feature, "Positive Test", "Valid input", "System should work correctly"],
            [feature, "Negative Test", "Invalid input", "System should show error"],
            [feature, "Edge Case", "Boundary values", "System should handle edge cases"],
        ]

    df = pd.DataFrame(test_cases, columns=[
        "Module", "Test Case", "Test Steps", "Expected Result"
    ])

    df.to_excel("test_cases.xlsx", index=False)

    print("Test cases generated successfully!")
    print("File saved as test_cases.xlsx")

feature = input("Enter feature: ")
generate_test_cases(feature)

