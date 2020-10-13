import src.signup as signup
import src.signin as signin
# TODO - auto feed values into signup if user wants to sign up using data they entered during sign in prompt

if __name__ == "__main__":
    while True:
        response = signup.pyip.inputMenu(['sign up', 'sign in'])
        if response == 'sign up':
            signup.prompt()
        elif response == 'sign in':
            signin.prompt()

