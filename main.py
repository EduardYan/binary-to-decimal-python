#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

def bin_to_decimal(binary):
    try:
      decimal = int(binary, 2)
      return decimal
    except ValueError:
        return None

def decimal_to_bin(decimal):
    try:
        binary = bin(int(decimal))[2:]
        return binary
    except ValueError:
        return None
      

def display_result(title, input_value, result):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(title, style="cyan", justify="center")
    table.add_column("Result", style="green", justify="center")
    table.add_row(str(input_value), str(result))
    console.print(table)

def main():
    console = Console()
    
    welcome_message = "Welcome to the binary-decimal converter"
    panel = Panel(welcome_message, title="Instructions 🚀", style="bold blue")
    console.print(panel)
    
    try:
      while True:
        choice = Prompt.ask("Select conversion type:", choices=["b", "d"], default="Binary")

        if choice.lower() == 'binary' or choice.lower() == 'b':
            binary_input = Prompt.ask("Enter a binary number")
            decimal_result = bin_to_decimal(binary_input)
            
            if decimal_result is not None:
                  display_result("Binary", binary_input, decimal_result)
            else:
                  console.print("Invalid input. Please enter a valid binary number.", style='bold red')

        elif choice.lower() == 'decimal' or choice.lower() == 'd':
            decimal_input = Prompt.ask("Enter a decimal number")
            binary_result = decimal_to_bin(decimal_input)
            
            if binary_result is not None:
                  display_result("Decimal", decimal_input, binary_result)
            else:
                  console.print("Invalid input. Please enter a valid decimal number.", style='bold red')

        else:
            console.print("Invalid choice. Please enter 'Binary' or 'Decimal.'", style='bold red')
            
    except KeyboardInterrupt:
      console.print("\nGood Bye 👋", style='bold blue')

if __name__ == "__main__":
    main()
