import os
import sys
import shutil
import pathlib

DIR = os.path.realpath(os.path.dirname(sys.argv[0]));
TEMPLATE_PROJECT_NAME = "sketch_TEMPLATE"
TEMPLATE_PROJECT_DIR = f"{DIR}/{TEMPLATE_PROJECT_NAME}"


def start_new_project(): # 新しくプロジェクトを作成する。
    PROJECT_BASE_NAME = "sketch_" + str(input("\nプロジェクト名を入力してください：").replace(" ","_").replace("-","_"))
    HAVE_SUBPROJECT = yes_or_no("サブプロジェクトを作成しますか。[y/N]")
    LOOP_COUNT = 1
    if HAVE_SUBPROJECT:
        LOOP_COUNT = int(input("作成するサブプロジェクト数:"))

    for i in range(LOOP_COUNT):
        PROJECT_NAME = PROJECT_BASE_NAME
        if HAVE_SUBPROJECT:
            PROJECT_NAME += "_" + str(i)
        PROJECT_DIR = f"{DIR}/{PROJECT_NAME}"
        if os.path.exists(PROJECT_DIR):
            print("プロジェクトファイルがすでに存在します。")
        else:
            print(f"新しいプロジェクトを {PROJECT_DIR} に作成中...")

            shutil.copytree(f"{TEMPLATE_PROJECT_DIR}",f"{PROJECT_DIR}")
            os.rename(
                f"{PROJECT_DIR}/{TEMPLATE_PROJECT_NAME}.pde",
                f"{PROJECT_DIR}/{PROJECT_NAME}.pde")
            print("プロジェクトを正常に作成しました。")
        print("Finished")
def create_template():  #Processingプロジェクトファイルのテンプレートを作成。
    print(f"プロジェクトテンプレート({TEMPLATE_PROJECT_NAME}) が見つかりませんでした.\nテンプレートフォルダを以下のパスの作成しています {TEMPLATE_PROJECT_DIR}...")
    os.makedirs(f"{TEMPLATE_PROJECT_DIR}",exist_ok=True)
    program_file = pathlib.Path(f"{TEMPLATE_PROJECT_DIR}/{TEMPLATE_PROJECT_NAME}.pde")
    program_file.touch()
    print(f"Project template file created.")

def yes_or_no(message):
    while True:
        choice = input(message).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False

def main(): 
    if os.path.exists(TEMPLATE_PROJECT_DIR):
        start_new_project()
    else :
        create_template()# テンプレートがなければ作成する。
        start_new_project()

    input("\nエンターを押してプログラムを終了します。");

if __name__ == "__main__":
    main()