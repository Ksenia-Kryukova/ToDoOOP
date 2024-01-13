from .args_parser import args_parser
from .commands import create_command, Command, CommandResult


def main():
    args = args_parser()
    command: Command = create_command(args)

    try:
        result: CommandResult = command.execute()
    except ToDoListBaseException as exception:
        ErrorPrinter(exception).print()
    else:
        SuccessPrinter(result).print()
