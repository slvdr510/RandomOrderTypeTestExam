import json, random, os, subprocess, platform, time

current_script_path = os.path.abspath(__file__)
current_script_directory = os.path.dirname(current_script_path)

def main():
    global random_order
    global seconds_after_correct
    global seconds_after_error
    global abs_json_file_route
    
    # >>> Modify the next values to use the script as you'd like <<<<
    
    random_order = True                 # True or False
    seconds_after_correct = 0.25        # Seconds to wait after a correct answer
    seconds_after_error = 0             # Seconds to wait after an incorrect answer
    json_file_name = 'teoria_fisica'    # Change this value to the name of your .json file. Default: 'teoria_fisica'
    
    # To use this program for your own purposes, you must create a .json file with the following format:
    # [{"question:"Matrix","option":["option one","option two"],"correctOption": "1"}]
    
    
    abs_json_file_route = os.path.join(current_script_directory,json_file_name+'.json')
    
    try:
        with open(abs_json_file_route, 'rb') as read_file:
            jsonPalabras = json.load(read_file)
    except Exception as e:
        print(f"\nError: {e}\n")
    
    beginExam(jsonPalabras)

def cls():
    system = platform.system()
    if system == 'Windows':
        subprocess.run('cls', shell=True)
    elif system in ('Linux', 'Darwin'):
        subprocess.run('clear', shell=True)

def beginExam(json_data):
    try:
        
        if random_order:
            random.shuffle(json_data)

        failed_questions = []
        failed_answer_count = 0
        correct_answer_count = 0

        for questionNumber, data in enumerate(json_data):
            cls()
            
            print(f"{str(questionNumber+1)}. {data.get('question')}\n")
            
            for option in range(len(data.get('option'))):
                print(f"{option+1}. {data.get('option')[option]}")
            print("")
            eleccion = input("Your answer is... ")
            
            if eleccion == data.get('correctOption'):
                print('\nCorrect! 🎉')
                correct_answer_count+=1
                time.sleep(seconds_after_correct)
            else:
                print(f"\nError! ☹️\n\n{data.get('correctOption')}. {data.get('option')[int(data.get('correctOption'))-1]}\n")
                failed_answer_count+=1
                failed_questions.append(f"{str(questionNumber+1)}. {data.get('question')}\n{(data.get('correctOption'))}. {data.get('option')[int(data.get('correctOption'))-1]}\n\n")
                time.sleep(seconds_after_error)

            cls()

        print(f"Right answers: {correct_answer_count} ✔️  | Wrong answers: {failed_answer_count} ❌\n\n")

        for fallo in failed_questions:
            print(f"{str(fallo)}")
            
        print(f"Right answers: {correct_answer_count} ✔️  | Wrong answers: {failed_answer_count} ❌\n\n")

    except Exception as e:
        print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()

#
#             ╔█████████  ██╗  ██╗       ██╗ ██████╗   ███████╗   █████████    ██   ███████ 
#             ██══════╗   ██║   ██╗     ██╗  ██    ██║  ██╔══██║  ██         █ ██  ██     ██
#              ████████   ██║    ██╗   ██╗   ██    ██║  ██████╝   █████████    ██  ██     ██
#              ╚══════██  ██║     ██╗ ██╗    ██    ██║  ██╔══██╗         ██    ██  ██     ██
#             █████████╝  ███████╗  ███╝     ██████╝    ██║  ██║  ██     ██    ██  ██     ██
#             ╚═══════╝   ╚══════╝  ╚═╝      ╚════╝     ╚═╝  ╚═╝    █████      ██   ███████ 
#               
#                       https://github.com/slvdr510/randomOrderTypeTestExam