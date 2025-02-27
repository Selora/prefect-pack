import marvin  # type: ignore
from prefect import flow


@flow
def main():
    # use of marvin proves we have an OPENAI_API_KEY
    marvin.generate(str, instructions="Something jerry seinfeld would say")  # type: ignore


if __name__ == "__main__":
    main()
