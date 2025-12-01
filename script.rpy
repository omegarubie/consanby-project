git add# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('로보', color="#1100ff")


# 여기에서부터 게임이 시작합니다.
label start:

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    return
label start:
    e "안녕"
    e "너가 날 만들었어"
    e "정말 반가워"
    return
python:
    name=renpy.input("네 이름은 뭐야?")
    name=name.strip() or "수줍은 청년"
return
define g = Character('[name]', color="#83e95b")



label start:

    g "내 이름은 [name](이)라고 해."
return

label start:
    e "[name]? 정말 예쁜 이름이다! 너무 좋아!"
    e "있잖아, 있잖아? 여기서 나가더라도 날 잊지 말아줘. 알았지?"
    