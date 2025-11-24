questions = ("Should you use smoking to relax?",
            "How many hours of sleep to suitable for young people?", 
            "What is the most important meal of the day?",
            "Where is the best place to exercise?", 
            "Who is the founder of Microsoft?"
            )
options = (("A. Noway", "B. Not", "C. Banned", "D. Yes"),
           ("A. 7p.m", "B. 10p.m", "C. 3a.m", "D. 12a.m"),
           ("A. vegetable", "B. fast food", "C. coca", "D. sugar"),
           ("A. at libraby", "B. at restaurant", "C. at park", "D. at cafe"),
           ("A. Bill Gates", "B. Beyoncé", "C. Auta", "D. Vaniessa"))
answers = ("C", "B", "A", "C", "A")
guesses = []
score = 0
question_num = 0
for q in questions:
    print("-------------------")
    print(q)
    for o in options[question_num]:
        print(o)
    
    guess = input("Nhập chọn 1 đáp án: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Chính xác!")
    else:
        print("Sai rồi!")
        print(f"Đáp án chuẩn: {answers[question_num]}")
    question_num += 1
print("-------------------")
print(" Kết quả cuối cùng ")
print("-------------------")
print("Đáp án chuẩn:", end=" ")
for a in answers:
    print(a, end=" ")
print()
print("Đáp án đã chọn của bạn:", end=" ")
for g in guesses:
    print(g, end=" ")
print()
score = int(score/len(questions)*100)
print(f"Điểm số của bạn là: {score}%")
