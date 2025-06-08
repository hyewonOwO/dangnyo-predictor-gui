def generate_detailed_advice(bmi, glucose, smoke, drink):
    advice_text = f"""
[당신의 건강 상태 요약]

BMI: {bmi:.1f} (정상: 18.0 ~ 25.0)
→ {"정상 범위입니다."
    if 18 < bmi < 25
        else ("과체중입니다. 체중 감량을 위한 식단 관리와 유산소 운동이 필요합니다."
    if bmi >= 25
        else "저체중입니다. 체중 증가를 위한 균형 잡힌 영양 섭취가 필요합니다.")}

공복혈당: {glucose:.1f} mg/dL (정상: 70 ~ 126)
→ {"정상 범위입니다."
    if 70 < glucose < 126
        else ("고혈당 상태입니다. 정제 탄수화물을 피하고 의사와의 상담이 필요합니다."
    if glucose >= 126
        else "저혈당 상태입니다. 충분한 영양 섭취가 필요합니다.")}

흡연: {"흡연 중" if smoke else "비흡연"}
→ {"흡연은 당뇨 합병증 위험을 증가시킵니다. 금연을 권장합니다." if smoke else "좋은 습관을 유지하고 계십니다."}

음주: {"음주 중" if drink else "비음주"}
→ {"음주는 혈당 조절에 악영향을 줄 수 있습니다. 절주 또는 금주를 권장합니다." if drink else "좋은 습관을 유지하고 계십니다."}
"""
    return advice_text
