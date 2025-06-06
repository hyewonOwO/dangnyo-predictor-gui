import joblib
import numpy as np

# 모델 불러오기
model = joblib.load("diabetes_model.pkl")

# 사용자 입력 예시 (여기선 Entry로부터 받은 값들을 가정)
age = int(entry_age.get())
sex = 0 if gender_var.get() == "남" else 1
bmi = float(entry_bmi.get())
glucose = float(entry_glu.get())
smoke = 1 if smoke_var.get() == "유" else 0
drink = 1 if drink_var.get() == "유" else 0

# 입력값 배열로 묶기
user_input = np.array([[age, sex, bmi, glucose, smoke, drink]])

# 예측 수행
result = model.predict(user_input)[0]
proba = model.predict_proba(user_input)[0][1]

# 결과 표시
if result == 1:
    result_label.config(text=f"⚠️ 당뇨 위험: {proba*100:.1f}%")
else:
    result_label.config(text=f"✅ 정상: 위험도 {proba*100:.1f}%")

