def generate_advice(bmi, glucose, smoke, drink):
    advice = ""
    if bmi >= 25:
        advice += "- 과체중: 체중 감량 필요\n"
    if glucose >= 126:
        advice += "- 고혈당: 의사 상담 권장\n"
    if smoke:
        advice += "- 흡연: 당뇨 위험 증가\n"
    if drink:
        advice += "- 음주: 혈당 조절 저해 가능\n"
    return advice or "건강한 생활습관을 유지하고 계십니다!"
