import math
import string


def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26

    if any(c.isupper() for c in password):
        charset += 26

    if any(c.isdigit() for c in password):
        charset += 10

    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


def check_password_strength(password):

    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length to 8 or more")

    # Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Number
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special character
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Entropy
    entropy = calculate_entropy(password)

    # Rating
    if score >= 5 and entropy >= 60:
        rating = "Very Strong"
    elif score >= 4 and entropy >= 40:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {
        "password": password,
        "score": score,
        "entropy": entropy,
        "rating": rating,
        "feedback": feedback
    }


# Main program
if _name_ == "_main_":

    password = input("Enter a password: ")

    result = check_password_strength(password)

    print("\n--- Cybersecurity Password Analysis ---")
    print("Rating  :", result["rating"])
    print("Score   :", result["score"], "/ 6")
    print("Entropy :", round(result["entropy"], 2), "bits")

    print("\nFeedback:")

    if result["feedback"]:
        for item in result["feedback"]:
            print("-", item)
    else:
        print("- Password meets all requirements")