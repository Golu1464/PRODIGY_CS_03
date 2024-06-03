def check_password_strength(password):
  """
  Evaluates the strength of a password based on various criteria.

  Args:
      password: The password to be checked.

  Returns:
      A tuple containing:
          - Strength score (integer)
          - Feedback message (string)
  """
  strength_score = 0
  feedback_message = ""

  # Check length
  if len(password) >= 12:
    strength_score += 2
    feedback_message += "Length is good (12+ characters).\n"
  elif len(password) >= 8:
    strength_score += 1
    feedback_message += "Length is decent (8-11 characters).\n"
  else:
    feedback_message += "Password is too short. Use at least 8 characters.\n"

  # Check character types
  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  has_number = any(char.isdigit() for char in password)
  has_special = any(not char.isalnum() for char in password)

  character_types = 0
  if has_uppercase:
    character_types += 1
  if has_lowercase:
    character_types += 1
  if has_number:
    character_types += 1
  if has_special:
    character_types += 1

  strength_score += character_types
  if character_types == 0:
    feedback_message += "Password needs a mix of uppercase, lowercase, numbers, and symbols.\n"
  elif character_types == 1:
    feedback_message += "Password could benefit from more character types.\n"
  elif character_types == 2:
    feedback_message += "Password has a good mix of character types.\n"
  else:
    feedback_message += "Excellent! Password uses a variety of character types.\n"

  # Overall Strength Rating
  if strength_score == 0:
    feedback_message += "Password is very weak. Please consider creating a stronger password.\n"
  elif strength_score <= 2:
    feedback_message += "Password is weak. Consider using a longer password and including more character types.\n"
  elif strength_score == 3:
    feedback_message += "Password is moderately strong. You can improve it further by adding more character types.\n"
  elif strength_score == 4:
    feedback_message += "Password is strong!\n"
  else:
    feedback_message += "Password is very strong!\n"

  return strength_score, feedback_message

# Get user input
password = input("Enter your password: ")

# Check password strength
strength_score, feedback_message = check_password_strength(password)

print(feedback_message)