def is_valid_name(name):
    return name.strip() != ""


def input_baby_lion_names():
    lion_names = []

    print("🦁 아기 사자 명단 관리 프로그램입니다.")

    while True:
        name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")

        if name == "q":
            print("\n📌 이름 입력을 종료합니다.")
            break
        elif not is_valid_name(name):
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
        else:
            lion_names.append(name)
            print(f"✅ '{name}' 이(가) 등록되었습니다.")

    return lion_names


def print_baby_lion_names(lion_names):
    print("\n📋 현재 아기 사자 명단입니다.")

    if len(lion_names) == 0:
        print("등록된 아기 사자가 없습니다.")
    else:
        for index, name in enumerate(lion_names, start=1):
            print(f"🦁 {index}. {name}")


def main():
    baby_lion_list = input_baby_lion_names()
    print_baby_lion_names(baby_lion_list)


if __name__ == "__main__":
    main()