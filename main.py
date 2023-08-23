import streamlit as st 


# main code comes here

st.header("test - bot")

user_input =  st.text_input("Enter your question here ")
run_button =   st.button("Run")




if(run_button and user_input != ""):

    user_input_file =  open("user_input.txt", "w")
    print(user_input)
    user_input_file.write(str(user_input)+ "\n")
    user_input_file.close()
    # activate engine 
    file_2 = open("engine_start.txt", "w")
    file_2.write("1\n")
    file_2.close()

    # writing response
    alfa = 1
    while(alfa != 0):
        engine_off = open("engine_start.txt", "r").readline()
        #print(engine_off)
        try:
            alfa = int(engine_off)
        except:
            alfa = 1
        if(alfa == 0):
            data_1 = open("response.txt", "r").readlines()
            st.write(data_1)
            
