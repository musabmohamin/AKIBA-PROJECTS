while 1:
    password=input("ENTER PASSWORD")


    def minimum_length(minimum_length=8):
        if len(password)<minimum_length:
            return False
        else:
            return True

    def upper_case(password):
            upper=[]
            for char in password:
                if char. isupper():
                    upper.append(char)
            if len(upper)==0:
                return False
            else:
                return True

            
    def lower_case(password):
        lower=[]
        for char in password:
            if char .islower():
                lower.append(char)
        if len(lower)==0:
            return False
        else:
            return True
            
    def digits(password):
        digits=[]
        for char in password:
            if char.isdigit():
                digits.append(char)

        if len(digits)==0:
            return False
        else:
            return True

    def special_character(password):
        special_character=[]
        for char in password:
            if not char.isalnum() and not char.isspace():
                special_character.append(char)
        if len(special_character)==0:
            return False
        else:
            return True

    def analyze_password(): 
        password_error=[]
        if special_character(password)==False:
            password_error.append("use special character")
        if digits(password)==False:
            password_error.append("use digits")
        if  lower_case(password)==False:
            password_error.append("use lower case letters")
        if  upper_case(password)==False:
            password_error.append("use upper case letter")
        if minimum_length(minimum_length=8)==False:
            password_error.append("mimium length is 8")
        if len(password_error)==0:
            return "PASSWORD SUCCESSFUL"
        else:
            return password_error
            

    password_result=analyze_password()
    print(password_result)
          
    