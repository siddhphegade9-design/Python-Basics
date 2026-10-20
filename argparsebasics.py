import argparse

parser = argparse.ArgumentParser(description="Simple Calculator.")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()

if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "sub":
    result = args.num1 - args.num2
elif args.operation == "mul":
    result = args.num1 * args.num2
elif args.operation == "div":
    if args.num2 == 0:
        parser.error("Cannot divide by zero")
    result = args.num1 / args.num2

print(f"{args.num1} {args.operation} {args.num2} = {result}")

#While executing the script first the terminal will be empty we will need to execute python "{name of the file}" {num1} {num2} {operation} in the terminal to get the result. For example, python argparsebasics.py 10 5 add will give us the result of 10 + 5 = 15.0


