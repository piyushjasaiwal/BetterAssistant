from assistant import Assistant

class Assistant_CLI:

    def main(self):
        self.assistant = Assistant()
        should_continue = "yes"
        while True:
            if "q" in should_continue or "quit" in should_continue or "Q" in should_continue:
                save_chat = input("Would you like to save the chat, Master?\n")
                if "no" in save_chat:
                    print("Bye Master, Take Care")
                    break

                file_name = input("Any preferred name for the chat file, Master?\n")
                if file_name is None or file_name.strip() == "" or "no" in file_name or "any" in file_name:
                    file_name = "logs"
                
                self.assistant.export(filename=file_name)
                print("Bye Master, Take Care")
                break
            
            query = input("What is your query master\n")
            response = self.assistant.ask(query=query)
            print(f"Master, The answer to your query {query} is: ")
            print(f"{response}\n")
            should_continue = input("Press enter to continue/Type Q or quit to exit")


if __name__ == "__main__":
    assistant_cli = Assistant_CLI()
    assistant_cli.main()
