import streamlit as st
from PIL import Image
import pytesseract
import wolframalpha

# Wolfram Alpha API Client
WOLFRAM_ALPHA_APP_ID = '83KT9P-H6VXW857KV'
client = wolframalpha.Client(WOLFRAM_ALPHA_APP_ID)

def solve_equation(equation):
    try:
        res = client.query(equation)
        answer = next(res.results).text
        return answer
    except:
        return "Could not solve the equation"

def main():
    st.title("Equation Solver")
    st.sidebar.markdown("Equation Solver")
    st.subheader("This app allows you to solve basic math questions.")
    st.subheader("\n Mathematics")
    st.markdown("Solve Linear equations, Quadratic equations, Simultaneous equations solve etc.")
    st.write("\n* Linear equations, solve: 3x + 4 = 16",
            "\n* Quadratic equations solve: x^2 - 5x + 6 = 0",
            "\n* Simultaneous equations solve: 2x + 3y = 14, 6x - y =12"
            "\n* Solve: (x^2 -1)/(x^4-x)")

    st.write("Upload an image of the equation you want to solve or write the equation in the text input below.")

    # Option to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Convert image to text
        st.write("Converting image to text...")
        equation = pytesseract.image_to_string(image)
        st.write(f"Detected Equation: {equation}")

        # Solve the equation
        if equation:
            st.write("Solving the equation...")
            solution = solve_equation(equation)
            st.write(f"Solution: {solution}")
        else:
            st.write("No equation detected in the image.")

    # Option to input text directly
    st.write("Or you can write the equation directly:")
    user_equation = st.text_input("Enter the equation here:")
    if user_equation:
        st.write("Solving the equation...")
        solution = solve_equation(user_equation)
        st.write(f"Solution: {solution}")

if __name__ == "__main__":
    main()