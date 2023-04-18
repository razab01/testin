import streamlit as st
def find_largest_num(a, b, c):
    largest = max(a, b, c)
    return largest
def main():
    st.title("Find the largest number among three given numbers")
    st.write("Enter three numbers below:")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find the largest number"):
        largest_num = find_largest_num(num1, num2, num3)
        st.write("The largest number is:", largest_num)
if __name__ == "__main__":
    main()
