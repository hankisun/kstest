from loguru import logger
import argparse
import random
import re
import sys
import json

logger.remove()
logger.add(sys.stdout, format="{level} {message}", level="INFO")

def new_tab_dict(title=""):
    return {
        "title": title,
        "columns": [],
        "contents": [],
        "before_sep_bar": True
    }

def check_doc_title(l):
    if m := re.search(r"^#+\s*(.+)", l):
        return m.groups()[0]
    return None

def parse_table_row(l):
    if m := re.findall(r"\|([^\|]+)", l):
        return m
    return None

def check_table_column(l, tab_dict):
    if tab_dict["before_sep_bar"] is False:
        return None
    return parse_table_row(l)  

def is_seperation_bar(l):
    if m := re.search(r"^\|(?:\s*\:?-+\:?\s*\|)+", l):
        logger.debug(f"{m.span()} {len(l)}")
        if m.span()[1] == len(l):
            return True
    return False

def is_md_table(l):
    if m := re.search(r"^\|", l):
        return True
    return False

def insert_to_tab_dict(l, tab_dict):
    if is_seperation_bar(l):
        tab_dict["before_sep_bar"] = False
    elif columns := check_table_column(l, tab_dict):
        logger.debug(columns)
        tab_dict['columns'] = [column.strip() for column in columns]
    else: # contents
        parsed = parse_table_row(l)
        tab_dict['contents'].append({column: content.strip() for (column, content) in zip(tab_dict['columns'], parsed)})

def read_md(path):
    docs = []
    tab_dict = new_tab_dict()
    
    with open(path) as f:
        while True:
            l = f.readline()
            if not l:
                break
            l = l.strip()
            if title := check_doc_title(l):
                if tab_dict["contents"]:
                    docs.append(tab_dict)
                tab_dict = new_tab_dict(title)
            elif is_md_table(l):
                insert_to_tab_dict(l, tab_dict)

    logger.debug(json.dumps(docs, ensure_ascii=False, indent=2))
    logger.info(f"{len(docs)} tables are loaded")
    return docs

def write_in_english_loop(contents):
    correct = 0
    incorrect = 0
    cnt = len(contents)
    print("Please write in English (Q to go back)")
    print()

    for i, idx in enumerate(random.sample(range(0, cnt), k=cnt)):
        print('-'*5 + f" [{i+1:3}/{cnt:3}] " + '-'*5)
        print()
        print(">>> " + contents[idx]["Kor"])
        print(">>> ", end="")
        answer = input()
        if answer.upper() == 'Q':
            print("go back")
            break
        print()
        if answer == contents[idx]["Eng"]:
            print("    Correct! Great!!")
            correct += 1
        else:
            print("    Incorrect..")
            incorrect += 1
            print("*** " + contents[idx]["Eng"])

        print()
        print(f"(Correct {correct:3} / Incorrect {incorrect:3})")
        print()
    print("=== Finished! Congratulations! ===")
    return (correct, incorrect)

def main(docs):
    while True:
        print("=== English Writing Test ===")
        print("1. Test ALL")
        print("2. Select a Table")
        print()
        selection = input("Select a number (Q to quit) : ")

        print()
        if selection.upper() == "Q":
            print("quit")
            break
        
        if selection == '1':
            print("[Test ALL]")
            contents = [content for tab in docs for content in tab["contents"]]
            write_in_english_loop(contents)
        elif selection == '2':
            back_flag = False
            while True:
                print("[Select a Table]")
                tab_list = [tab["title"] for tab in docs]
                for i, title in enumerate(tab_list):
                    print(f"{i+1}. {title}")
                print()
                print("Select a table number (Q to go back) : ")
                selection = input("Enter table number: ")
                if selection.upper() == "Q":
                    back_flag = True
                    break
                try:
                    selection = int(selection)
                except ValueError as e:
                    print("Only Number is accepted. try again..")
                    continue
                selection -= 1
                if selection >= 0 and selection < len(tab_list):
                    break
                else:
                    print("Invalid number. Try again...")
            
            if back_flag:
                print("go back")
                continue
            else:
                contents = docs[selection]["contents"]
                write_in_english_loop(contents)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    
    docs = read_md(args.path)
    main(docs)

