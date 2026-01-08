HISTORY_FILE = "calculation_history.txt"


def save_to_history(expression, result):
    file = open(HISTORY_FILE, "a")
    file.write(expression + " = " + str(result) + "\n")
    file.close()


def show_history():
    try:
        file = open(HISTORY_FILE, "r")
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            print("📭 No history available.")
        else:
            print("\n📜 Calculation History:")
            for line in reversed(lines):
                print("   ➤", line.strip())

    except FileNotFoundError:
        print("⚠️ History file not found.")


def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("🧹 History cleared successfully!")


def calculate(expression):
    operators = ["+", "-", "*", "/", "%"]
    operator = None

    for op in operators:
        if op in expression:
            operator = op
            break

    if operator is None:
        print("❌ Invalid expression. Use + - * / %")
        return

    try:
        numbers = list(map(float, expression.split(operator)))
    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    if len(numbers) < 2:
        print("⚠️ Enter at least two numbers.")
        return

    result = numbers[0]

    for num in numbers[1:]:
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            if num == 0:
                print("🚫 Error: Division by zero!")
                return
            result /= num
        elif operator == "%":
            if num == 0:
                print("🚫 Error: Modulus by zero!")
                return
            result %= num

    if int(result) == result:
        result = int(result)

    print(f"✅ Result: 🎯 {result}")
    save_to_history(expression, result)


def main():
    print("\n🧮✨ Welcome to Smart Calculator ✨🧮")
    print("🔢 Supports multiple & multi-digit numbers")
    print("➕ Operators: +  -  *  /  %")
    print("📜 Commands: history | clear | exit\n")

    while True:
        user_input = input("👉 Enter calculation: ").strip()

        if user_input.lower() == "exit":
            print("👋 Thank you for using Smart Calculator!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)


main()
