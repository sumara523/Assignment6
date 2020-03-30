def URLSplit(input):
    input = input.replace(":/", "")
    return input.split("/")