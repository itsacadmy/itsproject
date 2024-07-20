import streamlit as its

its.title("Welcome to ITS Academy")
its.header("Institute of Traditional Studies !")
its.subheader("Learn Web Development and Programming Languages with us in a Simple manner !")

its.markdown("Let's Start Coding....")
its.code("""for i in range(1,5,1)):
        print("Hello")
            """)
   
name=its.text_input("Enter Your Name: ")
fname=its.text_input("Enter Your Father's Name: ")
adr = its.text_area("Enter Your Address: ")

classdata = its.selectbox("Enter Your class : ",(1,2,3,4,5,6))

button = its.button("Submit")
if button:
    its.markdown(f"""
    Name : {name}
    Father Name: {fname}
    Address : {adr}
    Class : {classdata}
    """) 
