def arithmetic_arranger(problems, showSolution=False):
    # Key: ops = operators, arr_problems = arranged_problems, ss = show_solution
    operators = ["+", "-"]
    arrangedProblems = ""
    
    # Check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    fourthLine = ""
    
    for operation in problems:
        # Split the operation into terms
        try:
            terms = operation.split()
        except:
            return "Error: Problem not a string."
        
        # Extract terms and operator
        try:
            first, operator, second = terms
        except:
            return "Error: Not correctly formatted. Use spaces between terms."
        
        # Check if terms are integers
        try:
            firstTerm = int(first)
            secondTerm = int(second)
        except:
            return "Error: Numbers must only contain digits."
        
        # Check if the operator is valid
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers are more than four digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the result of the operation
        if operator == "+":
            solution = firstTerm + secondTerm
        else:
            solution = firstTerm - secondTerm
        
        solutionStr = str(solution)
        
        # Create the formatted lines
        firstLine += " " * (2 + max(len(first), len(second)) - len(first)) + first + "    "
        secondLine += operator + " " * (1 + max(len(first), len(second)) - len(second)) + second + "    "
        thirdLine += "-" * (max(len(first), len(second)) + 2) + "    "
        fourthLine += " " * (2 + max(len(first), len(second)) - len(solutionStr)) + solutionStr + "    "
    
    # Remove trailing spaces
    firstLine = firstLine.rstrip()
    secondLine = secondLine.rstrip()
    thirdLine = thirdLine.rstrip()
    fourthLine = fourthLine.rstrip()
    
    # Combine the lines into the arranged problems
    arrangedProblems = firstLine + "\n" + secondLine + "\n" + thirdLine
    if showSolution:
        arrangedProblems += "\n" + fourthLine
    
    return arrangedProblems
