import argparse
import sys

from commands.dimension import dimension
from commands.compare import compare

class TerritorioCLI:
    CLI_VERSION = "Territorio CLI 1.0.0"

    def __init__(self):
        self.__run()

    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog="territorio",
            epilog="Desenvolvido por: Luis H. Silva",
            description="Case Técnico Estágio ScientifiCloud",
            usage="%(prog)s [options]"
        )
        self.parser.version = self.CLI_VERSION

        self.parser.add_argument("-v", "--version", action="version")
        
        subparsers = self.parser.add_subparsers(dest="command")
        self.__create_dimension_subparser(subparsers)
        self.__create_compare_subparser(subparsers)

        parse_args = self.parser.parse_args()
        if parse_args and parse_args.command:
            try:
                command = parse_args.command.lower()
                if  command == "dimension":
                    dimension(parse_args.id, parse_args.path_to_image)
                elif command == "compare":
                    compare(parse_args.id1, parse_args.id2, parse_args.path_to_image)
            except Exception as e:
                print(f"Argumento invalido: {e}")
        else: 
            self.parser.print_help()
        sys.exit()

    def __create_dimension_subparser(self, subparsers):
        self.dimensions_parser = subparsers.add_parser(
            "dimension", 
            help="Provides the territory's dimension and generates a bar chart."
        )
        self.dimensions_parser.add_argument("id", help="ID of the territory to be analyzed")
        self.dimensions_parser.add_argument("path_to_image", type=str, help="Path to the image file where the output chart will be saved")

    def __create_compare_subparser(self, subparsers):
        self.dimensions_parser = subparsers.add_parser(
            "compare", 
            help="Compares the dimensions of two territories and generates a comparative bar chart between them."
        )
        self.dimensions_parser.add_argument("id1", help="ID of the first territory to be compared")
        self.dimensions_parser.add_argument("id2", help="ID of the second territory to be compared")
        self.dimensions_parser.add_argument("path_to_image", type=str,  help="Path to the image file where the output chart will be saved")
