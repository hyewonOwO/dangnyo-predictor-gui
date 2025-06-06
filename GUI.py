from logic.predictor import get_prediction
from logic.advice import generate_advice
import tkinter as tk
import numpy as np
import joblib

# =========================
# 모델 불러오기
# =========================
model = joblib.load("model/diabetes_model.pkl")

# =========================
# 기능 함수들
# =========================

# 프레임 전환 함수
def show_frame(frame):
    for f in (frame_start, frame_input, frame_result):
        f.pack_forget()
    frame.pack(expand=True)

# 결과 보기 기능 함수 (모델 예측 포함)
def show_result():
    try:
        # 사용자 입력 가져오기
        name = entry_name.get()
        age = int(entry_age.get())
        sex = 0 if var_gender.get() == 1 else 1  # 남:0, 여:1
        bmi = float(entry_bmi.get())
        glucose = float(entry_family.get())
        smoke = var_smoke.get()
        drink = var_drink.get()

        # 입력 디버깅 출력
        print("입력 확인:")
        print("이름:", name)
        print("나이:", age)
        print("성별:", sex)
        print("BMI:", bmi)
        print("공복혈당:", glucose)
        print("흡연:", smoke)
        print("음주:", drink)

        # 예측 및 조언
        result, proba = get_prediction(model, age, sex, bmi, glucose, smoke, drink)
        advice = generate_advice(bmi, glucose, smoke, drink)

        # 결과 디버깅 출력
        print("모델 결과:", result, "확률:", proba)

        # 결과 표시
        if result == 1:
            result_label.config(text=f"⚠️ {name} 님, 당뇨 위험: {proba*100:.1f}%")
        else:
            result_label.config(text=f"✅ {name} 님, 정상 범위입니다! 위험도: {proba*100:.1f}%")

        advice_label.config(text=advice)
        show_frame(frame_result)

    except Exception as e:
        result_label.config(text=f"입력 오류: {e}")
        advice_label.config(text="값을 정확히 입력했는지 확인해주세요.")
        show_frame(frame_result)

# =========================
# 메인 윈도우 설정
# =========================
root = tk.Tk()
root.title("당뇨 예측 및 관리 프로그램")
root.geometry("800x600")

# =========================
# 프레임 1: 시작 화면
# =========================
frame_start = tk.Frame(root)
tk.Label(frame_start, text="당뇨 예측 및 관리\n프로그램", font=("Arial", 20), justify="center").pack(pady=60)
tk.Button(frame_start, text="시작하기", font=("Arial", 14), command=lambda: show_frame(frame_input)).pack()
frame_start.pack(expand=True)

# =========================
# 프레임 2: 입력 화면
# =========================
frame_input = tk.Frame(root)
tk.Label(frame_input, text="건강 정보 입력", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=20)

# 이름 입력 추가
tk.Label(frame_input, text="이름:", width=11, font=("Arial", 12)).grid(row=1, column=0, sticky='e')
entry_name = tk.Entry(frame_input, width=17)
entry_name.grid(row=1, column=1, sticky='w')

tk.Label(frame_input, text="나이:", width=11, font=("Arial", 12)).grid(row=2, column=0, sticky='e')
entry_age = tk.Entry(frame_input, width=17)
entry_age.grid(row=2, column=1, sticky='w')

tk.Label(frame_input, text="성별:", width=11, font=("Arial", 12)).grid(row=3, column=0, sticky='e')
var_gender = tk.IntVar()
tk.Radiobutton(frame_input, text="남", variable=var_gender, value=1).grid(row=3, column=1, sticky='w')
tk.Radiobutton(frame_input, text="여", variable=var_gender, value=2).grid(row=3, column=1, sticky='e')

tk.Label(frame_input, text="BMI:", width=11, font=("Arial", 12)).grid(row=4, column=0, sticky='e')
entry_bmi = tk.Entry(frame_input, width=17)
entry_bmi.grid(row=4, column=1, sticky='w')

tk.Label(frame_input, text="공복혈당:", font=("Arial", 12)).grid(row=5, column=0, sticky='e')
entry_family = tk.Entry(frame_input, width=17)
entry_family.grid(row=5, column=1, sticky='w')

tk.Label(frame_input, text="흡연:", width=11, font=("Arial", 12)).grid(row=6, column=0, sticky='e')
var_smoke = tk.IntVar()
tk.Radiobutton(frame_input, text="유", variable=var_smoke, value=1).grid(row=6, column=1, sticky='w')
tk.Radiobutton(frame_input, text="무", variable=var_smoke, value=0).grid(row=6, column=1, sticky='e')

tk.Label(frame_input, text="음주:", width=11, font=("Arial", 12)).grid(row=7, column=0, sticky='e')
var_drink = tk.IntVar()
tk.Radiobutton(frame_input, text="유", variable=var_drink, value=1).grid(row=7, column=1, sticky='w')
tk.Radiobutton(frame_input, text="무", variable=var_drink, value=0).grid(row=7, column=1, sticky='e')

tk.Button(frame_input, text="결과보기", font=("Arial", 14), command=show_result).grid(row=8, column=0, columnspan=2, pady=30)

# =========================
# 프레임 3: 결과 화면
# =========================
frame_result = tk.Frame(root)

tk.Label(frame_result, text="당뇨병 위험 결과", font=("Arial", 16)).pack(pady=10)

result_label = tk.Label(frame_result, text="", font=("Arial", 14))
result_label.pack(pady=5)

advice_label = tk.Label(frame_result, text="", font=("Arial", 12))
advice_label.pack(pady=5)

tk.Button(frame_result, text="뒤로가기", command=lambda: show_frame(frame_input)).pack(pady=10)

# =========================
# 메인 루프
# =========================
root.mainloop()
