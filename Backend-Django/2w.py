lion_cubs = []

def register_lion_cub():
    name = input("아기사자 이름을 입력하세요: ")
    track = input("트랙을 입력하세요: ")
    season = input("기수를 입력하세요: ")
    
    lion_cub = {
        "이름": name, 
        "트랙": track, 
        "기수": season}
    lion_cubs.append(lion_cub)
    print(f"{name} 아기사자가 등록되었습니다.")

def search_name():
    search_name = input("검색할 아기사자 이름을 입력하세요: ")
    found = False
    for cub in lion_cubs:
        if cub["이름"] == search_name:
            print(f"이름: {cub['이름']}\n트랙: {cub['트랙']}\n기수: {cub['기수']}")
            found = True
            break
    if not found:
        print(f"{search_name} 아기사자는 등록되지 않았습니다.")

def search_track():
    search_track = input("조회할 트랙명을 입력하세요: ")
    found = False
    print(f"\n📋 {search_track} 트랙 아기사자 명단")
    
    for cub in lion_cubs:
        if cub["트랙"] == search_track:
            print(f"- {cub['이름']} ({cub['기수']}기)")
            found = True
    
    if not found:
        print(f"{search_track} 트랙에 속한 아기사자가 없습니다.")

def main():
    while True:
        print("\n기능을 선택하세요\n")
        print("1. 아기사자 등록")
        print("2. 이름으로 검색")
        print("3. 트랙으로 조회")
        print("4. 종료")
        choice = input("선택: ")
        
        if choice == '1':
            register_lion_cub()
        elif choice == '2':
            search_name()
        elif choice == '3':
            search_track()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()