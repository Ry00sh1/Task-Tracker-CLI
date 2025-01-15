# todo_cli/main.py

from argparse import ArgumentParser
from todo_cli.tasks import add_task, delete_task, list_tasks, mark_done, mark_in_progress

def main() -> None:
    parser = ArgumentParser(description= "CLI ToDo App.")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Add a new task.")
    parser_add.add_argument("description", type=str, help="Task description.")

    parser_list = subparsers.add_parser("list", help="List tasks.")
    parser_list.add_argument(
        "status",
        nargs="?",
        choices=['todo','in-progress','done'],
        help="Filter tasks by status."
    )

    parser_delete = subparsers.add_parser("delete", help="Delete a task.")
    parser_delete.add_argument(
        "id",
        type=int,
        help="The ID of the target task."
    )

    parser_done = subparsers.add_parser("mark-done", help="Mark a task as 'done'.")
    parser_done.add_argument(
        "id",
        type=int,
        help="The ID of the target task."
    )

    parser_inprogress = subparsers.add_parser("mark-in-progress", help="Mark a task as 'in-progress'.")
    parser_inprogress.add_argument(
        "id",
        type=int,
        help="The ID of the target task."
    )

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-done":
        mark_done(args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(args.id)

if __name__ == "__main__":
    main()