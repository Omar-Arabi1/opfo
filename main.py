from cli.cli import Cli
from cli.check import check_config
from util.config_obj import Config

def main():
    cli = Cli()
    args = cli.setup()
    config = Config()
    config_file = config.create_config_file()
    config.generate_default_config(file_path=config_file)


if __name__ == "__main__":
    main()
