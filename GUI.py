from logic.predictor import get_prediction
from logic.advice import generate_advice
from logic.advice_detail import generate_detailed_advice
import tkinter as tk
import joblib

# =========================
# 모델 불러오기
# =========================
model = joblib.load("model/diabetes_model.pkl")

# =========================
# 기능 함수들
# =========================

def show_frame(frame):
    for f in (frame_start, frame_input, frame_result, frame_advice):
        f.pack_forget()
    frame.pack(expand=True)

def show_result():
    try:
        global user_bmi, user_glucose, user_smoke, user_drink

        name = entry_name.get()
        age = int(entry_age.get())
        sex = 0 if var_gender.get() == 1 else 1
        bmi = float(entry_bmi.get())
        glucose = float(entry_family.get())
        smoke = var_smoke.get()
        drink = var_drink.get()

        # 사용자 수치 저장 (관리 프레임에서 사용)
        user_bmi = bmi
        user_glucose = glucose
        user_smoke = smoke
        user_drink = drink

        result, proba = get_prediction(model, age, sex, bmi, glucose, smoke, drink)
        advice = generate_advice(bmi, glucose, smoke, drink)

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

def show_advice():
    bmi = user_bmi
    glucose = user_glucose
    smoke = user_smoke
    drink = user_drink

    advice_text = generate_detailed_advice(bmi, glucose, smoke, drink)
    advice_text_label.config(text=advice_text)
    show_frame(frame_advice)

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
tk.Button(frame_start, text="시작하기", font=("Arial", 14), command=lambda: show_frame(frame_input)).pack(pady=10)
frame_start.pack(expand=True)

# =========================
# 프레임 2: 입력 화면
# =========================
frame_input = tk.Frame(root)
tk.Label(frame_input, text="건강 정보 입력", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=20)

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

tk.Button(frame_input, text="결과보기", font=("Arial", 14), command=show_result).grid(row=8, column=0, columnspan=2, pady=20)
tk.Button(frame_input, text="← 뒤로가기", font=("Arial", 10), command=lambda: show_frame(frame_start)).grid(row=9, column=0, columnspan=2)

# =========================
# 프레임 3: 결과 화면
# =========================
frame_result = tk.Frame(root)
tk.Label(frame_result, text="당뇨병 위험 결과", font=("Arial", 16)).pack(pady=10)
result_label = tk.Label(frame_result, text="", font=("Arial", 14))
result_label.pack(pady=5)
advice_label = tk.Label(frame_result, text="", font=("Arial", 12))
advice_label.pack(pady=5)

btn_result_row = tk.Frame(frame_result)
btn_result_row.pack(pady=10)
tk.Button(btn_result_row, text="당뇨 관리 방법", font=("Arial", 14), command=show_advice).pack(side='left', padx=5)

tk.Button(frame_result, text="← 뒤로가기", font=("Arial", 10), command=lambda: show_frame(frame_input)).pack(pady=5)

# =========================
# 프레임 4: 당뇨 관리 프레임
# =========================
frame_advice = tk.Frame(root)
tk.Label(frame_advice, text="당뇨 관리 조언", font=("Arial", 18)).pack(pady=20)

advice_text_label = tk.Label(frame_advice, text="", font=("Arial", 12), justify="left")
advice_text_label.pack(padx=20, pady=10)

tk.Button(frame_advice, text="← 뒤로가기", font=("Arial", 12), command=lambda: show_frame(frame_result)).pack(pady=20)

# =========================
# 메인 루프
# =========================
show_frame(frame_start)
root.mainloop()
