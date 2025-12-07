from message_queue.engine import Engine

def main():
    engine = Engine(num_producers=3, num_consumers=2)
    engine.start()
    engine.wait()

if __name__ == "__main__":
    main()
