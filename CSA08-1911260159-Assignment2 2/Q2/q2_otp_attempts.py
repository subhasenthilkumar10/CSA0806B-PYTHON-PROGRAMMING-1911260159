# Q2 - OTP verification using while and for loops

CORRECT_OTP = "246810"


def check_otp_while():
    print("\nWHILE LOOP")
    attempts = 0

    while attempts < 3:
        entered = input("Enter OTP (blank to skip): ").strip()

        if entered == "":
            print("Blank entry - not counted.")
            continue

        attempts += 1
        if entered == CORRECT_OTP:
            print("OTP accepted.")
            break
        else:
            print("Wrong OTP. Attempts used:", attempts)
    else:
        print("Account locked for 30 minutes.")


def check_otp_for():
    print("\nFOR LOOP")
    for attempt in range(1, 4):
        # Keep asking until a non-blank entry is received.
        entered = ""
        while entered == "":
            entered = input("Enter OTP (blank to skip): ").strip()
            if entered == "":
                print("Blank entry - not counted.")

        if entered == CORRECT_OTP:
            print("OTP accepted.")
            break
        print("Wrong OTP. Attempts used:", attempt)
    else:
        print("Account locked for 30 minutes.")


def extra_attempts_allowed(security_answer_correct):
    allowed_attempts = 5 if security_answer_correct else 3
    print("\nChanged condition: allowed attempts =", allowed_attempts)
    # pass is a placeholder: no extra action is needed when the answer is correct.
    if security_answer_correct:
        pass
    for attempt in range(1, allowed_attempts + 1):
        print("Attempt number:", attempt)


if __name__ == "__main__":
    print("For a quick test, use OTP 246810.")
    # Run one version at a time by removing the comment from the call.
    check_otp_while()
    # check_otp_for()
    extra_attempts_allowed(True)
