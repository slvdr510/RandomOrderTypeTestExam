import json, random, os, subprocess, platform, time

current_script_path = os.path.abspath(__file__)
current_script_directory = os.path.dirname(current_script_path)


#             ╔█████████  ██╗  ██╗       ██╗ ██████╗   ███████╗   █████████    ██   ███████ 
#             ██══════╗   ██║   ██╗     ██╗  ██    ██║  ██╔══██║  ██         █ ██  ██     ██
#              ████████   ██║    ██╗   ██╗   ██    ██║  ██████╝   █████████    ██  ██     ██
#              ╚══════██  ██║     ██╗ ██╗    ██    ██║  ██╔══██╗         ██    ██  ██     ██
#             █████████╝  ███████╗  ███╝     ██████╝    ██║  ██║  ██     ██    ██  ██     ██
#             ╚═══════╝   ╚══════╝  ╚═╝      ╚════╝     ╚═╝  ╚═╝    █████      ██   ███████ 
#               
#                       https://github.com/slvdr510/randomOrderTypeTestExam


# >>> Modify the next values to use the script as you'd like <<<<

random_order = True
seconds_after_correct = 0.5
seconds_after_error = 2

# Name of the .json file with the words and definitions. (My .json name is 'teoria_fisica', change it as you create new files.)
json_file_name = 'teoria_fisica'
# NOTE: Follow the following format [{"question:"Matrix","option":["option one","option two"],"correctOption": "1"}]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def cls():
    system = platform.system()
    if system == 'Windows':
        subprocess.run('cls', shell=True)
    elif system in ('Linux', 'Darwin'):
        subprocess.run('clear', shell=True)

abs_json_file_route = os.path.join(current_script_directory,json_file_name+'.json')

def beginExam(json_data):
    try:
        
        if random_order:
            random.shuffle(json_data)

        failed_questions = []
        failed_answer_count = 0
        correct_answer_count = 0

        for questionNumber, data in enumerate(json_data):
            cls()
            
            print(f"\n\n{str(questionNumber+1)}. {data.get('question')}\n")
            
            for option in range(len(data.get('option'))):
                print(f"{option+1}. {data.get('option')[option]}")
            print("")
            eleccion = input("Your answer is... ")
            
            if eleccion == data.get('correctOption'):
                print('\nCorrect!')
                correct_answer_count+=1
                time.sleep(int(seconds_after_correct))
            else:
                print(f"\nError!\n\n{data.get('correctOption')}. {data.get('option')[int(data.get('correctOption'))-1]}\n")
                failed_answer_count+=1
                failed_questions.append(f"QUESTION\n{str(questionNumber+1)}. {data.get('question')}\nANSWER:\n{(data.get('correctOption'))}. {data.get('option')[int(data.get('correctOption'))-1]}\n\n")
                time.sleep(int(seconds_after_error))

            cls()

        print(f"\n\nFailed answers: {failed_answer_count}❌ | Correct answers: {correct_answer_count}✔️\n\n")

        for fallo in failed_questions:
            print(f"{str(fallo)}")

    except Exception as e:
        print(f"\nError: {e}\n")

with open(abs_json_file_route, 'rb') as read_file:
    jsonPalabras = json.load(read_file)

beginExam(jsonPalabras)
