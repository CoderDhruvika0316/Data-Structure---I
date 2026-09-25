scores = [2, 5, 6, 8, 7, 3, 9, 1, 4]

target = int(input(f"List : {scores}\nEnter a number you want ot find from the scores list:"))

step = 0
for i in scores:
    step += 1

    if i == target:
        break

print(f"Position : {step}   |   Steps : {step}   | Target : {target}")

formula = len(scores) // 2
print(f"Best Case : {formula}   |   Worst Case : {step}")