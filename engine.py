from engine_component import get_ai_response
import time 
#def main_function():



if __name__ == '__main__':
    while(True):
        alfa = 0
        while(alfa != 1):
            engine_activation = open("engine_start.txt", "r").readline()
            try:
                if(int(engine_activation) == 1):
                    print(engine_activation)
                    user_input = open("user_input.txt", "r").readline()
                    print("user input is ::-   {}".format(user_input))
                    response = get_ai_response(user_input)
                    # writing back response
                    data_1 = open("response.txt", "w")
                    data_1.write(response)
                    data_1.close()  # type: ignore
                    # closging the engine

                    alfa = engine_activation

                    # reversing the engine
                    engine_activation = open("engine_start.txt", "w")
                    engine_activation.write("0\n")
                    engine_activation.close()

                    print("process completed successfully")
            except Exception as e:
                print(e)
