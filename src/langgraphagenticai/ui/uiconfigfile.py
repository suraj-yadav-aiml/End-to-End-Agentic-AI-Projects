from configparser import ConfigParser, ParsingError

class Config:
    def __init__(self, config_file_path="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        try:
            with open(config_file_path, 'r', encoding='utf-8-sig') as f: 
                self.config.read_file(f)
        except FileNotFoundError:
            raise ValueError(f"Configuration file not found: {config_file_path}")
        except PermissionError:
            raise ValueError(f"Permission denied accessing: {config_file_path}")
        except ParsingError as e:
            raise ValueError(f"INI syntax error in {config_file_path}: {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error reading config: {str(e)}")

        # Verify DEFAULT section exists
        if 'DEFAULT' not in self.config:
            raise ValueError("Missing [DEFAULT] section in config file")


    def get_llm_options(self):
        value = self.config['DEFAULT'].get('LLM_OPTIONS', '')
        return [opt.strip() for opt in value.split(',')] if value else []

    def get_usecase_options(self):
        value = self.config['DEFAULT'].get('USECASE_OPTIONS', '')
        return [opt.strip() for opt in value.split(',')] if value else []

    def get_groq_model_options(self):
        value = self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS', '')
        return [model.strip() for model in value.split(',')] if value else []

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE', 'Default Title')
    

if __name__ == "__main__":
    try:
        config = Config()
        print(config.get_llm_options())
        print(config.get_usecase_options())
        print(config.get_groq_model_options())
        print(config.get_page_title())
    except ValueError as ve:
        print(f"Configuration Error: {ve}")