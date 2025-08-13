from assistant import Assistant

class Assistant_CLI:

    def main(self):
        self.assistant = Assistant()
        while True:
            query = input("What is your query master\n")

            if "exit" in query or "quit" in query:
                save_chat = input("Would you like to save chat Master?\n")
                if "no" in save_chat:
                    print("Bye Master, Take Care")
                    break

                file_name = input("Any preferred name for the chat Master?\n")
                if file_name is None or file_name.strip() == "" or "no" in file_name or "any" in file_name:
                    file_name = "logs"
                
                self.assistant.export(filename=file_name)
                print("Bye Master, Take Care")
                break
            
            self.assistant.ask(query=query) # type: ignore

if __name__ == "__main__":
    assistant_cli = Assistant_CLI()
    assistant_cli.main()
