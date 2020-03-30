def URLSplit(input):
    input = input.replace(":/", "")

    input = input.split("/") 

    if len(input) > 3:
        for i in range (2, len(input)):
            if i == len(input) - 1:
                input[2] = input[2] + input[i]
            elif i == 2:
                input[2] = input[i] + "/"
            else:
                input[2] = input[2] + input[i] + "/"

    input = [input[0],input[1], input[2]]
    return input