# fulling functional code:
def arithmetic_arranger(problems, true_false_check = False):

    if len(problems) > 5:
        return "Error: Too many problems."
    
    # arranged_problems = ""
    first_line_str = ""
    second_line_str = ""
    underscore_line_str = ""
    answer_line_str = ""
    
    # start of formating each problem
    for each_problem in problems:
        # error check for mutiplication and division
        if each_problem.__contains__("/") or each_problem.__contains__("*"):
            return "Error: Operator must be '+' or '-'."

        # breaks string into parts and find length of longest string
        this_problem_list = each_problem.split()
        longest_string_in_problem = len(max(this_problem_list, key=len))

        # determine formatting width
        format_width = longest_string_in_problem + 2

        # name some variables
        first_number = this_problem_list[0]
        second_number = this_problem_list[2]
        operator = this_problem_list[1]

        # A way to check if numeric
        if (first_number.isnumeric() == False) or (second_number.isnumeric() == False):
            return "Error: Numbers must only contain digits."
        
        # Check for max number of digits
        if longest_string_in_problem > 4:
            return "Error: Numbers cannot be more than four digits."

        # does the math
        if operator == "+":
            answer = (int(first_number) + int(second_number))
        elif operator == "-":
            answer = (int(first_number) - int(second_number))

        # spacing and underscore formatting
        first_line_number_of_spaces = (format_width - len(first_number))
        second_line_number_of_spaces = (format_width - len(second_number) -1)
        if true_false_check == True:
            answer_line_number_of_spaces = (format_width - len(str(answer)))
        else:
            answer_line_number_of_spaces = format_width

        first_line_spaces = ""
        second_line_spaces = ""
        underscore = ""
        answer_line_spaces = ""

        for dash in range(format_width):
            underscore += '-'
        for spaces1 in range(first_line_number_of_spaces):
            first_line_spaces += " "
        for spaces2 in range(second_line_number_of_spaces):
            second_line_spaces += " "
        for spaces3 in range(answer_line_number_of_spaces):
            answer_line_spaces += " "
        
        # formats each line
        first_line = first_line_spaces+first_number
        second_line = operator+second_line_spaces+second_number
        underscore_line = underscore # not strickly needed but makes things easier to follow
        if true_false_check == True:
            answer_line = answer_line_spaces+str(answer)
        else:
            answer_line = answer_line_spaces

        # formats the lines together
        first_line_str += (first_line + "    ")
        second_line_str += (second_line + "    ")
        underscore_line_str += (underscore_line + "    ")
        answer_line_str += (answer_line + "    ")

    # makes it shiny!
    first_line_str = str.rstrip(first_line_str)
    second_line_str = str.rstrip(second_line_str)
    underscore_line_str = str.rstrip(underscore_line_str)
    answer_line_str = str.rstrip(answer_line_str)
    if true_false_check == True:
        arranged_problems = f'{first_line_str}\n{second_line_str}\n{underscore_line_str}\n{answer_line_str}'
    else:
        arranged_problems = f'{first_line_str}\n{second_line_str}\n{underscore_line_str}'
    return arranged_problems

# If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
# The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
# Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
# Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.