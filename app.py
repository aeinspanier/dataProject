from utils.parsing import parse_queue_msg
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


if __name__ == "__main__":
    parse_queue_msg.get_queue_msg()
