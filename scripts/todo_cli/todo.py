import time
import sys
import os

arg = sys.argv
todo_file = "todo.txt"
done_file = "done.txt"
archive_file = "archive.txt"


def option_help():
    sys.stdout.buffer.write('''
    Commands :
      add \"todo item\"\t\t\tAdd a new todo.
      ls\t\t\t\tShow remaining todos.
      del NUMBER\t\t\tDelete a todo.
      done NUMBER\t\t\tComplete a todo.
      help\t\t\t\tShow usage.
      report\t\t\t\tStatistics.
      archive\t\t\t\tArchives all the completed task

    General Options
      -h, --help\t\t\tShow help.
      -v, --version\t\t\tShow version and exit.
      -p, --print <file>\t\tPrints the file: (t)odo, (d)one, (a)rchive
      '''.encode('utf8'))


def option_add(todo_to_add):
    todo_add = " ".join(todo_to_add)
    with open(todo_file, "a") as f1:
        f1.write(todo_add + '\n')
    print(f"Added todo: \"{todo_add}\"")


def option_ls():
    todo = []
    try:
        with open(todo_file, "r") as f1:
            for i in f1:
                todo.append(i)
        for i in range(len(todo) - 1, -1, -1):
            sys.stdout.buffer.write("[{}] {}\n".format(i + 1, todo[i][:-1]).encode('utf8'))
    except FileNotFoundError:
        print("There are no pending todos!")


def option_del(todo_to_delete):
    try:
        with open(todo_file, "r") as f1:
            todo = f1.readlines()
        if todo_to_delete > len(todo) or todo_to_delete == 0:
            print(f"Error: todo #{todo_to_delete} does not exist. Nothing deleted.")
        else:
            todo.remove(todo[todo_to_delete - 1])
            with open(todo_file, "w") as f1:
                for i in todo:
                    f1.write(i)
            print("Deleted todo #{}".format(todo_to_delete))
    except FileNotFoundError:
        print("There are no pending todos! Nothing deleted.")
    except ValueError:
        print("Error: Enter a NUMBER. Nothing deleted.")


def option_done(mark_done):
    try:
        with open(todo_file, "r") as f1:
            todo = f1.readlines()
        if mark_done > len(todo) or mark_done == 0:
            print("Error: todo #{} does not exist.".format(mark_done))
            return

        dodo = todo[mark_done - 1]
        todo.remove(dodo)
        with open(todo_file, "w") as f1, open(done_file, "a") as f2:
            for i in todo:
                f1.write(i)
            t = time.localtime()
            f2.write(f"{t.tm_year}-{t.tm_mon:02}-{t.tm_mday:02} {dodo}")
        print(f"Marked todo #{mark_done} as done.")
        print(f"Yay! Only {len(todo)} task(s) are left.")
    except FileNotFoundError:
        print("There are no pending todos! Nothing marked Done.")
    except ValueError:
        print("Error: Enter a NUMBER. Nothing marked Done.")


def option_report():
    len_todo = 0
    len_done = 0
    t = time.localtime()
    try:
        with open(todo_file, "r") as f1:
            len_todo = len(f1.readlines())
    except FileNotFoundError:
        pass
    try:
        with open(done_file, "r") as f2:
            len_done = len(f2.readlines())
    except FileNotFoundError:
        pass
    print(f"{t.tm_year}-{t.tm_mon:02}-{t.tm_mday:02} Pending : {len_todo} Completed : {len_done}")


def option_archive():
    try:
        with open(done_file, 'r') as f2:
            todo = f2.readlines()
        os.remove(done_file)
        with open(archive_file, 'a') as f3:
            for i in todo:
                f3.write(i)
        print("All task completed are archived")
    except FileNotFoundError:
        print("Error: No task done to archive. Complete the pending task now!")


def option_print(file_code):

    if file_code == 't':
        try:
            with open(todo_file, 'r') as f1:
                print('\nToDo List:')
                for i in f1:
                    print(i[:-1])
        except FileNotFoundError:
            print("There are no pending todos!")
    elif file_code == 'd':
        try:
            with open(done_file, 'r') as f2:
                print('\nDone List:')
                for i in f2:
                    print(i[:10], '\t', i[10:-1])
        except FileNotFoundError:
            print("Nothing has been marked as done")
    elif file_code == 'a':
        try:
            with open(archive_file, 'r') as f3:
                print('\nArchive List:')
                for i in f3:
                    print(i[:10], '\t', i[10:-1])
        except FileNotFoundError:
            print("Nothing in archives")
    else:
        print("Enter the correct argument")


if len(arg) == 1 or arg[1] in ["help", '-h', "--help"]:
    option_help()
elif arg[1] == "add":
    if len(arg) == 2:
        print("Error: Missing todo string. Nothing added!")
    else:
        option_add(arg[2:])
elif arg[1] == "ls":
    option_ls()
elif arg[1] == "del":
    if len(arg) < 3:
        print("Error: Missing NUMBER for deleting todo.")
    else:
        option_del(int(arg[2]))
elif arg[1] == "done":
    if len(arg) == 2:
        print("Error: Missing NUMBER for marking todo as done.")
    else:
        option_done(int(arg[2]))
elif arg[1] == "report":
    option_report()
elif arg[1] == "--version" or arg[1] == '-v':
    print("ToDo 1.0")
elif arg[1] == "archive":
    option_archive()
elif arg[1] == "--print" or arg[1] == '-p':
    if len(arg) < 3:
        print("No file name entered!")
    else:
        option_print(arg[2])
else:
    print("ERROR: unknown command \"{}\"".format(arg[1]))
