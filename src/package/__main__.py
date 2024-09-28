from package.cli import cli


# Have to do it like this so pyproject.toml can find the main entry point
def main():
    cli()


if __name__ == "__main__":
    main()
