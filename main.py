import re
import phonenumbers
import streamlit as st

# Check if given input has any valid url
def is_valid_url(url):
    regex = r"((http|https)://)?[a-zA-Z0-9./-]+[.][a-zA-Z]{2,}+[.][a-zA-Z]{2,}"
    pattern = re.compile(regex)
    return pattern.search(url).group() if pattern.search(url) else None

# Check if given input has any valid phone number
def is_valid_phone_number(text):
    numbers_list = []
    numbers = phonenumbers.PhoneNumberMatcher(text= text, region="IN")
    for value in numbers:
        numbers_list.append(value.number.national_number)
        return numbers_list
    
class User1:
    def __init__(self, user_data = ""):
        self.user_data = user_data

    def streamlit_ui(self):
        st.title("URL and Phone Number Extractor")
        st.write("Enter User Data")
        self.user_data = st.text_input("User Data", "Enter Data Here")
        st.button("Submit")
        st.write("Valid URL(s): ", self.get_user_data()[0])
        st.write("Valid Phone Number(s): ", self.get_user_data()[1])
        for url in self.get_user_data()[0]:
            domain = url.split('.')[1].capitalize()
            st.write(f"Click here to go to [{domain}] {url}")

    def get_user_data(self):
        data = self.user_data
        url_list =[]
        while data is not None:
            url = is_valid_url(url=data)
            if url is not None:
                url_list.append(url)
                data = data.replace(url, "")
            else:
                break
        numbers_list = is_valid_phone_number(data)
        return url_list, numbers_list


if __name__ == "__main__":
    b_obj = User1(user_data="")
    b_obj.streamlit_ui()

